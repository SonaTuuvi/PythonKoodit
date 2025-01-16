import math  # Tarvitaan matemaattisia toimintoja varten

# Kysytään käyttäjältä ympyrän säde
sade = float(input("Anna ympyrän säde: "))

# Lasketaan ympyrän pinta-ala
pinta_ala = math.pi * sade**2

# Tulostetaan ympyrän pinta-ala käyttäen f-merkkijonoa (f-string)
# Ensimmäinen 'f' ennen lainausmerkkejä mahdollistaa muuttujien käytön merkkijonossa
# {pinta_ala:.2f} - Tämä sisällä oleva 'f' tarkoittaa, että pinta-ala tulostetaan
# kahden desimaalin tarkkuudella ('.2') liukulukuna ('f' = floating-point number)
print(f"Ympyrän pinta-ala on: {pinta_ala:.2f}")