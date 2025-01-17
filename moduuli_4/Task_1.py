# Tulostetaan kolmella jaolliset luvut väliltä 1..1000
luku = 1  # Aloitetaan luvusta 1

while luku <= 1000:  # Jatketaan, kunnes luku on korkeintaan 1000
    if luku % 3 == 0:  # Tarkistetaan, onko luku jaollinen kolmella
        print(luku)  # Tulostetaan luku, jos se on jaollinen kolmella
    luku += 1  # Kasvatetaan lukua yhdellä jokaisessa silmukan kierrossa