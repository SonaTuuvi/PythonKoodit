from flask import Flask, jsonify  # Flask web-palvelimen luomiseen ja JSON-vastausten käsittelyyn
import mariadb  # MariaDB-tietokannan käyttöön

app = Flask(__name__)  # Flask-sovellus käynnistetään

# Tietokannan yhteysasetukset (Täydennä omilla tiedoillasi)
DB_CONFIG = {
    "host": "",  # Palvelimen osoite (esim. "127.0.0.1" paikallisessa käytössä)
    "user": "",  # Tietokannan käyttäjänimi
    "password": "",  # Tietokannan salasana
    "database": "flight_game"  # Käytettävä tietokanta
}


def hae_lentokentan_tiedot(icao):
    """
    Hakee lentokentän nimen ja kaupungin ICAO-koodin perusteella tietokannasta.

    :param icao: ICAO-koodi (merkkijono), joka yksilöi lentokentän.
    :return: JSON-objekti, jossa on lentokentän nimi ja sen sijaintikunta,
             tai virheilmoitus, jos kenttää ei löydy.
    """
    try:
        # Luodaan yhteys MariaDB-tietokantaan
        yhteys = mariadb.connect(**DB_CONFIG)
        kursori = yhteys.cursor()

        # Suoritetaan SQL-kysely lentokenttätietojen hakemiseksi
        kursori.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao,))
        rivi = kursori.fetchone()  # Haetaan ensimmäinen tulos

        # Suljetaan tietokantayhteys
        kursori.close()
        yhteys.close()

        # Jos kenttä löytyi, palautetaan tiedot JSON-muodossa
        if rivi:
            return {"ICAO": icao, "Name": rivi[0], "Municipality": rivi[1]}
        else:
            return {"error": "Lentokenttää ei löydy"}

    except mariadb.Error as e:
        # Palautetaan virheilmoitus, jos tietokantayhteydessä tapahtuu virhe
        return {"error": f"Tietokantavirhe: {str(e)}"}


@app.route('/kenttä/<string:icao>', methods=['GET'])
def hae_kentta(icao):
    """
    Flask-reitti, joka hakee annetun ICAO-koodin perusteella lentokentän tiedot.

    :param icao: ICAO-koodi (merkkijono).
    :return: JSON-objekti, jossa lentokentän tiedot tai virheilmoitus.
    """
    return jsonify(hae_lentokentan_tiedot(icao))  # Palautetaan haetut tiedot JSON-formaatissa


# Käynnistetään Flask-palvelin
if __name__ == '__main__':
    app.run(debug=True, port=3000)  # Flask toimii debug-tilassa portissa 3000
