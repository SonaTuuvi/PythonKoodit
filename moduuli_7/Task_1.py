# Ohjelma, joka määrittää vuodenajan kuukauden numeron perusteella
def vuoden_aika():
    # Määritellään monikko, jossa on vuodenajat järjestyksessä kuukausittain
    kuukaudet = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
    # Pyydetään käyttäjältä kuukauden numero
    numero = int(input("Syötä kuukauden numero (1-12): "))
    # Tarkistetaan, että numero on kelvollinen
    if 1 <= numero <= 12:
        # Tulostetaan vastaava vuodenaika
        print(f"Kuukausi kuuluu vuodenaikaan: {kuukaudet[numero - 1]}")
    else:
        # Virheilmoitus, jos numero ei ole välillä 1-12
        print("Virheellinen kuukauden numero!")

vuoden_aika()