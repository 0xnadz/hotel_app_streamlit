# 🏨 PROJET INTERFACE HÔTEL - BASE DE DONNÉES + STREAMLIT

CE PROJET EST RÉALISÉ DANS LE CADRE DU MODULE **BASES DE DONNÉES RELATIONNELLES**.

## 🎯 OBJECTIF DU PROJET

DÉVELOPPER UNE APPLICATION DE GESTION D’UN HÔTEL AVEC :
- UNE BASE DE DONNÉES RELATIONNELLE (`SQLITE`)
- UNE INTERFACE UTILISATEUR EN PYTHON AVEC **STREAMLIT**

L’APPLICATION PERMET DE :
- VOIR LES CLIENTS ET RÉSERVATIONS
- AJOUTER UN CLIENT OU UNE RÉSERVATION
- AFFICHER LES CHAMBRES DISPONIBLES ENTRE DEUX DATES


## 📁 CONTENU DU PROJET

| FICHIER         | DESCRIPTION                                                   |
|-----------------|---------------------------------------------------------------|
| `create_db.py`  | SCRIPT PYTHON POUR CRÉER LA BASE `hotel.db` AVEC LES TABLES ET LES DONNÉES |
| `hotel.db`      | FICHIER SQLITE CONTENANT LES DONNÉES DE L’HÔTEL               |
| `app.py`        | INTERFACE STREAMLIT COMPLÈTE                                   |
| `README.md`     | CE FICHIER : RÉSUMÉ DU PROJET ET GUIDE D’UTILISATION          |


## 🚀 LANCER LE PROJET LOCALEMENT

### 1. INSTALLER LES DÉPENDANCES

```bash
pip install streamlit pandas

###2. LANCER L’APPLICATION

```bash
streamlit run app.py
💡 ASSURE-TOI D’AVOIR LE FICHIER hotel.db DANS LE MÊME DOSSIER QUE app.py.

---

## 🔍 FONCTIONNALITÉS DE L’INTERFACE

- 🧾 Voir la liste des clients  
- 📆 Voir les réservations  
- 🔍 Rechercher les chambres disponibles entre deux dates  
- ➕ Ajouter un nouveau client  
- 📋 Ajouter une réservation  

---

## 🧠 TECHNOLOGIES UTILISÉES

- Python 3.x  
- SQLite  
- Streamlit  
- pandas  

---

## 👩‍💻 RÉALISÉ PAR

Nada  
Étudiante en informatique, passionnée par la cybersécurité 💻🔐