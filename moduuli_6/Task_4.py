# Funktio, joka laskee annetun listan lukujen summan
def lasketa_summa(array):
    return sum(array)  # Palauttaa listan lukujen summan

# Pääohjelma, jossa suoritetaan ohjelman päälogiikka
def paaohjelama():
    # Pyydetään käyttäjältä kokonaislukuja syötteenä ja muunnetaan ne listaksi
    array_input = list(map(int, input("Anna kokonaislukuja ").split()))
    # Kutsutaan lasketa_summa-funktiota laskemaan annettujen lukujen summa
    summa = lasketa_summa(array_input)
    # Tulostetaan kokonaislukujen summa käyttäjälle
    print(f"kokonais-summa on {summa} ")

# Kutsutaan pääohjelmaa, jotta ohjelma suoritetaan
paaohjelama()