# 🐳 Docker Setup - Paradisias Hotel API

Guide complet pour construire, déployer et utiliser l'API Paradisias Hotel avec Docker.

## 📋 Prérequis

- Docker 20.10+
- Docker Compose 2.0+
- Compte DockerHub (pour le déploiement)

## 🚀 Déploiement Rapide

### Option 1: Utiliser l'image depuis DockerHub

```bash
# Télécharger et lancer l'API
docker run -p 9001:9001 lesage20/paradisias-api:latest

# Accéder à l'API
curl http://localhost:9001/
```

### Option 2: Construire localement

```bash
# Cloner le projet
git clone <repository-url>
cd paradApi

# Construire l'image
docker build -t paradisias-api .

# Lancer le conteneur
docker run -p 9001:9001 paradisias-api
```

### Option 3: Docker Compose (Recommandé)

```bash
# Lancer tous les services (API + PostgreSQL + Redis)
docker-compose up -d

# Voir les logs
docker-compose logs -f web

# Arrêter les services
docker-compose down
```

## 🔧 Configuration

### Variables d'Environnement

Copiez `env.example` vers `.env` et modifiez selon vos besoins :

```bash
cp env.example .env
```

Variables importantes :
- `DEBUG`: Mode debug (False en production)
- `SECRET_KEY`: Clé secrète Django
- `ALLOWED_HOSTS`: Domaines autorisés
- `PORT`: Port d'écoute (défaut: 9001)

### Base de Données

**SQLite (par défaut)**
```bash
# Aucune configuration requise
docker run -p 9001:9001 lesage/paradisias-api:latest
```

**PostgreSQL**
```bash
# Avec Docker Compose
docker-compose up -d postgres web
```

## 📦 Construction et Déploiement

### Script Automatisé

```bash
# Rendre le script exécutable
chmod +x deploy.sh

# Déployer vers DockerHub
./deploy.sh v1.0 votre-username-dockerhub
```

### Commandes Manuelles

```bash
# Construction
docker build -t votre-username/paradisias-api:v1.0 .

# Test local
docker run -p 9001:9001 votre-username/paradisias-api:v1.0

# Upload vers DockerHub
docker push votre-username/paradisias-api:v1.0
```

## 🌐 Endpoints Disponibles

Une fois l'API lancée sur le port 9001 :

- **Documentation Swagger**: http://localhost:9001/
- **Admin Django**: http://localhost:9001/admin/
- **API Hotels**: http://localhost:9001/hotel/
- **API Reports**: http://localhost:9001/reports/
- **API Comptes**: http://localhost:9001/accounts/

## 🔍 Surveillance et Santé

### Vérifications de Santé

```bash
# Vérifier l'état du conteneur
docker ps

# Voir les logs
docker logs container-name

# Tester l'endpoint de santé
curl http://localhost:9001/
```

### Métriques Docker

```bash
# Utilisation des ressources
docker stats

# Informations sur l'image
docker inspect lesage/paradisias-api:latest
```

## 🛠 Développement

### Mode Développement

```bash
# Construire pour le développement
docker build -f Dockerfile.dev -t paradisias-api-dev .

# Lancer avec volumes pour hot-reload
docker run -p 9001:9001 -v $(pwd):/app paradisias-api-dev
```

### Debug

```bash
# Accéder au shell du conteneur
docker exec -it container-name bash

# Voir les processus Django
docker exec -it container-name ps aux

# Collecter les fichiers statiques
docker exec -it container-name python manage.py collectstatic
```

## 📊 Performance

### Configuration Recommandée

**Production:**
- CPU: 2+ cores
- RAM: 1GB+
- Storage: 10GB+

**Optimisations:**
- Workers Gunicorn: 2 × CPU cores
- Timeout: 120s
- Max requests: 1000

## 🔒 Sécurité

### Bonnes Pratiques

1. **Utilisateur non-root**: Le conteneur utilise l'utilisateur `django`
2. **Secrets**: Utilisez des variables d'environnement
3. **HTTPS**: Configurez un reverse proxy (nginx/traefik)
4. **Firewall**: Limitez l'accès au port 9001

### Configuration Nginx (Exemple)

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:9001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 📝 Maintenance

### Mise à Jour

```bash
# Télécharger la nouvelle version
docker pull lesage/paradisias-api:latest

# Redémarrer avec la nouvelle image
docker-compose pull && docker-compose up -d
```

### Sauvegarde

```bash
# Sauvegarder la base de données
docker exec container-name python manage.py dumpdata > backup.json

# Sauvegarder les volumes
docker run --rm -v paradisias_media_volume:/data -v $(pwd):/backup alpine tar czf /backup/media-backup.tar.gz /data
```

## 🐛 Dépannage

### Problèmes Courants

**Port 9001 déjà utilisé:**
```bash
# Changer le port
docker run -p 8000:9001 lesage/paradisias-api:latest
```

**Problème de permissions:**
```bash
# Vérifier les permissions
docker exec -it container-name ls -la /app
```

**API ne répond pas:**
```bash
# Vérifier les logs
docker logs container-name

# Tester la connectivité
docker exec -it container-name curl localhost:9001
```

## 🤝 Support

- **Documentation**: Voir `API_DASHBOARD_DOCUMENTATION.md`
- **Issues**: Créer un ticket GitHub
- **Email**: support@paradisias-hotel.com

---

**🎉 Votre API Paradisias Hotel est maintenant prête à être déployée !** 