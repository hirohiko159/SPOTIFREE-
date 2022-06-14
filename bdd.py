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

    def affichage(self, reponse):
        for line in reponse:
          print (" | ".join(line))

    def verificationUtilisateur(self,username,password):
        sql="SELECT nom_user FROM user Where nom_user=? AND pwd=?;"
        self.cursor.execute(sql,(username,password))
        data=self.cursor.fetchall()  
        if len(data):
            return True
        return False

    def resultatRechercheMusiques(nom_musique, groupe, album, annee_sortie, cursor):
        sql="SELECT nom_musique, chemin_fichier FROM musique"
        au_moins_un_champ_non_vide=False
        if nom_musique:
            if au_moins_un_champ_non_vide == False:
                sql=sql+" WHERE nom_musique='nom_musique'"
            else:
                sql=sql+" AND nom_musique='nom_musique'"
                au_moins_un_champ_non_vide=True
        elif groupe:
            if au_moins_un_champ_non_vide == False:
                sql=sql+" WHERE groupe='groupe'"
            else:
                sql=sql+" AND groupe='groupe'"
                au_moins_un_champ_non_vide=True
        elif album:
            if au_moins_un_champ_non_vide == False:
                sql=sql+" WHERE album='album'"
            else:
                sql=sql+" AND album='album'"
                au_moins_un_champ_non_vide=True
        elif annee_sortie:
            if au_moins_un_champ_non_vide == False:
                sql=sql+" WHERE annee_sortie='annee_sortie'"
            else:
                sql=sql+" AND annee_sortie='annee_sortie'"
                au_moins_un_champ_non_vide=True
        sql=sql+";"
        cursor.execute(sql)
        data = cursor.fetchall()

bdd = Bdd()
print(bdd.verificationUtilisateur("formation", "formation"))
