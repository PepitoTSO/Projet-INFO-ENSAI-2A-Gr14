# Projet-info   /The DM's Sound Buddy/
Le projet info du groupe 14
# **DM's Sound Buddy**

## **Présentation du projet**

Le **DM's Sound Buddy** est une application conçue pour les maîtres de jeu de rôle et les conteurs souhaitant enrichir leurs parties avec des ambiances sonores personnalisées. L'objectif principal de l'application est de faciliter la gestion d'effets sonores, permettant aux utilisateurs de rechercher, télécharger et organiser des sons en playlists, puis de les jouer facilement pendant une session.

L'application repose sur l'API [Freesound](https://freesound.org/apiv2/), offrant ainsi une grande variété d'effets sonores que les utilisateurs peuvent rechercher par mots-clés. L'outil permet non seulement de créer des playlists personnalisées, mais aussi de copier celles d'autres utilisateurs pour les adapter à ses propres besoins.

## **Fonctionnalités principales**

- **Gestion des utilisateurs et des playlists**
  Les utilisateurs peuvent créer et gérer des comptes personnels. Ils ont la possibilité de constituer des playlists d'effets sonores qu'ils pourront sauvegarder et réutiliser.

- **Recherche et téléchargement de sons**
  L'application propose une interface de recherche connectée à l'API Freesound, permettant de trouver des effets sonores spécifiques. Les utilisateurs peuvent ensuite les télécharger sans duplicatas, et les intégrer dans leurs playlists.

- **Lecture des sons pendant une session**
  En un clic, les sons de la playlist sélectionnée peuvent être joués lors d'une partie de jeu de rôle, facilitant ainsi la création d'une ambiance sonore immersive.

- **Consultation et duplication de playlists**
  Les utilisateurs ont accès aux playlists publiques d'autres membres, qu'ils peuvent consulter et dupliquer pour les adapter à leurs besoins personnels.

## **Fonctionnalités optionnelles**

- **Recherche avancée** : Basée sur des critères plus complexes comme la similarité avec d'autres sons, les mots-clés associés, les commentaires de la communauté Freesound, ou encore la popularité des sons.
- **Lecture aléatoire d'effets sonores** : Une fonctionnalité permettant de jouer certains sons à intervalles aléatoires, utile pour des bruits d'ambiance comme ceux de la nature.
- **Lecture en boucle** : Les utilisateurs peuvent configurer certains sons pour qu'ils se répètent en boucle (ex : bruit de fond, pluie).
- **Lecture simultanée** : Il est également possible de jouer plusieurs sons en même temps pour une expérience sonore plus riche et plus complexe.

## **Guide d'utilisation**

Après avoir téléchargé les packages nécessaire, vous pouvez lancer le fichier se trouvant sous src/__main__.py. Vous voilà dans l'application, pour votre première utilisation, créez un compte puis connectez-vous. Vous pouvez désormais créer des playlist, rechercher des sons et pleins d'autres fonctionnalités.

Il vous manque une fonctionnalité? Pas de soucis, la licence de ce projet vous permet de copier le code et de l'adapter selon vos besoins. Et mieux que ça, nous avons voulu une application décentralisée accessible à tous et facilement modifiable.


**Welcome to the user guide for our application, The DM’s Sound Buddy.**
  First, you need to sign up using a username and a password that must be at least 8 characters long. Once your registration is validated, you can log in and directly enter the application. You also have the option to log out from anywhere within the app. Moreover, you can find information about the app before logging in and in the main menu, in case you need a reminder.

You are now at the main menu. From here, you can:
- **Search for a sound**
- **Manage the sounds in your library**
- **Listen to and manage your playlists**
- **Access to the sound player**

  First, to search for a sound, go to the "Search for a sound" menu and type in the type of sound you want, whether it's a door creak, a rain recording, or loud laughter. The app will then provide you with a list of sounds that match your search, and you can choose to listen to one of the sounds from the list. The sound you listen to will be downloaded and can be found in your "Available Sounds." If you don't find the sound you’re looking for, you can try the "Recommendations," which will give you a new list of sounds based on your search. You can also add the sound to a (pre-existing) playlist right after listening to it if you wish.

  You have access to all the sounds you've listened to in the "Available Sounds" menu. You can view all of them if you’re looking for a sound you've already downloaded. Of course, you can also listen to any of your sounds after selecting one. You’ll then have the option to pause it, loop it, or play it for a set duration using the "Play for X seconds" option. You can also listen to another sound while the first one is still playing or even randomly play a sound while listening to another. This is all designed to offer you the most comprehensive listening experience possible.

  With all these sounds, you can create and listen to playlists. This happens in the "My Playlists" menu, where you have several options. You can create a playlist (and delete it), then add sounds to it, specifying where you want each sound to be placed in the playlist. Afterward, you can play a playlist by going to the "Play a Playlist" menu, where you can choose the playlist you want to listen to and start it from the beginning. You can also play a single sound from the playlist, loop a sound, or play a sound randomly, just like in the "Available Sounds" menu.

You can also modify your playlists in the "Edit a Playlist" menu. The options here include:
- **Renaming a playlist** by typing the new name you want to give it
- **Adding or removing a sound from a playlist**, specifying its position in the playlist when you add it
- **Changing the order of a sound in a playlist** to adjust the playlist's composition
There's also an option to copy a playlist. You will have access to all playlists created by other users of the app. Using this option, you can search for a playlist that might interest you, copy it to your own collection, and listen to it or modify it as you like.

  Finally, in the main menu, there’s the "Player" menu, which automatically appears when you play one of your sounds or playlists. It allows you to pause (or not) a sound and skip to the next sound in a playlist. If you’re playing multiple sounds simultaneously, you can stop all of them except for the playlist currently playing. And you can continue browsing your sounds or playlists even while a sound is playing by returning to the "Available Sounds" or "My Playlists" menus.



## Paquets requis
Installez les paquets requis avec les commandes bash suivantes :

```bash
pip install -r requirements.txt     # installe tous les paquets listés dans le fichier
pip list                            # pour lister tous les paquets installés
