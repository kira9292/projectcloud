# Étape de build
FROM python:3.9-slim as builder

WORKDIR /app

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Création de l'environnement virtuel
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape de production
FROM python:3.9-slim

WORKDIR /app

# Copie de l'environnement virtuel depuis l'étape de build
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copie du code de l'application
COPY . .

# Configuration des variables d'environnement
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV HOSTNAME=::

# Exposition du port (Railway utilise la variable PORT)
EXPOSE $PORT

# Commande pour démarrer l'application avec Gunicorn en écoutant sur IPv6
CMD gunicorn --bind [::]:$PORT app:app 