import streamlit as st
import sqlite3
import pandas as pd

# Connexion à la base de données SQLite
def get_connection():
    conn = sqlite3.connect("hotel.db")
    return conn

st.title("🏨 Interface de gestion d'hôtel")

# Menu
menu = ["Voir les clients", "Voir les réservations", "Voir les chambres disponibles", "Ajouter un client", "Ajouter une réservation"]
choix = st.sidebar.selectbox("Navigation", menu)

conn = get_connection()
cursor = conn.cursor()

if choix == "Voir les clients":
    st.subheader("Liste des clients")
    df = pd.read_sql("SELECT * FROM CLIENT", conn)
    st.dataframe(df)

elif choix == "Voir les réservations":
    st.subheader("Liste des réservations")
    df = pd.read_sql("SELECT * FROM RESERVATION", conn)
    st.dataframe(df)

elif choix == "Voir les chambres disponibles":
    st.subheader("Chambres disponibles entre deux dates")
    date_debut = st.date_input("Date de début")
    date_fin = st.date_input("Date de fin")

    if date_debut and date_fin:
        requete = f'''
        SELECT * FROM CHAMBRE
        WHERE NumChambre NOT IN (
            SELECT NumChambre
            FROM RESERVATION
            WHERE '{date_debut}' < DateFin AND '{date_fin}' > DateDebut
        )
        '''
        df = pd.read_sql(requete, conn)
        st.dataframe(df)

elif choix == "Ajouter un client":
    st.subheader("Ajouter un nouveau client")
    with st.form("form_client"):
        num = st.number_input("NumClient", min_value=1)
        adresse = st.text_input("Adresse")
        ville = st.text_input("Ville")
        cp = st.number_input("Code Postal", min_value=0)
        email = st.text_input("Email")
        tel = st.text_input("Téléphone")
        nom = st.text_input("Nom Complet")
        submitted = st.form_submit_button("Ajouter")
        if submitted:
            cursor.execute("INSERT INTO CLIENT VALUES (?, ?, ?, ?, ?, ?, ?)", (num, adresse, ville, cp, email, tel, nom))
            conn.commit()
            st.success("Client ajouté avec succès !")

elif choix == "Ajouter une réservation":
    st.subheader("Ajouter une réservation")
    with st.form("form_resa"):
        num_res = st.number_input("NumRes", min_value=1)
        debut = st.date_input("Date Début")
        fin = st.date_input("Date Fin")
        client = st.number_input("NumClient", min_value=1)
        submitted = st.form_submit_button("Réserver")
        if submitted:
            cursor.execute("INSERT INTO RESERVATION VALUES (?, ?, ?, ?)", (num_res, debut, fin, client))
            conn.commit()
            st.success("Réservation ajoutée avec succès !")

conn.close()
