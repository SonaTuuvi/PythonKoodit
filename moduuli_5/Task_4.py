# Ohjelma kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain
# samassa järjestyksessä kuin ne syötettiin.

def main():
    kaupunkien_nimet = []  # Lista kaupunkien nimien tallentamiseen
    for i in range(5):  # Toistetaan viisi kertaa, yksi kerta jokaiselle kaupungille
        nimi = input("Anna kaupungin nimi: ").strip()  # Pyydetään käyttäjältä kaupungin nimi
        kaupunkien_nimet.append(nimi)  # Lisätään nimi listaan

    # Tulostetaan kaupunkien nimet yksi kerrallaan
    for i in range(len(kaupunkien_nimet)):  # Käydään läpi listan kaikki indeksit
        print(kaupunkien_nimet[i])  # Tulostetaan kaupungin nimi

main()  # Käynnistetään ohjelma

