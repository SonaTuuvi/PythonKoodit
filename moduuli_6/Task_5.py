# Funktio, joka poistaa parittomat luvut annetusta listasta
def ottaa_pois_parittomat_luvut(array):
    karsitun_lista = list()  # Luodaan uusi lista parillisille luvuille
    for i in array:  # Käydään läpi kaikki listan alkiot
        if i % 2 == 0:  # Tarkistetaan, onko luku parillinen
            karsitun_lista.append(i)  # Lisätään parillinen luku listaan
    return karsitun_lista  # Palautetaan lista, jossa on vain parilliset luvut

# Funktio, joka pyytää käyttäjältä syötteenä lukuja ja palauttaa ne listana
def anna_luvut():
    luvut_list = list(map(int, input("Anna luvut: ").split()))  # Muutetaan syöte listaksi kokonaislukuja
    return luvut_list  # Palautetaan lista luvuista

# Pääohjelma, jossa kutsutaan muita funktioita
def paaohjelma():
    print(ottaa_pois_parittomat_luvut(anna_luvut()))  # Tulostetaan lista parillisista luvuista

# Suoritetaan pääohjelma
paaohjelma()
