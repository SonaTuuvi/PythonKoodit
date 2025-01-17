import random
# Ohjelma toteutaa algoritmi piin (π) likiarvon laskemiseksi Monte Carlon menetelmällä.
# Tämä menetelmä perustuu tilastolliseen mallinnukseen:
# valitsemme satunnaisesti monta pistettä ympyrän sisältävästä neliöstä
# ja määritämme kuinka monta pistettä on ympyrän sisällä. Sitten lasketaan π suhdeluvulla.

def estimate_pi(num_points):
    inside_circle = 0  # Lasketaan ympyrän sisälle jäävien pisteiden määrä
    count = 0  # Laskuri toistojen seuraamiseen

    while count < num_points:  # Toistetaan, kunnes pisteiden määrä on saavutettu
        # Generoidaan satunnainen piste (x, y) neliön sisällä
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Tarkistetaan, jääkö piste ympyrän sisälle
        if x ** 2 + y ** 2 < 1:
            inside_circle += 1  # Kasvatetaan ympyrän sisäpuolisten pisteiden laskuria
        count += 1  # Kasvatetaan laskuria
        # Lasketaan π likiarvo

    pi_estimate = 4 * inside_circle / num_points
    return pi_estimate

# Pääohjelma
if __name__ == '__main__':
    num_points = int(input("Anna pisteiden määrä (esim. 1000000): "))  # Pyydetään käyttäjältä pisteiden määrä
    if num_points <= 0:
        print("Pisteiden määrän tulee olla positiivinen kokonaisluku.")  # Tarkistetaan, että määrä on positiivinen
    else:
        pi_value = estimate_pi(num_points)  # Lasketaan piin likiarvo käyttäjän antamalla pisteiden määrällä
        print(f"Piin likiarvo {num_points} pisteellä: {pi_value}")  # Tulostetaan tulos

"""
Proportio

Ympyrän pinta-ala: πr^2, missä r=1, joten ympyrän pinta-ala on π.
Neliön pinta-ala: (2r)^2 = 4.
Ympyrän ja neliön pinta-alojen suhde: π / 4.

Jos valitsemme satunnaisesti pisteitä neliön sisältä, ympyrään osuvien pisteiden osuus
lähestyy arvoa π / 4. Tämä tarkoittaa, että:

n / N ≈ π / 4,

missä:
- n on ympyrän sisään osuvien pisteiden määrä.
- N on kaikkien pisteiden kokonaismäärä.

Tästä voidaan johtaa:
π ≈ 4 * (n / N).

2. Miten tämä toimii?
- Valitsemme neliön, jonka kärkipisteet ovat (-1, -1), (1, -1), (1, 1) ja (-1, 1), koska ympyrän säde on 1.
- Generoimme satunnaisesti N pistettä (x, y), missä x ja y ovat välillä [-1, 1].
- Jokaiselle pisteelle tarkistamme, onko se ympyrän sisällä. Tämä tapahtuu testaamalla ehto:
  x^2 + y^2 < 1,
  koska pisteen etäisyyden origosta täytyy olla pienempi kuin säde (r = 1).

- Lasketaan ympyrän sisään osuvien pisteiden määrä (n).
- Lasketaan π kaavalla:
  π ≈ 4 * (n / N).
"""


