# Application Flask avec PostgreSQL

Une application Flask simple qui permet d'ajouter et de visualiser des noms dans une base de données PostgreSQL.

## Configuration du déploiement sur Railway

### Prérequis
- Un compte GitHub
- Un compte Railway
- L'interface de ligne de commande Railway installée

### Étapes de configuration

1. **Configuration de Railway**
   - Créez un nouveau projet sur Railway
   - Ajoutez un service PostgreSQL :
     1. Cliquez sur "New Project"
     2. Sélectionnez "Provision PostgreSQL"
     3. Attendez que la base de données soit créée
   - Obtenez votre token d'authentification :
     ```bash
     railway token
     ```

2. **Configuration des secrets GitHub**
   - Allez dans les paramètres de votre dépôt GitHub
   - Naviguez vers "Secrets and variables" > "Actions"
   - Ajoutez le secret suivant :
     - `RAILWAY_TOKEN` : Votre token d'authentification Railway

3. **Configuration de la base de données**
   - Railway fournit automatiquement la variable d'environnement `DATABASE_URL`
   - Cette URL contient toutes les informations de connexion :
     - Host
     - Port
     - Nom de la base de données
     - Utilisateur
     - Mot de passe
   - L'application utilise automatiquement ces informations

### Déploiement automatique

Le déploiement est automatiquement déclenché lorsque des modifications sont poussées sur la branche `main`.

Le workflow CI/CD :
1. Configure l'environnement Python
2. Installe les dépendances
3. Exécute les tests (optionnel)
4. Déploie sur Railway

### Déploiement manuel

Pour déployer manuellement :
```bash
railway up
```

## Développement local

1. Clonez le dépôt
2. Créez un environnement virtuel :
```bash
python -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Configurez les variables d'environnement dans un fichier `.env` :
```bash
DATABASE_URL=postgresql://user:password@host:port/database
FLASK_SECRET_KEY=votre_clé_secrète
```

5. Lancez l'application :
```bash
python app.py
```

## Structure du projet

```
.
├── .github/
│   └── workflows/
│       └── main.yml
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   ├── index.html
│   └── liste.html
└── README.md
``` 