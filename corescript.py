import sys
from bdd import Bdd

def authentification(username, password):
    bdd = Bdd()
    userAuthentifie = bdd.verificationUtilisateur(username, password)
    bdd.closeBdd()
    return userAuthentifie

def rechercheMusique(mot_clef):
    bdd = Bdd()
    resultatRecherche = bdd.resultatRechercheMusiques(mot_clef)
    bdd.closeBdd()
    return resultatRecherche

def recherchePlaylists(nom_user):
    bdd = Bdd()
    resultatRecherche = bdd.resultatListePlaylists(nom_user)
    bdd.closeBdd()
    return resultatRecherche.split("|")[0]

def recupererMusiquesDepuisPlaylist(nom_user):
    bdd = Bdd()
    resultatRecherche = bdd.recupereMusiquesDepuisPlaylist(nom_user)
    bdd.closeBdd()
    return resultatRecherche

def ajouterMusiqueAPlaylist(nom_user, nom_musique, nom_playlist):
    bdd = Bdd()
    id_musique=bdd.recupererIdMusiqueDepuisNom(nom_musique)
    id_user=bdd.recupererIdUserDepuisNom(nom_user)
    bdd.ajouterMusiqueAPlaylist(nom_playlist,id_user,id_musique)
    bdd.closeBdd()
    
def main():
    if sys.argv[1] == "authentification":
        if sys.argv[2] != "" and sys.argv[3] != "":
            return authentification(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "recherche_musique":
        if sys.argv[2] != "":
            return rechercheMusique(sys.argv[2])
    elif sys.argv[1] == "telechargement":
        #TODO
        return "Erreur"
    elif sys.argv[1] == "recherche_liste_playlists":
        if sys.argv[2] != "":
            return recherchePlaylists(sys.argv[2])
    elif sys.argv[1] == "ajouter_musique_a_playlist":
        if sys.argv[2] != "" and sys.argv[3] != "" and sys.argv[4] != "":
            return ajouterMusiqueAPlaylist(sys.argv[2], sys.argv[4], sys.argv[3])

print(main())
