#!/usr/bin/env python
from re import A
import paramiko
from sys import version
import random
import os
# import bdd

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('127.0.0.1', username='daxtors', password='loul')
reponse=''

while True:
    print ("############# Bienvenue sur SPOTIFREE #############")
    print ("\n"*5)
    print ("Connexion: (1) pour rentrer vos log, (2) pour creer un compte ")
    if reponse not in ['1','2']: 
        reponse = input ("que voulez vous faire (1,2) ")
    if reponse in ['1']:
        userid=input("Username")
        userpasswd=input("Password")
        commande= 'python3 corescript.py authentification %s %s'%(userid,userpasswd)  
        stdin, stdout, stderr = client.exec_command(commande)
        print(stdout.read())
        stdin.close()

        if stdout==0:
            print ("########### Bievenue dans votre espace personel ########")
            print ("(1)Chercher une musique")
            print ("(2)Playlist")
            print ("(3)Spotifriends")

            if reponse in ['1']:
                print ("\n"*5)
                print ("veuillez entre un mot clef pour la chanson desirer:")
                
                print (" que voulez vous faire: a) telecharger la musique vers votre repertoire personnelle")
                print ("b) ajouter a une playlist")
                if reponse in ['a']:
                    print()
                    
                if reponse in ['b']:
                    print()
                    
            if reponse in ['2']:
                print ("\n"*5)
                
                #ajoute supression playlist
                #lecture d"une playlist (option aleatoire)
            if reponse in ['3']:
                print ("\n"*5)
                
                #ajouter ou suprrimer amis
                #envoyer des messages
                #partage playlist
    else : 
        print("mauvais login")
    if reponse in ['2']:
        print ("veuillez saisir un nom d'utilisateur et un mot de passe")
        #TODO + corescruipt fonction création utilisateur
        
client.close()    
        

    

