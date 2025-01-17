def onko_alkuluku(luku):
    """
    Funktio tarkistaa, onko annettu luku alkuluku.

    Alkuluku on kokonaisluku, joka on suurempi kuin 1 ja jaollinen vain ykkösellä ja itsellään.
    Jos luku on jaollinen jollain muulla luvulla, se ei ole alkuluku.
    Optimoidussa tarkistuksessa testataan jakajia vain neliöjuureen asti.

    Parametrit:
        luku (int): Tarkistettava luku.

    Palauttaa:
        bool: True, jos luku on alkuluku, muuten False.
    """

    # Alkuluvut ovat suurempia kuin 1. Luvut, jotka ovat pienempiä tai yhtä suuria kuin 1, eivät ole alkulukuja.
    if luku <= 1:
        return False

    # Tarkistetaan, onko luvulla jakajia väliltä 2 ja √luku.
    # Miksi riittää tarkistaa vain √lukuun asti?
    # Jos luku on jaollinen jollakin luvulla i, niin täytyy olla olemassa myös toinen jakaja j siten, että i * j = luku.
    # Jos i on suurempi kuin √luku, niin j on pienempi kuin √luku.
    # Esimerkki: Jos luku = 36, jakajat ovat 2*18, 3*12, 4*9, 6*6. Riittää tarkistaa luvut 2, 3, 4, 5, 6.
    for i in range(2, int(luku ** 0.5) + 1):  # Käydään läpi luvut 2:sta neliöjuureen asti
        # Jos luku on jaollinen i:llä, se ei ole alkuluku.
        if luku % i == 0:
            return False  # Palautetaan heti False, jos löytyy jakaja.

    # Jos ei löydy yhtään jakajaa, palautetaan True, eli luku on alkuluku.
    return True


def tarkista_alkuluku():
    """
    Pääohjelma, joka kysyy käyttäjältä luvun ja ilmoittaa, onko se alkuluku.
    """
    try:
        # Pyydetään käyttäjältä kokonaisluku
        luku = int(input("Syötä kokonaisluku: "))  # Käyttäjältä kysytään luku

        # Kutsutaan funktiota tarkistamaan, onko luku alkuluku
        if onko_alkuluku(luku):
            print(f"Luku {luku} on alkuluku.")  # Tulostetaan, jos luku on alkuluku
        else:
            print(f"Luku {luku} ei ole alkuluku.")  # Tulostetaan, jos luku ei ole alkuluku

    except ValueError:
        # Jos syöte ei ole kokonaisluku, annetaan virheilmoitus
        print("Syötä kelvollinen kokonaisluku.")  # Kehotetaan syöttämään kelvollinen kokonaisluku


# Käynnistetään ohjelma
tarkista_alkuluku()
