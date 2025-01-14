# Pyydetään käyttäjältä kolme kokonaislukua
num_1 = int(input("Anna ensimmäinen luku: "))
num_2 = int(input("Anna toinen luku : "))
num_3 = int(input("Anna kolmas luku : "))

# Lasketaan lukujen summa, tulo ja keskiarvo
summa = num_1 + num_2 + num_3       # Lukujen summa
tulo = num_1 * num_2 * num_3        # Lukujen tulo
keskiarvo = summa / 3               # Lukujen keskiarvo

# Tulostetaan tulokset
print(f"Lukujen summa on: {summa}")
print(f"Lukujen tulo on: {tulo}")
print(f"Lukujen k1eskiarvo on: {keskiarvo:.2f}")