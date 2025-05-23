from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import os
from dotenv import load_dotenv
import time

# Charger les variables d'environnement
load_dotenv()

# Vérifier que les variables sont bien chargées
print("Vérification des variables d'environnement...")
print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")
print(f"PGHOST: {os.getenv('PGHOST')}")
print(f"PGDATABASE: {os.getenv('PGDATABASE')}")
print(f"PGUSER: {os.getenv('PGUSER')}")
print(f"PGPORT: {os.getenv('PGPORT')}")

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'votre_clé_secrète')

# Configuration de la base de données
def get_db_connection(max_attempts=3, delay=5):
    for attempt in range(max_attempts):
        try:
            print(f"Tentative de connexion {attempt + 1}/{max_attempts}...")
            
            # URL de connexion fixe
            database_url = "postgresql://postgres:XryfpIdaudgshtRgNYIEgisVMDccpWtn@postgres.railway.internal:5432/railway"
            print(f"URL de connexion: {database_url}")
            
            conn = psycopg2.connect(database_url, connect_timeout=10)
            print("Connexion réussie!")
            return conn
        except psycopg2.Error as e:
            print(f"Erreur de connexion (tentative {attempt + 1}): {e}")
            if attempt < max_attempts - 1:
                print(f"Attente de {delay} secondes avant la prochaine tentative...")
                time.sleep(delay)
            else:
                print("Nombre maximum de tentatives atteint")
                return None

# Création de la table si elle n'existe pas
def init_db():
    conn = get_db_connection()
    if conn is None:
        return False
    
    try:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS noms (
                id SERIAL PRIMARY KEY,
                nom VARCHAR(100) NOT NULL
            )
        ''')
        conn.commit()
        cur.close()
        conn.close()
        return True
    except psycopg2.Error as e:
        print(f"Erreur lors de la création de la table: {e}")
        return False

@app.route('/')
def index():
    if not init_db():
        flash("Erreur de connexion à la base de données. Veuillez vérifier votre configuration.", "error")
    
    return render_template('index.html')

@app.route('/ajouter', methods=['POST'])
def ajouter():
    print("Début de la route /ajouter")
    nom = request.form['nom']
    print(f"Nom reçu: {nom}")
    
    conn = get_db_connection()
    if conn is None:
        print("Échec de la connexion à la base de données")
        flash("Erreur de connexion à la base de données", "error")
        return redirect(url_for('index'))
    
    try:
        print("Connexion réussie, création du curseur")
        cur = conn.cursor()
        
        # Vérifier si la table existe
        print("Vérification de l'existence de la table")
        cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'noms')")
        table_exists = cur.fetchone()[0]
        print(f"Table existe: {table_exists}")
        
        if not table_exists:
            print("Table n'existe pas, initialisation de la base")
            if not init_db():
                print("Échec de l'initialisation de la base")
                flash("Erreur lors de l'initialisation de la base de données", "error")
                return redirect(url_for('index'))
        
        print("Insertion du nom dans la base")
        cur.execute('INSERT INTO noms (nom) VALUES (%s)', (nom,))
        conn.commit()
        print("Insertion réussie")
        flash("Nom ajouté avec succès!", "success")
    except psycopg2.Error as e:
        print(f"Erreur PostgreSQL: {e}")
        flash(f"Erreur lors de l'ajout du nom: {e}", "error")
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        flash(f"Une erreur inattendue s'est produite: {e}", "error")
    finally:
        print("Fermeture des connexions")
        cur.close()
        conn.close()
    
    print("Redirection vers la liste")
    return redirect(url_for('liste'))

@app.route('/liste')
def liste():
    conn = get_db_connection()
    if conn is None:
        flash("Erreur de connexion à la base de données", "error")
        return redirect(url_for('index'))
    
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM noms ORDER BY id DESC')
        noms = cur.fetchall()
    except psycopg2.Error as e:
        flash(f"Erreur lors de la récupération des noms: {e}", "error")
        noms = []
    finally:
        cur.close()
        conn.close()
    
    return render_template('liste.html', noms=noms)

if __name__ == '__main__':
    if init_db():
        print("Base de données initialisée avec succès")
    else:
        print("Erreur lors de l'initialisation de la base de données")
    app.run(debug=True)
