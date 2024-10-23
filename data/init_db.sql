DROP SCHEMA IF EXISTS bdd CASCADE;
CREATE SCHEMA bdd;

--------------------------------------------------------------
-- Les utilisateurs
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.utilisateur CASCADE ;
CREATE TABLE bdd.utilisateur (
    id_utilisateur INT AUTO_INCREMENT PRIMARY KEY,
    pseudo varchar UNIQUE NOT NULL,
    mdp varchar NOT NULL
);

--------------------------------------------------------------
-- Les playlists
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.playlist;

CREATE TABLE bdd.playlist (
    id_playlist INT AUTO_INCREMENT PRIMARY KEY,
    id_utilisateur integer FOREIGN KEY,
    nom_playlist varchar NOT NULL
);

--------------------------------------------------------------
-- Les sons
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.son CASCADE;

CREATE TABLE bdd.son (
    id_son integer PRIMARY KEY,
    nom_son varchar,
    tags varchar,
    path_stockage varchar NOT NULL
);

--------------------------------------------------------------
-- La table de jointure playlist-son
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.playlist_son_join CASCADE;

CREATE TABLE bdd.playlist_son_join (
    id_son integer FOREIGN KEY,
    id_playlist integer FOREIGN KEY,
    ordre_son_playlist integer
);