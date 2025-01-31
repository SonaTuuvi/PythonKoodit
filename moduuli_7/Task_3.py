def lentoasemat():
    # Määritellään sanakirja lentoasematietojen tallentamiseen
    lentoasemat_dict = {}
    while True:
        # Tulostetaan valikko käyttäjälle
        print("\nValitse toiminto:")
        print("1 - Lisää lentoasema")
        print("2 - Hae lentoasema")
        print("3 - Lopeta")
        # Pyydetään käyttäjältä valinta
        valinta = input("Syötä valinta: ")

        if valinta == "1":
            # Käyttäjä lisää lentoaseman: kysytään ICAO-koodi ja nimi
            icao = input("Syötä lentoaseman ICAO-koodi: ")
            nimi = input("Syötä lentoaseman nimi: ")
            # Tallennetaan tiedot sanakirjaan
            lentoasemat_dict[icao] = nimi
            print("Lentoasema lisätty.")
        elif valinta == "2":
            # Käyttäjä haluaa hakea lentoaseman tietoja
            icao = input("Syötä haettava ICAO-koodi: ")
            # Tarkistetaan, löytyykö lentoasema sanakirjasta
            if icao in lentoasemat_dict:
                print(f"Lentoaseman nimi: {lentoasemat_dict[icao]}")
            else:
                print("Lentoasemaa ei löydy.")
        elif valinta == "3":
            # Käyttäjä haluaa lopettaa ohjelman
            print("Ohjelma lopetetaan.")
            break
        else:
            # Virheilmoitus, jos valinta on virheellinen
            print("Virheellinen valinta, yritä uudelleen.")

lentoasemat()