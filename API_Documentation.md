# Documentation API - Paradisias Hotel 🏨

## Vue d'ensemble
API REST complète pour la gestion d'un hôtel développée avec Django REST Framework.
- **Base URL**: `http://localhost:8000` (développement) ou `https://api.paradisias-hotel.com`
- **Documentation interactive**: `/` (Swagger UI)
- **Format**: JSON
- **Authentification**: JWT (JSON Web Tokens)

---

## 🔐 Authentification

### Endpoints d'authentification
| Méthode | Endpoint | Description |
|---------|-----------|-------------|
| `POST` | `/auth/login/` | Connexion utilisateur |
| `POST` | `/auth/logout/` | Déconnexion |
| `POST` | `/auth/token/refresh/` | Rafraîchir le token JWT |
| `POST` | `/auth/password/reset/` | Réinitialiser mot de passe |
| `POST` | `/auth/password/reset/confirm/` | Confirmer nouveau mot de passe |
| `POST` | `/auth/registration/` | Inscription nouvel utilisateur |

### Headers requis
```http
Authorization: Bearer <votre_token_jwt>
Content-Type: application/json
```

---

## 👥 Gestion des Utilisateurs (`/accounts/`)

### Profils Utilisateurs
| Méthode | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/accounts/profiles/` | Liste de tous les profils |
| `POST` | `/accounts/profiles/` | Créer un nouveau profil |
| `GET` | `/accounts/profiles/{id}/` | Détails d'un profil |
| `PUT` | `/accounts/profiles/{id}/` | Modifier un profil |
| `DELETE` | `/accounts/profiles/{id}/` | Supprimer un profil |

### Clients
| Méthode | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/accounts/clients/` | Liste des clients |
| `POST` | `/accounts/clients/` | Créer un client |
| `GET` | `/accounts/clients/{id}/` | Détails d'un client |
| `PUT` | `/accounts/clients/{id}/` | Modifier un client |
| `DELETE` | `/accounts/clients/{id}/` | Supprimer un client |

### Employés
| Méthode | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/accounts/employes/` | Liste des employés |
| `POST` | `/accounts/employes/` | Créer un employé |
| `GET` | `/accounts/employes/{id}/` | Détails d'un employé |
| `PUT` | `/accounts/employes/{id}/` | Modifier un employé |
| `DELETE` | `/accounts/employes/{id}/` | Supprimer un employé |

### Gestion des Droits
| Méthode | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/accounts/users/` | Liste des utilisateurs |
| `GET` | `/accounts/groups/` | Liste des groupes/rôles |
| `GET` | `/accounts/permissions/` | Liste des permissions |

---

## 🏨 Gestion Hôtelière (`/hotel/`)

### 🏢 Étages
| Méthode | Endpoint | Description | Filtres |
|---------|-----------|-------------|---------|
| `GET` | `/hotel/etages/` | Liste des étages | - |
| `POST` | `/hotel/etages/` | Créer un étage | - |
| `GET` | `/hotel/etages/{id}/` | Détails d'un étage | - |
| `PUT` | `/hotel/etages/{id}/` | Modifier un étage | - |
| `DELETE` | `/hotel/etages/{id}/` | Supprimer un étage | - |

**Structure des données:**
```json
{
  "id": 1,
  "name": "Premier étage",
  "description": "Chambres standard",
  "number": 1,
  "status": "actif",
  "created_at": "2023-01-01T10:00:00Z",
  "updated_at": "2023-01-01T10:00:00Z"
}
```

### 🛏️ Types de Chambres
| Méthode | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/hotel/types_chambre/` | Liste des types |
| `POST` | `/hotel/types_chambre/` | Créer un type |
| `GET` | `/hotel/types_chambre/{id}/` | Détails d'un type |
| `PUT` | `/hotel/types_chambre/{id}/` | Modifier un type |
| `DELETE` | `/hotel/types_chambre/{id}/` | Supprimer un type |

**Structure des données:**
```json
{
  "id": 1,
  "name": "Suite Deluxe",
  "description": "Suite avec vue sur mer",
  "numberAdult": 2,
  "numberChildren": 1,
  "price": 15000,
  "created_at": "2023-01-01T10:00:00Z",
  "updated_at": "2023-01-01T10:00:00Z"
}
```

### 🚪 Chambres
| Méthode | Endpoint | Description | Filtres |
|---------|-----------|-------------|---------|
| `GET` | `/hotel/chambres/` | Liste des chambres | `number`, `type` |
| `POST` | `/hotel/chambres/` | Créer une chambre | - |
| `GET` | `/hotel/chambres/{id}/` | Détails d'une chambre | - |
| `PUT` | `/hotel/chambres/{id}/` | Modifier une chambre | - |
| `DELETE` | `/hotel/chambres/{id}/` | Supprimer une chambre | - |

**Filtres disponibles:**
- `?number=101` - Filtrer par numéro de chambre
- `?type=1` - Filtrer par type de chambre

**Statuts des chambres:**
- `os` - Occupée Sale
- `og` - Occupée Gratuite  
- `op` - Occupée Propre
- `lp` - Libre Propre
- `ls` - Libre Sale
- `nettoyage` - En nettoyage

### 🎫 Coupons de Réduction
| Méthode | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/hotel/coupons/` | Liste des coupons |
| `POST` | `/hotel/coupons/` | Créer un coupon |
| `GET` | `/hotel/coupons/{id}/` | Détails d'un coupon |
| `PUT` | `/hotel/coupons/{id}/` | Modifier un coupon |
| `DELETE` | `/hotel/coupons/{id}/` | Supprimer un coupon |

### 📋 Réservations
| Méthode | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/hotel/reservations/` | Liste des réservations |
| `POST` | `/hotel/reservations/` | Créer une réservation |
| `GET` | `/hotel/reservations/{id}/` | Détails d'une réservation |
| `PUT` | `/hotel/reservations/{id}/` | Modifier une réservation |
| `DELETE` | `/hotel/reservations/{id}/` | Supprimer une réservation |

**Statuts des réservations:**
- `en attente` - En attente de confirmation
- `confirmée` - Réservation confirmée
- `annulée` - Réservation annulée

### 🏨 Locations/Séjours
| Méthode | Endpoint | Description | Filtres |
|---------|-----------|-------------|---------|
| `GET` | `/hotel/locations/` | Liste des locations | `checkIn_date`, `checkOut_date` |
| `POST` | `/hotel/locations/` | Créer une location | - |
| `GET` | `/hotel/locations/{id}/` | Détails d'une location | - |
| `PUT` | `/hotel/locations/{id}/` | Modifier une location | - |
| `DELETE` | `/hotel/locations/{id}/` | Supprimer une location | - |

**Filtres disponibles:**
- `?checkIn_date=2023-12-25` - Filtrer par date d'arrivée
- `?checkOut_date=2023-12-30` - Filtrer par date de départ

**Statuts des locations:**
- `pj` - Payé jour
- `dj` - Dette jour
- `dt` - Dette totale
- `dp` - Dette payée
- `archive` - Archivée

**Types de paiement:**
- `espece` - Espèce
- `cheque` - Chèque
- `visa` - Visa
- `devise` - Devise

### 🧾 Factures
| Méthode | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/hotel/factures/` | Liste des factures |
| `POST` | `/hotel/factures/` | Créer une facture |
| `GET` | `/hotel/factures/{id}/` | Détails d'une facture |
| `PUT` | `/hotel/factures/{id}/` | Modifier une facture |
| `DELETE` | `/hotel/factures/{id}/` | Supprimer une facture |

### 💰 Dépenses
| Méthode | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/hotel/depenses/` | Liste des dépenses |
| `POST` | `/hotel/depenses/` | Créer une dépense |
| `GET` | `/hotel/depenses/{id}/` | Détails d'une dépense |
| `PUT` | `/hotel/depenses/{id}/` | Modifier une dépense |
| `DELETE` | `/hotel/depenses/{id}/` | Supprimer une dépense |

---

## 📊 Exemples d'utilisation

### Créer une réservation
```bash
curl -X POST http://localhost:8000/hotel/reservations/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "guest": 1,
    "room": 101,
    "checkIn": "2023-12-25T14:00:00Z",
    "checkOut": "2023-12-30T11:00:00Z",
    "recorded_by": 1
  }'
```

### Rechercher des chambres libres
```bash
curl "http://localhost:8000/hotel/chambres/?status=lp" \
  -H "Authorization: Bearer <token>"
```

### Filtrer les locations par date
```bash
curl "http://localhost:8000/hotel/locations/?checkIn_date=2023-12-25" \
  -H "Authorization: Bearer <token>"
```

---

## 🔒 Permissions

Toutes les API utilisent le système de permissions Django (`DjangoModelPermissions`):
- **Lecture**: Nécessite la permission `view_<model>`
- **Création**: Nécessite la permission `add_<model>`
- **Modification**: Nécessite la permission `change_<model>`
- **Suppression**: Nécessite la permission `delete_<model>`

---

## 📝 Codes de Statut HTTP

| Code | Description |
|------|-------------|
| `200` | Succès |
| `201` | Créé avec succès |
| `400` | Données invalides |
| `401` | Non authentifié |
| `403` | Permission refusée |
| `404` | Ressource non trouvée |
| `500` | Erreur serveur |

---

## 🌐 Documentation Interactive

Accédez à la documentation Swagger interactive : `/`
- Interface graphique pour tester les API
- Schémas de données détaillés
- Exemples de requêtes et réponses 