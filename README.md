# SPOTIFREE-
Création d'une interface utilisateur (.cli lignes de commande)
Création d'une page connexion : 2 choix : création d'un compte (champs) ou connexion (login, pwd) ==>connexion BDD
Création du menu : 1/chercher une musique  2/playlist  3/spotifriends

0/Préalable
- *création des BDD (table : playlist musique, user/admin, friends)
- télécharger la musique sur youtube

1/cherche une musique:
- recherche avec mots clés
- affichage liste de résultats chansons
- choix à faire : menu : 
  a. téléchargement musique vers répertoire personnel, lancement VLC (ffmpeg)
  b. ajouter à une playlist
    - afficher la liste des playlists
    - option si pas de playlists: message d'erreur et renvoie au menu précédent (choix menu)
  

2/playlist
- afficher la liste des playlists
sous-menu :
  - ajouter et supprimer une playlist
  - lecture d'une playlist (option: aléatoire...)
  
3/Spotifriends
- afficher la liste des amis
- ajouter ou supprimer des amis
- envoyer des messages à ses amis
- partage playlists aux amis


*Création d'une BDD: 
  - table user : id (pri), nom_user, pwd, liste_amis
  - table musique : id (pri), nom_musique, nom_ariste, album, chemin_fichier, annee_sortie
  - table musiques_playlist : id (pri), nom_playlist, id_user (foreign), id_musique (foreign), authorized_users 
 

requêtes SQL (connexion client, ajout/supp d'une playlist, ajout user, ajout user dans la playlist)

serveur ftp
stocker les musiques 

communication
ssh (script), (python socket (securisé?))

communication server/bdd
corescript (classe BDD)
