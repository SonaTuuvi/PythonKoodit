from flask import Flask, jsonify  # Tuodaan tarvittavat kirjastot Flask-sovellusta varten

app = Flask(__name__)  # Luodaan Flask-sovellus

# Määritetään suurin esilaskettava luku alkulukujen tarkistusta varten
MAX_N = 1000000


def luo_alkuluvut(n):
    """
    Luo listan, joka kertoo, onko kukin luku välillä [0, n] alkuluku.
    Käytetään Eratostheneen seula -algoritmia tehokkaaseen alkulukujen esilaskentaan.

    :param n: Suurin tarkistettava luku (kokonaisluku).
    :return: Lista, jossa True tarkoittaa, että luku on alkuluku, ja False tarkoittaa, ettei ole.
    """
    onko_alkuluku = [True] * (n + 1)  # Alustetaan kaikki luvut alkuluvuiksi
    onko_alkuluku[0] = onko_alkuluku[1] = False  # 0 ja 1 eivät ole alkulukuja

    # Käydään luvut läpi ja merkitään yhdellä kertaa kaikki niiden monikerrat ei-alkuluvuiksi
    for i in range(2, int(n ** 0.5) + 1):  # Tarkistetaan vain luvut sqrt(n) asti
        if onko_alkuluku[i]:  # Jos luku on alkuluku
            for j in range(i * i, n + 1, i):  # Merkitään sen monikerrat ei-alkuluvuiksi
                onko_alkuluku[j] = False

    return onko_alkuluku  # Palautetaan lista, jossa alkuluvut on merkitty


# Luodaan esilaskettu lista alkuluvuista
alkuluvut = luo_alkuluvut(MAX_N)


def onko_alkuluku(n):
    """
    Tarkistaa, onko annettu luku alkuluku.

    :param n: Tarkistettava luku (kokonaisluku).
    :return: True, jos luku on alkuluku, muuten False.
    """
    if n <= MAX_N:  # Jos luku on esilasketussa listassa, käytetään suoraa tarkistusta
        return alkuluvut[n]

    if n < 2:  # Kaikki luvut alle 2 eivät ole alkulukuja
        return False

    # Tarkistetaan luvun jaollisuus kaikilla luvuilla 2 - sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Jos luku jakautuu ilman jakojäännöstä, se ei ole alkuluku

    return True  # Jos jaollisuutta ei löytynyt, luku on alkuluku


@app.route('/alkuluku/<int:luku>', methods=['GET'])
def tarkista_alkuluku(luku):
    """
    Flask-reitti, joka tarkistaa, onko annettu luku alkuluku.
    URL-osoitteessa oleva kokonaisluku tarkistetaan, ja vastaus palautetaan JSON-muodossa.

    :param luku: Tarkistettava luku (kokonaisluku).
    :return: JSON-muotoinen vastaus, jossa luku ja tieto siitä, onko se alkuluku.
    """
    tulos = {"Number": luku, "isPrime": onko_alkuluku(luku)}
    return jsonify(tulos)  # Palautetaan JSON-muotoinen vastaus


# Käynnistetään Flask-sovellus
if __name__ == '__main__':
    app.run(debug=True, port=3000)  # Flask pyörii portissa 3000 ja debug-tila on päällä
