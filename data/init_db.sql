DROP SCHEMA IF EXISTS bdd CASCADE;
CREATE SCHEMA bdd;

--------------------------------------------------------------
-- Le compte
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.compte CASCADE ;
CREATE TABLE bdd.compte (
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
-- La table de jointure entre playlist et son
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.playlist_son_join CASCADE ;

CREATE TABLE bdd.playlist_son_join (
    id_playlist integer FOREIGN KEY,
    id_son integer UNIQUE NOT NULL,
    ordre_son_in_plist integer NOT NULL
);


--------------------------------------------------------------
-- Les sons
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.son CASCADE;

CREATE TABLE bdd.son (
    id_playlist integer PRIMARY KEY,
    path_stockage varchar NOT NULL
);

