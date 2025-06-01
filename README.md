# 🏨 Projet Interface Hôtel - Base de Données + Streamlit

Ce projet est réalisé dans le cadre du module **Bases de Données Relationnelles**.

## 🎯 Objectif du projet

Développer une application de gestion d’un hôtel avec :
- Une base de données relationnelle (`SQLite`)
- Une interface utilisateur en Python avec **Streamlit**

L’application permet de :
- Voir les clients et réservations
- Ajouter un client ou une réservation
- Afficher les chambres disponibles entre deux dates


## 📁 Contenu du projet

| Fichier         | Description                                                   |
|-----------------|---------------------------------------------------------------|
| `create_db.py`  | Script Python pour créer la base `hotel.db` avec les tables et les données |
| `hotel.db`      | Fichier SQLite contenant les données de l’hôtel               |
| `app.py`        | Interface Streamlit complète                                   |
| `requirements.txt` | Dépendances Python nécessaires (`streamlit`, `pandas`)     |
| `README.md`     | Ce fichier : résumé du projet et guide d’utilisation          |


## 🚀 Lancer le projet localement

### 1. Installer les dépendances

```bash
pip install -r requirements.txt

### 2. Lancer l’application
streamlit run app.py
💡 Assure-toi d’avoir le fichier hotel.db dans le même dossier que app.py.


##🔍 Fonctionnalités de l’interface

🧾 Voir la liste des clients

📆 Voir les réservations

🔍 Rechercher les chambres disponibles entre deux dates

➕ Ajouter un nouveau client

📋 Ajouter une réservation


## Technologies utilisées

Python 3.x

SQLite (base de données légère)

Streamlit (interface web)

pandas (pour l’affichage des tableaux)

## 👩‍💻 Réalisé par
Nada
Étudiante en informatique, passionnée par la cybersécurité et les projets pratiques 💻🔐