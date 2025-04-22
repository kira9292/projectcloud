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
   - Ajoutez un service PostgreSQL
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
   - Railway fournira automatiquement les variables d'environnement pour la base de données
   - Les variables seront injectées dans l'application lors du déploiement

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

4. Configurez les variables d'environnement dans un fichier `.env`

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