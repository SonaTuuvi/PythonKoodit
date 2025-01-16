# Kysytään käyttäjältä laivan hyttiluokka
hyttiluokka = input("Anna laivan hyttiluokka: ")

# Tarkistetaan syöte ja tulostetaan kuvaus
if hyttiluokka  == "LUX":
    print(f"{hyttiluokka} on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print(f"{hyttiluokka} on ikkunallinen hytti autokannen yläpuolella")
elif hyttiluokka == "B":
    print(f"{hyttiluokka} on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print(f"{hyttiluokka} on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")



