DROP SCHEMA IF EXISTS bddtest CASCADE;
CREATE SCHEMA bddtest;

--------------------------------------------------------------
-- Les utilisateurs
--------------------------------------------------------------

DROP TABLE IF EXISTS bddtest.utilisateurs CASCADE;
CREATE TABLE bddtest.utilisateurs (
    pseudo VARCHAR UNIQUE NOT NULL,
    mdp_hache VARCHAR NOT NULL
);

--------------------------------------------------------------
-- Les playlists
--------------------------------------------------------------

DROP TABLE IF EXISTS bddtest.playlist;

CREATE TABLE bddtest.playlist (
    id_playlist SERIAL PRIMARY KEY,
    pseudo VARCHAR REFERENCES bddtest.utilisateurs(pseudo),
    nom_playlist VARCHAR NOT NULL
);

--------------------------------------------------------------
-- Les sons
--------------------------------------------------------------

DROP TABLE IF EXISTS bddtest.son CASCADE;

CREATE TABLE bddtest.son (
    id_son SERIAL PRIMARY KEY,
    nom_son VARCHAR,
    tags VARCHAR,
    path_stockage VARCHAR NOT NULL
);

--------------------------------------------------------------
-- La table de jointure playlist-son
--------------------------------------------------------------

DROP TABLE IF EXISTS bddtest.playlist_son_join CASCADE;

CREATE TABLE bddtest.playlist_son_join (
    id_son INTEGER REFERENCES bddtest.son(id_son),
    id_playlist INTEGER REFERENCES bddtest.playlist(id_playlist),
    ordre_son_playlist INTEGER,
    PRIMARY KEY (id_son, id_playlist)
);
