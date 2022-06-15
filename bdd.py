import mariadb
import sys
import os

os.system('clear')

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

    def affichage(self, reponse):
        affichage=""
        for line in reponse:
            affichage = affichage + " | ".join(line) 
        return affichage

    def verificationUtilisateur(self,username,password):
        sql="SELECT nom_user FROM user WHERE nom_user=? AND pwd=?;"
        self.cursor.execute(sql,(username,password))
        data=self.cursor.fetchall()  
        if data:
            return True
        return False    

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
    
    def resultatListePlaylists(self,nom_user):
        sql="""
                SELECT nom_playlist,id_user 
                FROM musiques_playlist 
                INNER JOIN user 
                ON user.id = musiques_playlist.id_user
                WHERE nom_user = ?; 
            """
        self.cursor.execute(sql,(nom_user,))
        data = self.cursor.fetchall()
        affichage_complet = ""
        for line in data:
            affichage_complet = affichage_complet + line[0] + "\n"
        return affichage_complet
    
    def ajouterMusiqueAPlaylist(self,nom_playlist,id_user,id_musique):
        sql="""
                INSERT INTO musiques_playlist 
                    (nom_playlist, id_user, id_musique, authorized_users) 
                VALUE 
                    (?,?,?,"");
            """
        self.cursor.execute(sql,(nom_playlist,id_user,id_musique))
        self.connection.commit()
    
    def supprimerPlaylist(self,nom_playlist,id_user):
        sql="""
                DELETE FROM musiques_playlist
                WHERE (nom_playlist = ? AND id_user = ?);
            """
        self.cursor.execute(sql,(nom_playlist,id_user))
        self.connection.commit()
    
    def partageAccesPlaylist(self,nom_playlist,id_user,guest):
        sql_recuperation_liste_access=  """
                                            SELECT authorized_users
                                            FROM musiques_playlist
                                            WHERE nom_playlist LIKE ?;
                                        """
        self.cursor.execute(sql_recuperation_liste_access,(nom_playlist,))
        data = self.cursor.fetchall()
        users_deja_autorises=""
        for line in data:
            if line[0]:
                print("pas vide")
            else:
                print("vide")
            users_deja_autorises = users_deja_autorises + line[0] + "\n"
        
        sql_update_liste_access=""
        if users_deja_autorises[0] == "":
            sql_update_liste_access="""
                                        UPDATE musiques_playlist 
                                        SET authorized_users = CONCAT(authorized_users,":",?)
                                        WHERE nom_playlist=? AND id_user=?;
                                    """
        else:
            sql_update_liste_access="""
                                        UPDATE musiques_playlist
                                        SET authorized_users=?
                                        WHERE nom_playlist=? AND id_user=?;
                                    """
        self.cursor.execute(sql_update_liste_access,(guest, nom_playlist, id_user))
        self.connection.commit()

    def resultatListeAmis(self,nom_user):
        sql="SELECT liste_amis FROM user where nom_user=?;"
        self.cursor.execute(sql,(nom_user,))
        #TODO try catch dans le for pour dodge le null pointer exception
        data = self.cursor.fetchall()
        affichage_complet=""
        for line in data:
            affichage_complet = affichage_complet + line[0] + "\n"
        return affichage_complet

    def supprimerAmi(self):
        print()

    def ajouterAmi(self, nom_amis):
        sql='select liste_amis from user where id=2;'
        self.cursor.execute(sql,(nom_amis))
        data = self.cursor.fetchall()
        amis_deja_enregistres=""
        for line in data:
            amis_deja_enregistres=amis_deja_enregistres+ line[0] +"\n"
            sql_update=""
        print(amis_deja_enregistres)
        if amis_deja_enregistres[0] != "":
            sql_update='UPDATE user SET liste_amis = CONCAT(liste_amis,":", ?) where id=2;'
        else :
            sql_update='UPDATE user SET liste_amis = ? where id=2;'

        self.cursor.execute(sql_update,(nom_amis,))
        self.connection.commit()

bdd = Bdd()

# print(bdd.verificationUtilisateur("formation", "formation"))
# print("")
# print(bdd.resultatRechercheMusiques(""))
# print("")
# print(bdd.resultatListePlaylists("toto"))
# print("")
# bdd.ajouterMusiqueAPlaylist("test",1,7)
# print("")
# bdd.supprimerPlaylist("test_toto_2",2)
# print("")
bdd.partageAccesPlaylist("test",1,"toto")
