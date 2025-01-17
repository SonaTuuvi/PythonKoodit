# Ohjelma, joka muuntaa tuumia senttimetreiksi
while True:  # Jatketaan silmukkaa, kunnes käyttäjä syöttää negatiivisen arvon
    tuumi = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))  # Pyydetään käyttäjältä syöte
    if tuumi < 0:  # Tarkistetaan, onko syöte negatiivinen
        print("Ohjelma lopetettu.")  # Ilmoitetaan ohjelman lopetus
        break  # Lopetetaan silmukka
    print(f"{tuumi} tuumaa on {tuumi * 2.54:.2f} senttimetriä.")  # Muunnetaan tuumat senttimetreiksi ja tulostetaan tulos
