import requests  # Tuodaan requests-kirjasto HTTP-pyyntöjen tekemiseen


def hae_saa(paikkakunta, api_avain):
    """
    Hakee OpenWeather API:sta säätilan ja lämpötilan annetulle paikkakunnalle.

    :param paikkakunta: Kaupungin nimi (merkkijono), jonka säätiedot haetaan.
    :param api_avain: OpenWeather API-avain (merkkijono).
    """
    # Rakennetaan API-pyyntö
    url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}&units=metric&lang=fi"

    try:
        vastaus = requests.get(url)  # Lähetetään GET-pyyntö API:lle
        print("API-vastaus:", vastaus.json())  # Tulostetaan koko API-vastaus (debuggausta varten)

        vastaus.raise_for_status()  # Tarkistetaan, että pyyntö onnistui (statuskoodi 200)
        data = vastaus.json()  # Muutetaan JSON-muotoinen vastaus Pythonin sanakirjaksi

        # Haetaan säätiedot vastauksesta
        saakuvaus = data["weather"][0]["description"].capitalize()  # Kuvaus säästä (esim. "Pilvistä")
        lampotila = data["main"]["temp"]  # Lämpötila Celsius-asteina

        # Tulostetaan säätiedot
        print(f"Sää paikkakunnalla {paikkakunta}: {saakuvaus}")
        print(f"Lämpötila: {lampotila}°C")

    except requests.exceptions.RequestException as e:
        print("Virhe haettaessa säätietoja:", e)  # Tulostetaan mahdollinen virheilmoitus


# Käynnistetään ohjelma
if __name__ == "__main__":
    api_avain = ""  # 🔹 Korvaa tämä omalla OpenWeather API-avaimellasi ennen suorittamista!
    paikkakunta = input("Anna paikkakunnan nimi: ")  # Käyttäjä syöttää paikkakunnan
    hae_saa(paikkakunta, api_avain)  # Haetaan ja tulostetaan säätiedot
