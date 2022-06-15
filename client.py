#!/usr/bin/env python
from re import A

from sys import version
import random
import os
import bdd

ip_address = "192.168.0.1"
username = "daxtors"
password = "loul"

def connexion (user):
    
def creation_compte (users):
    
def search_key_word (music):
    
def show_playlist (playlist):

def show_friends (friends):   

def telechargement (doawnload):
    
def add_playlist (play):
    
     

while True:
    print ("############# Bienvenue sur SPOTIFREE #############")
    print ("\n"*5)
    print ("Connexion: (1) pour rentrer vos log, (2) pour creer un compte ")
    if reponse not in ['1','2'] : 
        reponse = input ("que voulez vous faire (1,2) ")
    if reponse in ['1']:
        print("entre votre nom d'utilisateur et votre mot de passe")
        connexion
        if connexion == True:
            print ("########### Bievenue dans votre espace personelle ########")
            print ("(1)Chercher une musique")
            print ("(2)Playlist")
            print ("(3)Spotifriends")
            if reponse in ['1']:
                print ("\n"*5)
                print ("veuillez entre un mot clef pour la chanson desirer:")
                search_key_word
                print (" que voulez vous faire: a) telecharger la musique vers votre repertoire personnelle")
                print ("b) ajouter a une playlist")
                if reponse in ['a']:
                    telechargement
                if reponse in ['b']:
                    add_playlist
            if reponse in ['2']:
                print ("\n"*5)
                show_playlist
                #ajoute supression playlist
                #lecture d"une playlist (option aleatoire)
            if reponse in ['3']:
                print ("\n"*5)
                show_friends
                #ajouter ou suprrimer amis
                #envoyer des messages
                #partage playlist
    if reponse in ['2']:
        print ("veuillez saisir un nom d'utilisateur et un mot de passe")
        creation_compte
        
    
        
    
    

