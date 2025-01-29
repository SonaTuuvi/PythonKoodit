# Tämä koodi toteuttaa ohjelman, jossa:
# anna_nopan_luku-funktio: palauttaa satunnaisen nopan silmäluvun väliltä 1–6 simuloiden nopan heittoa.
# Pääohjelma: heittää noppaa jatkuvasti, kunnes saadaan kuutonen.
# Jokaisen heiton jälkeen tulostetaan saatu silmäluku.
# Kun kuutonen tulee, ohjelma lopettaa heittämisen.
import random

# Funktio palauttaa satunnaisen luvun väliltä 1-6, joka simuloi nopan heittoa.
def anna_nopan_luku():
    return random.randint(1, 6)

# Funktio tarkistaa, onko saatu silmäluku kuusi.
def onko_kuusi(number):
    return number == 6

# Funktio laskee silmälukujen summan ja lopettaa, kun saadaan kuutonen.
def laske_summa():
    sum = 0  # Alustetaan summa nollaksi.
    while True:  # Jatketaan, kunnes kuutonen saadaan.
        number = anna_nopan_luku()  # Heitetään noppaa.
        if onko_kuusi(number):  # Tarkistetaan, onko kuutonen.
            break  # Lopetetaan silmukka, jos kuutonen.
        else:
            sum += number  # Lisätään luku summaan.
    return sum  # Palautetaan summa.

# Pääohjelma
print(f"Kokonaislukujen summa ennen kuutosta: {laske_summa()}")