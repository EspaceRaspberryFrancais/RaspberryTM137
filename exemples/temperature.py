#!/usr/bin/env python3

# Importation des librairies
import tm1637
from time import sleep

# Definition de la reference de la sonde (remplacer les x par la ref.)
# Pour connaitre la ref. :
# cd /sys/bus/w1/devices/
# ls
nomSonde = "28-xxx"

# Initialisation de l'afficheur
tm = tm1637.TM1637(clk=23, dio=24)


# Fonction qui recupere et renvoie la temperature en float
def recup_temp(emplacement):
    fich_temp = open(emplacement)
    contenu_fich = fich_temp.read()
    fich_temp.close()
    seconde_ligne = contenu_fich.split("\n")[1]
    temperature_data = seconde_ligne.split(" ")[9]
    temperature = float(temperature_data[2:]) / 1000
    return temperature


# Affiche la temperature recuperee par la fonction recup_temp (arrondie)
def afficher_temp(emplacement_fich):
    temperature = recup_temp(emplacement_fich)
    tm.temperature(int(round(temperature)))
    print(temperature)


# Boucle inifinie appelant la fonction afficher_temp
while True:
    afficher_temp("/sys/bus/w1/devices/" + nomSonde + "/w1_slave")
    sleep(0.5)
