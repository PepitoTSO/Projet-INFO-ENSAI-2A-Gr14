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

## Paquets requis
Installez les paquets requis avec les commandes bash suivantes :

```bash
pip install -r requirements.txt     # installe tous les paquets listés dans le fichier
pip list                            # pour lister tous les paquets installés

