# 📊 Documentation API Dashboard - Statistiques KPIs

Cette documentation détaille l'API unifiée de statistiques pour le dashboard de l'hôtel Paradisias.

## 🔐 Authentification

Toutes les APIs nécessitent une authentification JWT. Les utilisateurs doivent appartenir aux groupes appropriés :
- **Admin** : Accès complet avec filtrage par période et comparaisons
- **Gérant** : Accès aux données opérationnelles du jour
- **Autres rôles** : Accès refusé (403)

## 📈 API Unifiée KPIs

### Endpoint Principal

**URL :** `GET /reports/kpi/`

**Description :** API intelligente qui adapte automatiquement sa réponse selon le rôle de l'utilisateur connecté.

#### Comportement selon le rôle

- **Admin** : Retourne les KPIs avec filtrage par période et comparaisons avec la période précédente
- **Gérant** : Retourne les KPIs opérationnels du jour avec détails des entrées/sorties

#### Paramètres de requête (Admin uniquement)

| Paramètre | Type | Requis | Valeurs possibles | Description |
|-----------|------|--------|-------------------|-------------|
| `period` | string | Non | `today`, `week`, `month`, `quarter`, `semester`, `year` | Période à analyser (défaut: `today`) |

---

## 🎯 Exemples d'Utilisation

### Requête Admin avec Période

```bash
GET /reports/kpi/?period=month
Authorization: Bearer YOUR_JWT_TOKEN
```

#### Réponse Admin

```json
{
    "user_role": "admin",
    "period": "month",
    "periode_debut": "2025-06-01T00:00:00Z",
    "periode_fin": "2025-06-30T23:59:59Z",
    "revenu_total": "125000.00",
    "taux_occupation": "78.50",
    "revpar": "4687.50",
    "nombre_locations": 45,
    "revenu_total_precedent": "98000.00",
    "taux_occupation_precedent": "65.30",
    "revpar_precedent": "3687.50",
    "nombre_locations_precedent": 38,
    "evolution_revenu": "27.55",
    "evolution_taux_occupation": "20.21",
    "evolution_revpar": "27.13",
    "evolution_locations": "18.42",
    "date_derniere_mise_a_jour": "2025-06-14T15:30:00Z"
}
```

### Requête Gérant

```bash
GET /reports/kpi/
Authorization: Bearer YOUR_JWT_TOKEN
```

#### Réponse Gérant

```json
{
    "user_role": "gerant",
    "revenus_jour": "8500.00",
    "locations_actives": 12,
    "entrees_prevues": 3,
    "sorties_prevues": 2,
    "entrees_details": [
        {
            "reference": "BK001234",
            "client": "Dupont Jean",
            "chambre": "CH12",
            "heure_arrivee": "14:30",
            "montant": 15000.0
        }
    ],
    "sorties_details": [
        {
            "reference": "BK001230",
            "client": "Martin Claire",
            "chambre": "CH08",
            "heure_depart": "11:00",
            "montant_paye": 12500.0,
            "montant_du": 0.0
        }
    ],
    "date_du_jour": "2025-06-14",
    "date_derniere_mise_a_jour": "2025-06-14T15:30:00Z"
}
```

---

## 📊 Métriques Disponibles

### Pour les Admins

- **Revenu Total** : Somme des montants payés (`amountPaid`) des bookings
- **Taux d'Occupation** : (Chambres occupées / Total chambres) × 100
- **RevPAR** : Revenue Per Available Room = Revenu Total / Nombre total de chambres
- **Nombre de Locations** : Nombre total de bookings créés dans la période
- **Évolutions** : Pourcentage de changement par rapport à la période précédente

### Pour les Gérants

- **Revenus du Jour** : Somme des paiements reçus aujourd'hui
- **Locations Actives** : Bookings en cours (`status='ongoing'`)
- **Entrées Prévues** : Check-ins prévus aujourd'hui avec détails
- **Sorties Prévues** : Check-outs prévus aujourd'hui avec détails

---

## 📊 Résumé Global du Dashboard

**Endpoint :** `GET /reports/dashboard/summary/`

**Description :** Vue d'ensemble des statistiques principales pour tous les utilisateurs autorisés.

#### Exemple de requête

```bash
GET /reports/dashboard/summary/
Authorization: Bearer YOUR_JWT_TOKEN
```

#### Réponse JSON

```json
{
    "total_chambres": 16,
    "chambres_occupees": 8,
    "chambres_libres": 6,
    "chambres_sale": 2,
    "revenus_today": "8500.00",
    "revenus_month": "125000.00",
    "revenus_year": "780000.00",
    "locations_today": 3,
    "locations_month": 45,
    "locations_year": 234,
    "taux_occupation_today": "50.00",
    "taux_occupation_month": "78.50",
    "taux_occupation_year": "65.20",
    "date_derniere_mise_a_jour": "2025-06-14T15:30:00Z"
}
```

---

## 💻 Intégration Frontend

### Code JavaScript Universel

```javascript
// Une seule fonction pour tous les rôles
async function fetchKPIs(period = null) {
    const url = period ? `/reports/kpi/?period=${period}` : '/reports/kpi/';
    
    try {
        const response = await fetch(url, {
            headers: {
                'Authorization': 'Bearer ' + getJWTToken(),
                'Content-Type': 'application/json'
            }
        });
        
        const data = await response.json();
        
        // L'API s'adapte automatiquement selon le rôle
        if (data.user_role === 'admin') {
            displayAdminKPIs(data);
        } else if (data.user_role === 'gerant') {
            displayGerantKPIs(data);
        }
        
        return data;
    } catch (error) {
        console.error('Erreur lors du chargement des KPIs:', error);
    }
}

// Fonction pour afficher les KPIs Admin
function displayAdminKPIs(data) {
    document.getElementById('revenu-total').textContent = data.revenu_total;
    document.getElementById('taux-occupation').textContent = data.taux_occupation + '%';
    document.getElementById('revpar').textContent = data.revpar;
    document.getElementById('evolution-revenu').textContent = data.evolution_revenu + '%';
    // ... autres métriques
}

// Fonction pour afficher les KPIs Gérant
function displayGerantKPIs(data) {
    document.getElementById('revenus-jour').textContent = data.revenus_jour;
    document.getElementById('locations-actives').textContent = data.locations_actives;
    document.getElementById('entrees-prevues').textContent = data.entrees_prevues;
    document.getElementById('sorties-prevues').textContent = data.sorties_prevues;
    
    // Afficher les détails
    displayEntreesDetails(data.entrees_details);
    displaySortiesDetails(data.sorties_details);
}
```

### Utilisation avec Différentes Périodes (Admin)

```javascript
// Changer la période d'analyse
document.getElementById('period-selector').addEventListener('change', function(e) {
    fetchKPIs(e.target.value);
});

// Actualisation automatique toutes les 5 minutes
setInterval(() => {
    fetchKPIs();
}, 5 * 60 * 1000);
```

---

## 📊 Périodes de Filtrage (Admin uniquement)

| Période | Description | Calcul |
|---------|-------------|--------|
| `today` | Aujourd'hui | 00:00:00 à 23:59:59 du jour actuel |
| `week` | Cette semaine | Du lundi au dimanche de la semaine actuelle |
| `month` | Ce mois | Du 1er au dernier jour du mois actuel |
| `quarter` | Ce trimestre | 3 mois (Q1: Jan-Mar, Q2: Apr-Jun, etc.) |
| `semester` | Ce semestre | 6 mois (S1: Jan-Jun, S2: Jul-Dec) |
| `year` | Cette année | Du 1er janvier au 31 décembre |

---

## 🚨 Codes d'Erreur

| Code | Description | Action |
|------|-------------|--------|
| `200` | Succès | Données retournées selon le rôle |
| `401` | Non authentifié | Vérifier le token JWT |
| `403` | Accès refusé | Vérifier les permissions utilisateur |
| `400` | Paramètres invalides | Vérifier la période demandée (admin) |
| `500` | Erreur serveur | Contacter l'administrateur |

---

## ✨ Avantages de l'API Unifiée

1. **Simplicité** : Une seule URL à retenir (`/reports/kpi/`)
2. **Intelligence** : S'adapte automatiquement selon le rôle
3. **Maintenance** : Code centralisé, plus facile à maintenir
4. **Évolutivité** : Facile d'ajouter de nouveaux rôles
5. **Performance** : Requêtes optimisées selon le besoin

---

## 📝 Notes Techniques

- **Détection du rôle** : Automatique via les groupes Django
- **Timezone** : Toutes les dates utilisent UTC
- **Devise** : Montants en francs CFA
- **Précision** : Taux et pourcentages avec 2 décimales
- **Cache** : Recommandé côté client (5-10 minutes)
- **Sécurité** : Permissions vérifiées à chaque requête 