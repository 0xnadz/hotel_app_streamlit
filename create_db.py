import sqlite3

# Connexion ou création du fichier .db
conn = sqlite3.connect("hotel.db")
cursor = conn.cursor()

# Supprimer si existant 
cursor.executescript("""
DROP TABLE IF EXISTS EVALUATION;
DROP TABLE IF EXISTS RESERVATION;
DROP TABLE IF EXISTS CHAMBRE;
DROP TABLE IF EXISTS TYPECHAMBRE;
DROP TABLE IF EXISTS PRESTATION;
DROP TABLE IF EXISTS CLIENT;
DROP TABLE IF EXISTS HOTEL;
""")

# Création des tables
cursor.executescript("""
CREATE TABLE HOTEL (
  NumHotel INTEGER PRIMARY KEY,
  Ville TEXT,
  Pays TEXT,
  CodePostal INTEGER
);

CREATE TABLE CLIENT (
  NumClient INTEGER PRIMARY KEY,
  Adresse TEXT,
  Ville TEXT,
  CodePostal INTEGER,
  Email TEXT,
  Tel TEXT,
  NomComplet TEXT
);

CREATE TABLE PRESTATION (
  NumPrestation INTEGER PRIMARY KEY,
  Prix INTEGER,
  Description TEXT
);

CREATE TABLE TYPECHAMBRE (
  NumType INTEGER PRIMARY KEY,
  NomType TEXT,
  Tarif REAL
);

CREATE TABLE CHAMBRE (
  NumChambre INTEGER PRIMARY KEY,
  Numero INTEGER,
  Etage INTEGER,
  EstOccupe BOOLEAN,
  NumType INTEGER,
  NumHotel INTEGER,
  FOREIGN KEY (NumType) REFERENCES TYPECHAMBRE(NumType),
  FOREIGN KEY (NumHotel) REFERENCES HOTEL(NumHotel)
);

CREATE TABLE RESERVATION (
  NumRes INTEGER PRIMARY KEY,
  DateDebut TEXT,
  DateFin TEXT,
  NumClient INTEGER,
  FOREIGN KEY (NumClient) REFERENCES CLIENT(NumClient)
);

CREATE TABLE EVALUATION (
  NumClient INTEGER,
  DateEval TEXT,
  Note INTEGER,
  Commentaire TEXT,
  NumHotel INTEGER,
  PRIMARY KEY (NumClient, NumHotel),
  FOREIGN KEY (NumClient) REFERENCES CLIENT(NumClient),
  FOREIGN KEY (NumHotel) REFERENCES HOTEL(NumHotel)
);
""")

# Insertion des données
cursor.executescript("""
INSERT INTO HOTEL VALUES
(1, 'Paris', 'France', 75001),
(2, 'Lyon', 'France', 69002),
(3, 'Marseille', 'France', 13005),
(4, 'Lille', 'France', 59800),
(5, 'Nice', 'France', 6000);

INSERT INTO CLIENT VALUES
(1, '12 Rue de Paris', 'Paris', 75001, 'jean.dupont@email.fr', '0612345678', 'Jean Dupont'),
(2, '5 Avenue Victor Hugo', 'Lyon', 69002, 'marie.leroy@email.fr', '0623456789', 'Marie Leroy'),
(3, '8 Boulevard Saint-Michel', 'Marseille', 13005, 'paul.moreau@email.fr', '0634567890', 'Paul Moreau'),
(4, '27 Rue Nationale', 'Lille', 59800, 'lucie.martin@email.fr', '0645678901', 'Lucie Martin'),
(5, '3 Rue des Fleurs', 'Nice', 6000, 'emma.giraud@email.fr', '0656789012', 'Emma Giraud');

INSERT INTO PRESTATION VALUES
(1, 15, 'Petit-déjeuner'),
(2, 30, 'Navette aéroport'),
(3, 0, 'Wi-Fi gratuit'),
(4, 50, 'Spa et bien-être'),
(5, 20, 'Parking sécurisé');

INSERT INTO TYPECHAMBRE VALUES
(1, 'Simple', 80),
(2, 'Double', 120);

INSERT INTO CHAMBRE VALUES
(1, 201, 2, 0, 1, 1),
(2, 502, 5, 1, 1, 2),
(3, 305, 3, 0, 2, 1),
(4, 410, 4, 0, 2, 2),
(5, 104, 1, 1, 2, 2),
(6, 202, 2, 0, 1, 1),
(7, 307, 3, 1, 1, 2),
(8, 101, 1, 0, 1, 1);

INSERT INTO RESERVATION VALUES
(1, '2025-06-15', '2025-06-18', 1),
(2, '2025-07-01', '2025-07-05', 2),
(7, '2025-11-12', '2025-11-14', 2),
(10, '2026-02-01', '2026-02-05', 2),
(3, '2025-08-10', '2025-08-14', 3),
(4, '2025-09-05', '2025-09-07', 4),
(9, '2026-01-15', '2026-01-18', 4),
(5, '2025-09-20', '2025-09-25', 5);

INSERT INTO EVALUATION VALUES
(1, '2025-06-15', 5, 'Excellent séjour, personnel très accueillant.', 1),
(2, '2025-07-01', 4, 'Chambre propre, bon rapport qualité/prix.', 2),
(3, '2025-08-10', 3, 'Séjour correct mais bruyant la nuit.', 3),
(4, '2025-09-05', 5, 'Service impeccable, je recommande.', 4),
(5, '2025-09-20', 4, 'Très bon petit-déjeuner, hôtel bien situé.', 5);
""")

# Enregistrer et fermer
conn.commit()
conn.close()

print("✅ hotel.db est prêt avec toutes les tables et données.")
