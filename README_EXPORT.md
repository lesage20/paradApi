# Export des données SQLite vers PostgreSQL

Ce script permet d'exporter uniquement les **données** (pas la structure) de votre base SQLite vers PostgreSQL. Ceci est idéal pour Django car vous pouvez faire `migrate` pour créer la structure, puis insérer vos données existantes.

## Fichiers générés

- `export_data_to_postgresql.py` : Script principal d'export
- `data_export_postgresql.sql` : Fichier SQL avec les données exportées
- `requirements_export.txt` : Dépendances nécessaires

## Installation des dépendances

```bash
pip install -r requirements_export.txt
```

## Utilisation

### Option 1 : Générer le fichier SQL (recommandée)

```bash
python export_data_to_postgresql.py
# Choisir l'option 1
```

Cela génère le fichier `data_export_postgresql.sql` que vous pouvez ensuite importer dans PostgreSQL.

### Option 2 : Insertion directe dans PostgreSQL

```bash
python export_data_to_postgresql.py
# Choisir l'option 2 et fournir les paramètres de connexion
```

## Processus recommandé pour migrer vers PostgreSQL

1. **Configurer PostgreSQL** dans votre `settings.py` Django
2. **Créer la base de données** PostgreSQL vide
3. **Faire les migrations** Django :
   ```bash
   python manage.py migrate
   ```
4. **Exporter les données** SQLite :
   ```bash
   python export_data_to_postgresql.py
   ```
5. **Importer les données** dans PostgreSQL :
   ```bash
   psql -h localhost -U votre_utilisateur -d votre_base < data_export_postgresql.sql
   ```

## Tables exclues automatiquement

Le script ignore automatiquement les tables système Django qui seront recréées par `migrate` :

- `django_migrations`
- `django_content_type`
- `auth_permission`
- `django_session`
- `django_admin_log`
- `django_site`
- `authtoken_token`
- `account_emailconfirmation`

## Tables exportées

- Toutes vos tables métier (hotel_*, userAccount_profil, etc.)
- Tables d'authentification (auth_user, auth_group, etc.)
- Tables de social auth et email (si elles contiennent des données)

## Notes importantes

- Le script utilise `TRUNCATE TABLE ... RESTART IDENTITY CASCADE` pour vider les tables avant insertion
- Les données sont correctement échappées pour PostgreSQL
- Les types de données sont automatiquement convertis
- La table `sqlite_sequence` est exportée pour maintenir les séquences des clés primaires

## En cas de problème

Si vous rencontrez des erreurs lors de l'import, vérifiez :
1. Que Django a bien créé toutes les tables avec `migrate`
2. Que les contraintes de clés étrangères sont respectées
3. Que l'encodage UTF-8 est bien pris en compte 