# On importe les fonctions dont on aura besoin
from gtts import gTTS
import os

# Ouverture du fichier texte et récupération de son contenu dans une variable
f = open("text.txt")
x = f.read()

# Définition de la langue du fichier texte
langue = 'fr'

# Gestion de l'audio
audio = gTTS(text=x, lang=langue, slow=False)
""" On sauvegarde l'audio sous forme de fichier wav et on procède à la lecture
    - La lecture dépend de l'OS utilisé.Étant sous linux j'ai utilisé des modules qui
      permettent d'effectuer une lecture audio en mode console 
    - Sous windows il s'agira juste de rentrer dans votre terminal powershell pour compiler le code
      et d'enlever le mot play de la commande"""
audio.save("audio.mp3")
os.system("play audio.mp3")
