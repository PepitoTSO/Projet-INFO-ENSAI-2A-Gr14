--------------------------------------------------------------
-- Remplissage de la base de données
--------------------------------------------------------------

-- Insertion des utilisateurs
INSERT INTO bdd.utilisateurs (pseudo, mdp_hache) VALUES
('Barbar', 'Gpriforce20'),
('MJ', 'Campagne2024'),
('Bard', 'Bard4life');

-- Insertion des playlists
INSERT INTO bdd.playlist (pseudo, nom_playlist) VALUES
('Barbar', 'Bagarre'),
('Barbar', 'Cri'),
('MJ', 'Histoire'),
('MJ', 'Combat'),
('MJ', 'Mer'),
('Bard', 'Sort_perso');

-- Insertion des sons  VOIR RESET
--INSERT INTO bdd.son (id_son, nom_son, tags, path_stockage) VALUES
--('1','Song 1', 'chill, relax', '/path/to/song1'),
--('2','Song 2', 'workout, gym', '/path/to/song2'),
--('3','Song 3', 'top hits, popular', '/path/to/song3'),
--('4','Song 4', 'indie, alternative', '/path/to/song4'),
--('5','Song 5', 'classical, orchestra', '/path/to/song5'),
--('6','Song 6', 'relax, chill', '/path/to/song6'),
--('7','Song 7', 'gym, workout', '/path/to/song7'),
--('8','Song 8', 'popular, top hits', '/path/to/song8'),
--('9','Song 9', 'morning, upbeat', '/path/to/song9'),
--('10','Song 10', 'evening, calm', '/path/to/song10'),
--('11','Song 11', 'road trip, fun', '/path/to/song11'),
--('12','Song 12', 'jazz, smooth', '/path/to/song12');

-- Insertion des associations playlist-son
--INSERT INTO bdd.playlist_son_join (id_son, id_playlist, ordre_son_playlist) VALUES
--(1, 1, 1),  -- Song 1 in Chill Vibes
--(6, 1, 2),  -- Song 6 in Chill Vibes
--(9, 3, 1),  -- Song 9 in Morning Routine
--(2, 2, 1),  -- Song 2 in Workout Mix
--(7, 2, 2),  -- Song 7 in Workout Mix
--(3, 4, 1),  -- Song 3 in Top Hits
--(8, 4, 2),  -- Song 8 in Top Hits
--(10, 5, 1), -- Song 10 in Evening Relax
--(4, 6, 1),  -- Song 4 in Indie Gems
--(11, 7, 1), -- Song 11 in Road Trip
--(5, 8, 1),  -- Song 5 in Classical Essentials
--(12, 9, 1), -- Song 12 in Jazz Collection
--(3, 6, 2),  -- Recoupement: Song 3 in Indie Gems
--(1, 5, 2),  -- Recoupement: Song 1 in Evening Relax
--(2, 7, 2),  -- Recoupement: Song 2 in Road Trip
--(4, 7, 3),  -- Recoupement: Song 4 in Road Trip
--(5, 9, 2),  -- Recoupement: Song 5 in Jazz Collection
--(6, 3, 2),  -- Recoupement: Song 6 in Morning Routine
--(8, 1, 3);  -- Recoupement: Song 8 in Chill Vibes
