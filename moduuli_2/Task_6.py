import random

# Luo tyhjä lista tallentamaan numerot
numerot = []

# Arvotaan kolme satunnaista lukua väliltä 0..9
for _ in range(3):
    satunnainen_luku = random.randint(0, 9)  # Arvotaan satunnainen luku
    numerot.append(str(satunnainen_luku))   # Muutetaan merkkijonoksi ja lisätään listaan

# Yhdistetään numerot yhdeksi merkkijonoksi
kolmenumeroinen_koodi = ''.join(numerot)

numerot.clear()  # Tyhjennetään lista "numerot". Kaikki sen sisältämät arvot poistetaan, mutta lista itse säilyy tyhjänä.

for _ in range(4):
    satunnainen_luku = random.randint(1, 6)  # Arvotaan satunnainen luku
    numerot.append(str(satunnainen_luku))   # Muutetaan merkkijonoksi ja lisätään listaan

nelinumeroinen_koodi = ''.join(numerot)

# Tulostetaan koodi
print(f"Kolmenumeroinen koodi: {kolmenumeroinen_koodi}")
print(f"Nelinumeroinen koodi: {nelinumeroinen_koodi}")
