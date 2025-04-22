from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'votre_clé_secrète')

# Configuration de la base de données
def get_db_connection():
    try:
        # Essayer d'abord d'utiliser DATABASE_URL si disponible
        database_url = os.getenv('DATABASE_URL')
        if database_url:
            conn = psycopg2.connect(database_url)
        else:
            # Fallback sur les variables individuelles
            conn = psycopg2.connect(
                host=os.getenv('PGHOST', 'postgres.railway.internal'),
                database=os.getenv('PGDATABASE', 'railway'),
                user=os.getenv('PGUSER', 'postgres'),
                password=os.getenv('PGPASSWORD'),
                port=os.getenv('PGPORT', '5432')
            )
        return conn
    except psycopg2.Error as e:
        print(f"Erreur de connexion à la base de données: {e}")
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
    nom = request.form['nom']
    conn = get_db_connection()
    if conn is None:
        flash("Erreur de connexion à la base de données", "error")
        return redirect(url_for('index'))
    
    try:
        cur = conn.cursor()
        # Vérifier si la table existe
        cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'noms')")
        table_exists = cur.fetchone()[0]
        
        if not table_exists:
            init_db()
        
        cur.execute('INSERT INTO noms (nom) VALUES (%s)', (nom,))
        conn.commit()
        flash("Nom ajouté avec succès!", "success")
    except psycopg2.Error as e:
        flash(f"Erreur lors de l'ajout du nom: {e}", "error")
    finally:
        cur.close()
        conn.close()
    
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
