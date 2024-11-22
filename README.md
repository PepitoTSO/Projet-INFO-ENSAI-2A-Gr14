# Projet-info   /The DM's Sound Buddy/
Le projet info du groupe 14
# **DM's Sound Buddy**

## **Project presentation**

The **DM's Sound Buddy** is an application designed for role-playing game masters and storytellers wishing to enrich their games with customised soundscapes. The main aim of the application is to facilitate the management of sound effects, allowing users to search, download and organise sounds into playlists, then play them easily during a session.

The application is based on the [Freesound] API (https://freesound.org/apiv2/), offering a wide variety of sound effects that users can search for using keywords. As well as creating custom playlists, users can copy other users' playlists and adapt them to their own needs.

## **Main features**

- **Management of users and playlists**
  Users can create and manage personal accounts. Users can create and manage personal accounts. They can create playlists of sound effects that they can save and reuse.

- **Sound search and download**
  The application offers a search interface connected to the Freesound API, enabling users to find specific sound effects. Users can then download them without duplication, and integrate them into their playlists.

- **Play sounds during a session**
  With the click of a button, sounds from the selected playlist can be played during a role-playing game session, helping to create an immersive soundscape.

- **Viewing and duplicating playlists**
  Users have access to the public playlists of other members, which they can consult and duplicate to adapt them to their personal needs.

## **Optional Features**

- **Advanced search** : Based on more complex criteria such as similarity to other sounds, related keywords, comments from the Freesound community, or popularity of sounds.
- **Shuffle sound effects** : A feature that allows certain sounds to be played at random intervals, useful for ambient sounds such as nature sounds.
- **Loop playback** : Users can set certain sounds to repeat in a loop (e.g. background noise, rain).
- **Simultaneous playback** : It is also possible to play several sounds at the same time for a richer, more complex sound experience.

## **User guide**

Once you've downloaded the necessary packages, you can launch the file found under src/__main__.py. Now you're in the application for the first time, create an account and log in. You can now create playlists, search for sounds and a whole host of other features.

Missing a feature? Don't worry, the licence for this project allows you to copy the code and adapt it to your needs. And best of all, we wanted a decentralised application that's accessible to everyone and easy to modify.


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
pip install -r requirements.txt     # installs all the packages present on the ENSAI VMs in the file, some of which are useless for our application.
pip install -r requirements2.txt    # installs all the necessary packages missing from the ENSAI VMs in the file
pip list                            # to list all installed packages
