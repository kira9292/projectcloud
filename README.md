# Application Flask avec PostgreSQL

Une application web simple développée avec Flask et PostgreSQL, déployée sur Railway.

## 🚀 Application en ligne

L'application est disponible en ligne à l'adresse suivante :
[https://projectcloud-production.up.railway.app/](https://projectcloud-production.up.railway.app/)

## 📋 Fonctionnalités

- Ajout de noms dans une base de données PostgreSQL
- Affichage de la liste des noms
- Interface utilisateur moderne et responsive
- Gestion des erreurs et messages de confirmation

## 🛠️ Technologies utilisées

- **Backend** : Python, Flask
- **Base de données** : PostgreSQL
- **Déploiement** : Railway
- **Frontend** : HTML, CSS (Inter font)

## 🚀 Déploiement

L'application est déployée sur Railway, une plateforme de déploiement cloud qui offre :
- Déploiement automatique depuis GitHub
- Base de données PostgreSQL intégrée
- Mise à l'échelle automatique
- Monitoring et logs

## 🔧 Configuration requise

- Python 3.x
- PostgreSQL
- pip (gestionnaire de paquets Python)

## 📦 Installation

1. Clonez le dépôt :
```bash
git clone [URL_DU_REPO]
cd [NOM_DU_REPO]
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurez les variables d'environnement :
```bash
FLASK_APP=app.py
FLASK_ENV=development
```

4. Lancez l'application :
```bash
flask run
```

## 🔒 Sécurité

- Les variables d'environnement sensibles sont gérées par Railway
- Les connexions à la base de données sont sécurisées
- Protection contre les injections SQL

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request 