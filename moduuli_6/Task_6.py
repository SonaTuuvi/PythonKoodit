import math

def laske_yksikköhinta(halk_cm, hinta):
    """Laskee pizzan yksikköhinnan euroina per neliömetri."""
    halkaisija_m = halk_cm / 100  # Muutetaan halkaisija metreiksi (cm → m)
    sade_m = halkaisija_m / 2  # Lasketaan pizzan säde (r = d/2)
    pinta_ala_m2 = math.pi * (sade_m ** 2)  # Lasketaan pinta-ala kaavalla A = πr²
    return hinta / pinta_ala_m2  # Lasketaan yksikköhinta (€/m²)

def kysy_pizzan_tiedot(numero):
    """Kysyy käyttäjältä pizzan halkaisijan ja hinnan."""
    print(f"Anna {numero}. pizzan tiedot:")  # Pyydetään käyttäjältä syötteet
    halkaisija = float(input("Halkaisija (cm): "))  # Käyttäjä syöttää halkaisijan
    hinta = float(input("Hinta (€): "))  # Käyttäjä syöttää hinnan
    return halkaisija, hinta  # Palautetaan syötteet

def vertaile_pizzoja(yksikköhinta1, yksikköhinta2):
    """Vertailee kahden pizzan yksikköhintoja ja tulostaa paremman vaihtoehdon."""
    print(f"\nPizza 1 yksikköhinta: {yksikköhinta1:.2f} €/m²")  # Tulostetaan ensimmäisen pizzan yksikköhinta
    print(f"Pizza 2 yksikköhinta: {yksikköhinta2:.2f} €/m²")  # Tulostetaan toisen pizzan yksikköhinta

    # Selvitetään, kumpi pizza on halvempi yksikköhinnan perusteella
    if yksikköhinta1 < yksikköhinta2:
        print("\nEnsimmäinen pizza antaa paremman vastineen rahalle!")  # Ensimmäinen pizza on edullisempi
    elif yksikköhinta2 < yksikköhinta1:
        print("\nToinen pizza antaa paremman vastineen rahalle!")  # Toinen pizza on edullisempi
    else:
        print("\nMolemmat pizzat ovat yhtä edullisia!")  # Pizzat ovat yhtä hyviä hinnan suhteen

def main():
    """Pääohjelma, joka suorittaa ohjelman vaiheet."""
    halkaisija1, hinta1 = kysy_pizzan_tiedot(1)  # Pyydetään ensimmäisen pizzan tiedot käyttäjältä
    halkaisija2, hinta2 = kysy_pizzan_tiedot(2)  # Pyydetään toisen pizzan tiedot käyttäjältä

    yksikköhinta1 = laske_yksikköhinta(halkaisija1, hinta1)  # Lasketaan ensimmäisen pizzan yksikköhinta
    yksikköhinta2 = laske_yksikköhinta(halkaisija2, hinta2)  # Lasketaan toisen pizzan yksikköhinta

    vertaile_pizzoja(yksikköhinta1, yksikköhinta2)  # Vertaillaan pizzojen hintoja ja tulostetaan tulos

main()