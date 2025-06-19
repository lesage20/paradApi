#!/bin/bash

# Script de déploiement Paradisias API vers DockerHub
# Usage: ./deploy.sh [version] [docker_username]

set -e

# Configuration par défaut
DEFAULT_VERSION="latest"
DEFAULT_USERNAME="lesage"  # Remplacez par votre nom d'utilisateur DockerHub
IMAGE_NAME="paradisias-api"

# Récupération des arguments
VERSION=${1:-$DEFAULT_VERSION}
DOCKER_USERNAME=${2:-$DEFAULT_USERNAME}
FULL_IMAGE_NAME="$DOCKER_USERNAME/$IMAGE_NAME:$VERSION"

echo "🚀 Déploiement de l'API Paradisias Hotel"
echo "📦 Image: $FULL_IMAGE_NAME"
echo "🐳 Port: 9001"
echo ""

# Vérification que Docker est en cours d'exécution
if ! docker info > /dev/null 2>&1; then
    echo "❌ Erreur: Docker n'est pas en cours d'exécution"
    exit 1
fi

# Nettoyage des images anciennes (optionnel)
echo "🧹 Nettoyage des images Docker anciennes..."
docker image prune -f || true

# Construction de l'image
echo "🔨 Construction de l'image Docker..."
docker build \
    --tag $FULL_IMAGE_NAME \
    --tag "$DOCKER_USERNAME/$IMAGE_NAME:latest" \
    --no-cache \
    .

if [ $? -eq 0 ]; then
    echo "✅ Image construite avec succès: $FULL_IMAGE_NAME"
else
    echo "❌ Erreur lors de la construction de l'image"
    exit 1
fi

# Test local rapide
echo "🧪 Test rapide de l'image localement..."
CONTAINER_ID=$(docker run -d -p 9001:9001 $FULL_IMAGE_NAME)

# Attendre que le conteneur démarre
sleep 10

# Vérifier que l'API répond
if curl -f http://localhost:9001/ > /dev/null 2>&1; then
    echo "✅ API répond correctement"
else
    echo "⚠️  L'API ne répond pas immédiatement (normal au premier démarrage)"
fi

# Arrêter le conteneur de test
docker stop $CONTAINER_ID > /dev/null
docker rm $CONTAINER_ID > /dev/null

# Connexion à DockerHub (si nécessaire)
echo "🔐 Connexion à DockerHub..."
if ! docker info | grep -q "Username: $DOCKER_USERNAME"; then
    echo "Veuillez vous connecter à DockerHub:"
    docker login
fi

# Push vers DockerHub
echo "📤 Upload vers DockerHub..."
docker push $FULL_IMAGE_NAME
docker push "$DOCKER_USERNAME/$IMAGE_NAME:latest"

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Déploiement réussi !"
    echo "📋 Informations de déploiement:"
    echo "   Image: $FULL_IMAGE_NAME"
    echo "   Latest: $DOCKER_USERNAME/$IMAGE_NAME:latest"
    echo "   Port: 9001"
    echo ""
    echo "🚀 Commandes pour utiliser l'image:"
    echo "   docker run -p 9001:9001 $FULL_IMAGE_NAME"
    echo "   docker run -p 9001:9001 $DOCKER_USERNAME/$IMAGE_NAME:latest"
    echo ""
    echo "🌐 L'API sera accessible sur: http://localhost:9001"
    echo "📚 Documentation Swagger: http://localhost:9001/"
else
    echo "❌ Erreur lors de l'upload vers DockerHub"
    exit 1
fi 