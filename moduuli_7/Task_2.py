def anna_nimet():
    # Määritellään joukko tallennettavia nimiä varten
    nimet_joukko = set()
    while True:
        # Pyydetään käyttäjältä nimi
        nimi = input("Syötä nimi (tai paina Enter lopettaaksesi): ")
        # Tarkistetaan, onko syöte tyhjä, jolloin ohjelma päättyy
        if nimi == "":
            break
        # Tarkistetaan, onko nimi jo joukossa
        if nimi in nimet_joukko:
            # Jos nimi on jo tallennettu, ilmoitetaan siitä
            print("Aiemmin syötetty nimi")
        else:
            # Lisätään uusi nimi joukkoon ja ilmoitetaan siitä
            print("Uusi nimi")
            nimet_joukko.add(nimi)

    # Tulostetaan kaikki syötetyt nimet
    print("\nSyötetyt nimet:")
    for nimi in nimet_joukko:
        print(nimi)

anna_nimet()