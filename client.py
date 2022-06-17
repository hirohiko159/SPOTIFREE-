

    
#!/usr/bin/env python
from re import A
import paramiko
from sys import version
import random
import os
# import bdd

#connection au serveur par SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('127.0.0.1', username='spotifree', password='loul')
reponse=''
login=False


#creation du menu spotifree avec plusieurs choix, on demande a l'utilisateur un nom de compte et un mot de passe, puis on les rentre en argument 
#pour les envoyer au serveur afin qu'ils soient verifiés, on lit la sortie (stdout), et si les log sont bons cela renvoie un 0,l'utilisateur peut acceder
#à son compte, où il peut rechercher une musique par mot clef.les autres fonctions n'ont pas pu etre finies par manque de temps.
print ("############# Bienvenue sur SPOTIFREE #############")
while login==False:
   
    print ("\n"*5)
    print ("Connexion: (1) pour rentrer vos log, (2) pour creer un compte ")
    if reponse not in ['1','2']: 
        reponse = input ("que voulez vous faire (1,2) ")
    if reponse in ['1']:
        userid=input("Username: ")
        userpasswd=input("Password: ")
        commande= 'python3 corescript.py authentification %s %s'%(userid,userpasswd)  
        stdin, stdout, stderr = client.exec_command(commande)
        print(stderr.read())
        rep=(stdout.read()).decode().split('\n')[0] 
        print(rep)
        stdin.close()
        if rep=='0':
            login=True   
        else : 
            print("mauvais login")
    if reponse in ['2']:
        print ("veuillez saisir un nom d'utilisateur et un mot de passe")
        #TODO + corescruipt fonction création utilisateur
print ("########### Bienvenue dans votre espace personel ########")
while True:
    print ("(1)Chercher une musique")
    print ("(2)Playlist")
    print ("(3)Spotifriends")
    reponse=input("que voulez vous faire?: ")
    if reponse in ['1']:
        print ("\n"*5)
        mot=input ("veuillez entre un mot clef pour la chanson desirer:")
        commande= 'python3 corescript.py recherche_musique %s '%(mot)  
        stdin, stdout, stderr = client.exec_command(commande)
        rep=(stdout.read()).decode().split('\n')[0] 
        print(rep)
        # print (" que voulez vous faire: a) telecharger la musique vers votre repertoire personnelle")
        # print ("b) ajouter a une playlist")
        # if reponse in ['a']:
        #     print()
            
        # if reponse in ['b']:
        #     print()
            
    if reponse in ['2']:
        print ("\n"*5)
        
        #ajoute supression playlist
        #lecture d"une playlist (option aleatoire)
    if reponse in ['3']:
        print ("\n"*5)
        
        #ajouter ou suprrimer amis
        #envoyer des messages
        #partage playlist

        
client.close()    
        

    


