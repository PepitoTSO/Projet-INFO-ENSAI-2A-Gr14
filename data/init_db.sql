DROP SCHEMA IF EXISTS bdd CASCADE;
CREATE SCHEMA bdd;

--------------------------------------------------------------
-- Les utilisateurs
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.utilisateurs CASCADE;
CREATE TABLE bdd.utilisateurs (
    pseudo VARCHAR UNIQUE NOT NULL,
    mdp_hache VARCHAR NOT NULL
);

--------------------------------------------------------------
-- Les playlists
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.playlist;

CREATE TABLE bdd.playlist (
    id_playlist SERIAL PRIMARY KEY,
    id_utilisateur VARCHAR REFERENCES bdd.utilisateurs(id_utilisateur),
    nom_playlist VARCHAR NOT NULL
);

--------------------------------------------------------------
-- Les sons
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.son CASCADE;

CREATE TABLE bdd.son (
    id_son SERIAL PRIMARY KEY,
    nom_son VARCHAR,
    tags VARCHAR,
    path_stockage VARCHAR NOT NULL
);

--------------------------------------------------------------
-- La table de jointure playlist-son
--------------------------------------------------------------

DROP TABLE IF EXISTS bdd.playlist_son_join CASCADE;

CREATE TABLE bdd.playlist_son_join (
    id_son INTEGER REFERENCES bdd.son(id_son),
    id_playlist INTEGER REFERENCES bdd.playlist(id_playlist),
    ordre_son_playlist INTEGER,
    PRIMARY KEY (id_son, id_playlist)
);
