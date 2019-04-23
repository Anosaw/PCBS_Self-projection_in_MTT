"""
This script is used to randomize the order of events in the participant list

"""
import random

l = {1:"1985: trou ozone", 2:"1988: JO Nagoya", 3:"1991: dislocation de l'URSS",
     4:"1994: métro Bordeaux", 5:"1997: Harry Potter", 6:"2000: Lettonie Eurovision", 7:"2003: génome humain",
     8:"2006: tramway Paris", 9:"2009: création Bitcoin", 10:"2012: Curiosity Mars", 11:"2015: musée Metallica",
     12:"2018: Simone Veil", 13:"2019: Netflix Friends", 14:"2019: coupe football", 15:"2020: viandes artificielles",
     16:"2023: loup Japon", 17:"2026: Inauguration Dubailand", 18:"2029: usine photosynthèse", 19:"2032: Grand Paris",
     20:"2035: bateaux automatiques", 21:"2038: avions solaires", 22:"2041: tunnel Béring", 23:"2044: thérapie Sida",
     24:"2047: 9.5 milliards", 25:"2050: humain Mars", 26:"2053: gaz renouvelable"}

nb = list(range(1,27))
random.shuffle(nb)

for element in nb:
    print(l[element])
