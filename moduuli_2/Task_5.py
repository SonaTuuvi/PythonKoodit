# Pyydetään käyttäjältä leiviskät, naulat ja luodit
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Määritellään vakioiden suhteet
naula_per_leiviska = 20          # Yksi leiviskä on 20 naulaa
luoti_per_naula = 32             # Yksi naula on 32 luotia
gramma_per_luoti = 13.3          # Yksi luoti on 13,3 grammaa

# Lasketaan kokonaisgrammat
kokonais_luoti = (leiviskat * naula_per_leiviska * luoti_per_naula) + (naulat * luoti_per_naula) + luodit
kokonais_grammat = kokonais_luoti * gramma_per_luoti

# Muunnetaan grammat kilogrammoiksi ja grammoiksi
kilogrammat = int(kokonais_grammat // 1000)  # Täydet kilogrammat
grammat = kokonais_grammat % 1000           # Jäljelle jäävät grammat

# Tulostetaan tulos
print(f"Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")
