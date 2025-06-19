import sqlite3
import psycopg2
from psycopg2.extras import execute_values
import os
from datetime import datetime

def export_data_from_sqlite():
    """Exporte les données de SQLite vers des fichiers SQL ou directement vers PostgreSQL"""
    
    # Connexion à la base SQLite
    sqlite_conn = sqlite3.connect('db.sqlite3')
    sqlite_cursor = sqlite_conn.cursor()
    
    # Tables à exclure (tables système Django qui seront recréées par migrate)
    excluded_tables = {
        'django_migrations',
        'django_content_type', 
        'auth_permission',
        'django_session',
        'django_admin_log',
        'django_site',
        'authtoken_token',
        'account_emailconfirmation'
    }
    
    # Récupérer toutes les tables
    sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = sqlite_cursor.fetchall()
    
    # Générer les instructions INSERT
    sql_statements = []
    sql_statements.append("-- Export des données de SQLite vers PostgreSQL")
    sql_statements.append(f"-- Généré le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    sql_statements.append("")
    
    for table in tables:
        table_name = table[0]
        
        # Ignorer les tables système
        if table_name in excluded_tables:
            print(f"Ignorer la table système: {table_name}")
            continue
            
        print(f"Exportation de la table: {table_name}")
        
        # Récupérer les données de la table
        sqlite_cursor.execute(f"SELECT * FROM {table_name}")
        rows = sqlite_cursor.fetchall()
        
        if not rows:
            print(f"  -> Table {table_name} vide")
            continue
            
        # Récupérer les noms des colonnes
        sqlite_cursor.execute(f"PRAGMA table_info({table_name})")
        columns_info = sqlite_cursor.fetchall()
        column_names = [col[1] for col in columns_info]
        
        sql_statements.append(f"-- Données pour la table {table_name}")
        sql_statements.append(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE;")
        
        # Générer les instructions INSERT
        for row in rows:
            # Préparer les valeurs en gérant les types de données
            values = []
            for value in row:
                if value is None:
                    values.append('NULL')
                elif isinstance(value, str):
                    # Échapper les apostrophes
                    escaped_value = value.replace("'", "''")
                    values.append(f"'{escaped_value}'")
                elif isinstance(value, (int, float)):
                    values.append(str(value))
                elif isinstance(value, bool):
                    values.append('TRUE' if value else 'FALSE')
                else:
                    values.append(f"'{str(value)}'")
            
            columns_str = ', '.join(column_names)
            values_str = ', '.join(values)
            
            sql_statements.append(f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});")
        
        sql_statements.append("")
        print(f"  -> {len(rows)} lignes exportées")
    
    # Écrire dans un fichier SQL
    with open('data_export_postgresql.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sql_statements))
    
    sqlite_conn.close()
    print(f"\nExport terminé ! Fichier généré: data_export_postgresql.sql")
    return 'data_export_postgresql.sql'

def insert_data_to_postgresql(host, database, username, password, port=5432):
    """Insère directement les données dans PostgreSQL"""
    try:
        # Connexion à PostgreSQL
        pg_conn = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password,
            port=port
        )
        pg_cursor = pg_conn.cursor()
        
        # Lire et exécuter les instructions SQL
        with open('data_export_postgresql.sql', 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        # Exécuter les instructions
        pg_cursor.execute(sql_content)
        pg_conn.commit()
        
        print("Données insérées avec succès dans PostgreSQL !")
        
        pg_conn.close()
        
    except Exception as e:
        print(f"Erreur lors de l'insertion dans PostgreSQL: {e}")

if __name__ == "__main__":
    print("=== Export des données SQLite vers PostgreSQL ===")
    print()
    
    # 1. Exporter les données vers un fichier SQL
    sql_file = export_data_from_sqlite()
    
    print(f"\nFichier SQL généré: {sql_file}")
    print()
    print("Options:")
    print("1. Utiliser le fichier SQL généré manuellement")
    print("2. Insérer directement dans PostgreSQL")
    
    choice = input("\nChoisir une option (1 ou 2): ").strip()
    
    if choice == "2":
        print("\nConfiguration PostgreSQL:")
        host = input("Host (par défaut: localhost): ").strip() or "localhost"
        database = input("Nom de la base: ").strip()
        username = input("Nom d'utilisateur: ").strip()
        password = input("Mot de passe: ").strip()
        port = input("Port (par défaut: 5432): ").strip() or "5432"
        
        insert_data_to_postgresql(host, database, username, password, int(port))
    else:
        print(f"\nVous pouvez maintenant utiliser le fichier {sql_file}")
        print("Pour l'exécuter dans PostgreSQL:")
        print(f"psql -h localhost -U votre_utilisateur -d votre_base < {sql_file}") 