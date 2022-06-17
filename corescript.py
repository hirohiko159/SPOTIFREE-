import sys
from unittest import result
from bdd import Bdd

# Fonction d'authentification
def authentification(bdd, username, password):
    userAuthentifie = bdd.verificationUtilisateur(username, password)
    return userAuthentifie

# Recherche de la liste des musiques corresppondant au mot-clef
def rechercheMusique(bdd, mot_clef):
    resultatRecherche = bdd.resultatRechercheMusiques(mot_clef)
    return resultatRecherche

# Recherche des playlists appartenant à l'utilisateur
def recherchePlaylists(bdd, nom_user):
    resultatRecherche = bdd.resultatListePlaylists(nom_user)
    split = resultatRecherche.split("\n")
    liste_playlist=[]
    for i in range(0,len(split)-1):
        liste_playlist.append(split[i].split("|")[0])
    return liste_playlist

# Récupère les musiques de la playlist de l'utilisateur
def recupererMusiquesDepuisPlaylist(bdd, nom_user):
    resultatRecherche = bdd.recupereMusiquesDepuisPlaylist(nom_user)
    return resultatRecherche

# Ajoute une musique à la playlist choisie par l'utilisateur
def ajouterMusiqueAPlaylist(bdd, nom_user, nom_playlist, nom_musique):
    id_musique=bdd.recupererIdMusiqueDepuisNom(nom_musique)
    id_user=bdd.recupererIdUserDepuisNom(nom_user)
    bdd.ajouterMusiqueAPlaylist(nom_playlist,id_user,id_musique)

# Le premier paramètre passé à corescript depuis le client en SSH permet d'identifier l'action à réaliser.
# L'authentification, la recherche de musiques par mot-clef et la recherche des playlists de l'utilisateur fonctionnent.
# L'ajout de musique à la playlist ne fonctionne pas (retourne un index out of range),
# alors qu'elle fonctionne lorsque appelée depuis le fichier bdd.py (voir commentaires dans le bdd.py)
# Le téléchargement n'a pas été développé.
def main():
    bdd = Bdd()
    # Évaluation du premier argument pour déterminer l'action à réaliser, puis vérification que les paramètres suivants nécessaires ne sont pas vide.
    if sys.argv[1] == "authentification":
        if sys.argv[2] != "" and sys.argv[3] != "":
            if authentification(bdd,sys.argv[2], sys.argv[3]):
                print("0")
            else:
                print("1")
    elif sys.argv[1] == "recherche_musique":
        if sys.argv[2] != "":
            print (rechercheMusique(bdd, sys.argv[2]))
    elif sys.argv[1] == "telechargement":
        #TODO
        print("Erreur")
    elif sys.argv[1] == "recherche_liste_playlists":
        if sys.argv[2] != "":
            print(*recherchePlaylists(bdd, sys.argv[2]), sep="|")
    elif sys.argv[1] == "ajouter_musique_a_playlist":
        if sys.argv[2] != "" and sys.argv[3] != "" and sys.argv[4] != "":
            ajouterMusiqueAPlaylist(bdd, sys.argv[2], sys.argv[3], sys.argv[4])
    bdd.closeBdd()


main()
