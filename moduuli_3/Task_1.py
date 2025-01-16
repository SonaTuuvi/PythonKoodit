# Pyydetään kuhan pituuden senttimetreinä
kuhan_pituus = int(input("Anna kuhan pituuden senttimetreinä: "))
# Tarkistetaan, onko kuha alamittainen
alin_mitta = 37 # senttimetriä

if kuhan_pituus > alin_mitta:
    print("Kuha täyttää alimman sallitun pyyntimitan.")
else:
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen. \n"
          f"Kuhaa puuttuu {alin_mitta - kuhan_pituus:.1f} cm alimmasta sallitusta pyyntimitasta.")