import random
import time
import string
mot_de_passe = input("quel est votre mot de passe: ")  # mot de passe

def mot_trouver(longueur):
    #  liste des elements à utiliser
    #  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lettres = string.ascii_letters
    mot_genere = ""  # attente du mot de passe

    # boucle
    for carac in range(len(mot_de_passe)):
        mot_genere = mot_genere + lettres[random.randint(0,25)]
    return mot_genere

debut = time.time()
while True:
    mot_alea = mot_trouver(len(mot_de_passe))
    print("mot de passe testé :" + mot_alea)
    if mot_de_passe == mot_alea:
        print("mot de passe trouvé: " + mot_alea)
        fin = time.time() - debut
        print("toruvé en : " + str(fin) + ' secondes')
        break