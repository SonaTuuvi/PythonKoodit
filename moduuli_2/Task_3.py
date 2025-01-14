# Pyydetään käyttäjältä suorakulmion kannan ja korkeuden
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# Lasketaan suorakulmion piiri ja pinta-ala
piiri = 2 * (kanta + korkeus)  # Suorakulmion piiri: 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus   # Suorakulmion pinta-ala: kanta * korkeus

# Tulostetaan suorakulmion piiri ja pinta-ala
print(f"Suorakulmion piiri on: {piiri:.2f}")
print(f"Suorakulmion pinta-ala on: {pinta_ala:.2f}")
5