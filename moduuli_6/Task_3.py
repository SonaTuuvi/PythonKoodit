# Funktio, joka muuntaa nestegallonat litroiksi
def nestegallonoilta_litramaaraan(gallonat):
    return gallonat * 3.78541  # 1 gallona = 3.78541 litraa

# Pääohjelma
def paohjelma():
    while True:
        # Kysytään käyttäjältä gallonamäärä
        gallonat = float(input("Anna bensiinin määrä Yhdysvaltain nestegallonoina (negatiivinen lopettaa): "))
        if gallonat < 0:  # Lopetetaan ohjelma, jos käyttäjä antaa negatiivisen arvon
            print("Ohjelma lopetettu.")
            break
        # Muutetaan gallonat litroiksi käyttäen funktiota
        litrat = nestegallonoilta_litramaaraan(gallonat)
        print(f"{gallonat} nestegallonaa on {litrat} litraa.")

# Suoritetaan pääohjelma
paohjelma()
