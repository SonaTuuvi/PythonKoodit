# Ohjelma, joka kysyy käyttäjältä lukuja ja löytää pienimmän ja suurimman
luvut = []  # Lista tallentaa käyttäjän syöttämät luvut

while True:
    syote = input("Anna luku (tyhjä merkkijono lopettaa): ").strip()  # Pyydetään käyttäjältä syöte ja poistetaan mahdolliset välilyönnit
    if syote == "":  # Tarkistetaan, onko syöte tyhjä merkkijono
        break  # Lopetetaan silmukka, jos syöte on tyhjä

    number = int(syote)  # Muutetaan syöte kokonaisluvuksi
    luvut.append(number)  # Lisätään luku listaan

print(f"Pienin luku: {min(luvut)}")  # Tulostetaan pienin luku
print(f"Suurin luku: {max(luvut)}")  # Tulostetaan suurin luku

