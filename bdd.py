import mariadb
import sys

class Bdd():
    def __init__(self):
        self.connection=None
        self.cursor=None
        try:
            self.connection = mariadb.connect(
            user="formation",
            password="formation",
            host="127.0.0.1",
            port=3306,
            database="SPOTIFREE"
        )
        except mariadb.Error as exception:
            print(f"Error connecting to MariaDB Platform: {exception}")
            sys.exit(1)

        self.cursor= self.connection.cursor()
    
    # Fonction d'affichage classique, mais peu utile, vu que l'affichage a souvent dû être adapté pour chaque requête
    def affichage(self, reponse):
        affichage=""
        for line in reponse:
            affichage = affichage + " | ".join(line) 
        return affichage
    
    # Vérifie l'existence de l'utilisateur et du mot de passe correspondant en bdd, retourne un booléen
    def verificationUtilisateur(self,username,password):
        sql="SELECT nom_user FROM user WHERE nom_user=? AND pwd=?;"
        self.cursor.execute(sql,(username,password))
        data=self.cursor.fetchall()  
        if data:
            return True
        return False    

    # Cherche avec un mot-clef uniquement dans ma table musique pour trouver une entrée où le nom de la musique / le nom de l'artiste / l'album correspond
    # au mot-clef, retourne ces données ainsi que le chemin du fichier sur le server
    def resultatRechercheMusiques(self, mot_clef):
        sql="SELECT DISTINCT nom_musique, nom_artiste, chemin_fichier FROM musique"
        if mot_clef:
            sql = sql + " WHERE nom_musique LIKE ? OR nom_artiste LIKE ? OR album LIKE ?;"
            mot_clef = "%" + mot_clef + "%"
            self.cursor.execute(sql,(mot_clef,mot_clef,mot_clef,))
        else:
            sql = sql + ";"
            self.cursor.execute(sql)
        data = self.cursor.fetchall()
        affichage_complet = ""
        for line in data:
            affichage_complet = affichage_complet + line[0] + "\n"
        return affichage_complet
    
    # Récupère la liste des playlists enregistrées pour l'utilisateur connecté, retourne la liste des musiques appartenant à une playlist
    # enregistrée par l'utilisateur (format "playlist|id_user|id_musique\nplaylist|id_user|id_musique"
    def resultatListePlaylists(self,nom_user):
        sql=""" 
                SELECT DISTINCT nom_playlist,id_user,id_musique
                FROM musiques_playlist 
                INNER JOIN user 
                ON user.id = musiques_playlist.id_user
                WHERE nom_user = ?; 
            """
        self.cursor.execute(sql,(nom_user,))
        data = self.cursor.fetchall()
        affichage_complet = ""
        for line in data:
            affichage_complet = affichage_complet + line[0] +  "|" + str(line[1]) + "|" + str(line[2]) + "\n"
        return affichage_complet

    # Permet de récupérer l'id de l'utilisateur en fonction de son nom
    #TODO Cette fonction fonctionne lors des tests effectués depuis le fichier bdd.py (voir fin du fichier), mais retourne un index out of range
    # lorsqu'elle est appellée depuis corescript.py
    def recupererIdUserDepuisNom(self, nom_user):
        sql="""
                SELECT id 
                FROM user
                WHERE nom_user=?;
            """
        self.cursor.execute(sql, (nom_user,))
        data = self.cursor.fetchall()
        return data[0][0]
    
    # Permet de récupérer les musiques d'une playlist depuis leur id apparaissant dans le resultat de la fonction "resultatListePlaylists".
    def recupereMusiquesDepuisPlaylist(self, nom_user):
        listeMusiques = self.resultatListePlaylists(nom_user)
        id_musiques_a_chercher=[]
        split = listeMusiques.split("\n")
        for i in range(0,len(split)- 1):
            id_musiques_a_chercher.append(split[i].split("|")[2])
        resultatRechercheMusique=[]
        for i in range(0,len(id_musiques_a_chercher)):
            sql="""
                    SELECT DISTINCT nom_musique,chemin_fichier
                    FROM musique
                    WHERE id=?;
                """
            self.cursor.execute(sql,(id_musiques_a_chercher[i],))
            data = self.cursor.fetchall()
            resultatRechercheMusique.append(data)
        return resultatRechercheMusique
    
    # Permet l'ajout d'une musique dans une playlist depuis son id
    def ajouterMusiqueAPlaylist(self,nom_playlist,id_user,id_musique):
        sql="""
                INSERT INTO musiques_playlist 
                    (nom_playlist, id_user, id_musique, authorized_users) 
                VALUE 
                    (?,?,?,NULL);
            """
        self.cursor.execute(sql,(nom_playlist,id_user,id_musique))
        self.connection.commit()
    
    # PErmet de récupérer l'id d'une musique depuis son nom
    def recupererIdMusiqueDepuisNom(self, nom_musique):
        sql="""
                SELECT id
                FROM musique
                WHERE nom_musique=?;
            """
        self.cursor.execute(sql,(nom_musique,))
        id_musique=self.cursor.fetchall()
        return id_musique[0][0]
    
    # Supprime une playlist
    def supprimerPlaylist(self,nom_playlist,id_user):
        sql="""
                DELETE FROM musiques_playlist
                WHERE (nom_playlist = ? AND id_user = ?);
            """
        self.cursor.execute(sql,(nom_playlist,id_user))
        self.connection.commit()
    
    # Permet d'ajouter un utilisateur dans la liste d'utilisateurs autorisés de la playlist de l'utilisateur connecté
    def partageAccesPlaylist(self,nom_playlist,id_user,guest):
        sql_recuperation_liste_access=  """
                                            SELECT authorized_users
                                            FROM musiques_playlist
                                            WHERE nom_playlist LIKE ?;
                                        """
        self.cursor.execute(sql_recuperation_liste_access,(nom_playlist,))
        data = self.cursor.fetchall()
        # On vérifie si l'entrée "ahtorized_users" est à NULL ou pas
        aucun_authorized_users=False
        users_deja_autorises=""
        for line in data:
            if line[0]:
                users_deja_autorises = users_deja_autorises + line[0] + "\n"
            if line[0] is None:
                aucun_authorized_users=True
            else:
                aucun_authorized_users=False

        sql_update_liste_access=""
        # Entrée non NULL, on CONCAT avec une fonction sql pour rajouter des données, séparateur :
        if aucun_authorized_users == False:
            sql_update_liste_access="""
                                        UPDATE musiques_playlist 
                                        SET authorized_users = CONCAT(authorized_users,":",?)
                                        WHERE nom_playlist=? AND id_user=?;
                                    """
        # Entrée NULL, on met à jour l'entrée "authorized_users"
        else:
            sql_update_liste_access="""
                                        UPDATE musiques_playlist
                                        SET authorized_users=?
                                        WHERE nom_playlist=? AND id_user=?;
                                    """
        self.cursor.execute(sql_update_liste_access,(guest, nom_playlist, id_user))
        self.connection.commit()

    # Récupère liste_amis de l'utilisateur
    def resultatListeAmis(self,nom_user):
        sql="SELECT liste_amis FROM user where nom_user=?;"
        self.cursor.execute(sql,(nom_user,))
        #TODO try catch dans le for pour dodge le null pointer exception
        data = self.cursor.fetchall()
        affichage_complet=""
        for line in data:
            affichage_complet = affichage_complet + line[0] + "\n"
        return affichage_complet

    # Il fait au moins 8000°C dans ma pièce, flemme
    def supprimerAmi(self):
        print()

    # On ajoute un ami dans l'entree liste_amis de l'utilisateur.
    # Même logique que dans la fonction partageAccesPlyalist.
    def ajouterAmi(self, nom_user, nom_amis):
        sql_recuperation_liste_access="""SELECT liste_amis FROM user WHERE nom_user=?;"""
        self.cursor.execute(sql_recuperation_liste_access,(nom_user,))
        data = self.cursor.fetchall()
        amis_deja_enregistres=""
        aucun_ami=False
        # On vérifie si l'entrée est à NULL
        for line in data:
            if line[0]:
               amis_deja_enregistres=amis_deja_enregistres+ line[0] +"\n"
            if line[0] is None:
                aucun_ami=True
            else:
                aucun_ami=False
        sql_update_liste_access=""
        if aucun_ami == False:
            sql_update_liste_access='UPDATE user SET liste_amis = CONCAT(liste_amis,":", ?) where nom_user=?;'
        else:
            sql_update_liste_access='UPDATE user SET liste_amis = ? where nom_user=?;'

        self.cursor.execute(sql_update_liste_access,(nom_amis,nom_user,))
        self.connection.commit()

    # On close la bdd 
    def closeBdd(self):
        self.connection.close()

# En dessous se trouvent tous les tests de mes fonctions.
# Sauf erreur elles fonctionnent toutes lorsque appelées depuis ce fichier (voir commentaires de la fonction qui pose problème).

#bdd = Bdd()
# print(bdd.verificationUtilisateur("formation", "formation"))
# print("")
# print(bdd.resultatRechercheMusiques(""))
# print("")
#print(bdd.resultatListePlaylists("formation"))
#print(bdd.recupereMusiquesDepuisPlaylist("formation"))
# print("")
# bdd.ajouterMusiqueAPlaylist("test",1,7)
# print("")
# bdd.supprimerPlaylist("test_toto_2",2)
# print("")
#bdd.partageAccesPlaylist("test",1,"coucou")
#bdd.ajouterAmi("formation","titututu")
#print(bdd.recupererIdMusiqueDepuisNom("'Kutiman - Tanzania.mp3'"))
#print(bdd.recupererIdUserDepuisNom("formation"))
