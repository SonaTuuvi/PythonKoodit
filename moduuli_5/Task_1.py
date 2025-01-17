# Ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.Ja ja tulostaa silmälukujen summan.

import random # Tuodaan käyttöön random-moduuli, jotta voimme arpoa satunnaisia lukuja.

def heita_arpakuutioita():
    numbers_of_dicce = int(input("Kuinka monta arpakuutiota heitetään? ")) #Pyydetään käyttäjä arpakuution määrä.
    if numbers_of_dicce < 0: # Tarkistetaan, että luku on vähintään 1
        print("Arpakuutioiden lukumäärän tulee olla vähintään 1.")  # Virheilmoitus, jos luku on negatiivinen tai 0
        return  # Lopetetaan ohjelman suoritus tässä tapauksessa

    # Alustetaan muuttuja heittojen summan tallentamiseen
    summa = 0  # Tässä muuttuja, johon kerätään kaikkien arpakuutioiden silmäluvut
    # Toistetaan heitto kaikille arpakuutioille
    for i in range(numbers_of_dicce):# Silmukassa käydään läpi niin monta kierrosta kuin käyttäjä syötti
        summa += random.randint(1, 6)# Arvotaan satunnainen luku välillä 1 ja 6

# Tulostetaan silmälukujen summa
    print(f"Heitettyjen arpakuutioiden silmälukujen summa on: {summa}")  # Näytetään käyttäjälle laskettu summa

# Käynnistä ohjelma
heita_arpakuutioita()  # Kutsutaan funktiota ohjelman suorittamiseksi