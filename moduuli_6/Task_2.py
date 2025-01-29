# Tämä koodi toteuttaa ohjelman, jossa:
# anna_nopan_luku-funktio: palauttaa satunnaisen nopan silmäluvun väliltä 1–6 simuloiden nopan heittoa.
# Pääohjelma: heittää noppaa jatkuvasti, kunnes saadaan kuutonen.
# Jokaisen heiton jälkeen tulostetaan saatu silmäluku.
# Kun kuutonen tulee, ohjelma lopettaa heittämisen.
import random

# Funktio palauttaa satunnaisen luvun väliltä 1-tahkojen määrä.
def anna_nopan_luku(tahkot):
    return random.randint(1, tahkot)

# Funktio laskee silmälukujen summan ja lopettaa, kun saadaan maksimisilmäluku.
def laske_summa(tahkot):
    summa = 0  # Alustetaan summa nollaksi.
    while True:  # Heitetään noppaa, kunnes maksimisilmäluku saavutetaan.
        numero = anna_nopan_luku(tahkot)  # Heitetään noppaa.
        summa += numero  # Lisätään luku summaan.
        print(f"Heiton tulos: {numero}")
        if numero == tahkot:  # Lopetetaan, jos saadaan maksimiarvo.
            break
    return summa  # Palautetaan summa.

# Pääohjelma
def paaohjelma():
    tahkot = int(input("Anna nopan tahkojen yhteismäärä: "))  # Kysytään nopan tahkojen määrä.
    print(f"Kokonaislukujen summa: {laske_summa(tahkot)}")

# Suoritetaan ohjelma.
paaohjelma()
