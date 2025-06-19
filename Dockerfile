# Utiliser Python 3.11 slim comme image de base pour des performances optimales
FROM python:3.11-slim

# Définir les métadonnées de l'image
LABEL maintainer="angezanou00@gmail.com" \
      description="API REST pour la gestion de Paradisias Hotel" \
      version="1.0"

# Définir les variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=paradApi.settings \
    PORT=9001

# Créer un utilisateur non-root pour la sécurité
RUN addgroup --system --gid 1001 django && \
    adduser --system --uid 1001 --gid 1001 --no-create-home django

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    gcc \
    libc6-dev \
    libpq-dev \
    libmagic1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . /app/

# Créer les répertoires nécessaires
RUN mkdir -p /app/static_cdn /app/media_cdn /app/logs && \
    chown -R django:django /app

# Changer vers l'utilisateur non-root
USER django

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port
EXPOSE 9001

# Définir les vérifications de santé
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python manage.py check --deploy || exit 1

# Commande de démarrage
CMD ["gunicorn", "--bind", "0.0.0.0:9001", "--workers", "3", "--timeout", "120", "paradApi.wsgi:application"] 