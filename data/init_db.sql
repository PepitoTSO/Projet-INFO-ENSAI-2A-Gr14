DROP SCHEMA IF EXISTS bdd CASCADE;
CREATE SCHEMA bdd;

--------------------------------------------------------------
-- Les utilisateurs
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.utilisateur CASCADE ;
CREATE TABLE bdd.utilisateur (
    id_utilisateur integer PRIMARY KEY,
    pseudo varchar UNIQUE NOT NULL,
    mdp_hash varchar NOT NULL,
    date_creation date NOT NULL,
    date_derniere_co date NOT NULL
);

--------------------------------------------------------------
-- Les playlists
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.playlist;

CREATE TABLE bdd.playlist (
    id_playlist integer PRIMARY KEY,
    id_utilisateur integer FOREIGN KEY,
    nom varchar NOT NULL
);

--------------------------------------------------------------
-- Les sons
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.son CASCADE;

CREATE TABLE bdd.son (
    id_playlist integer PRIMARY KEY,
    tags varchar,
    path_stockage varchar NOT NULL
);
