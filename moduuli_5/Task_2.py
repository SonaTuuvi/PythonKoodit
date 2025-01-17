# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja ja
# lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
# suuruusjärjestyksessä suurimmasta alkaen

def kerää_luvut_ja_tulosta_suurimmat():
    # Alustetaan tyhjä lista lukujen tallentamiseen
    luvut = []

    # Kysytään lukuja käyttäjältä, kunnes syötetään tyhjä merkkijono
    while True:
        syöte = input("Syötä luku (tai paina Enter lopettaaksesi): ")  # Pyydetään käyttäjää syöttämään luku
        if syöte == "":  # Jos syöte on tyhjä, lopetetaan syöttö
            break
        try:
            luku = int(syöte)  # Muunnetaan syöte liukuluvuksi (float)
            luvut.append(luku)  # Lisätään luku listaan
        except ValueError:  # Käsitellään virhe, jos syöte ei ole kelvollinen luku
            print("Syötä kelvollinen luku.")

    # Järjestetään lista suurimmasta pienimpään
    luvut.sort(reverse=True)

    # Tulostetaan viisi suurinta lukua
    print("Viisi suurinta lukua ovat:")
    for luku in luvut[:5]:  # Käydään läpi listan viisi ensimmäistä alkiota
        print(luku)

# Käynnistä ohjelma
kerää_luvut_ja_tulosta_suurimmat() # Kutsutaan funktiota ohjelman suorittamiseksi