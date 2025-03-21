import requests  # Tuodaan requests-kirjasto HTTP-pyyntöjen tekemiseen

def hae_chuck_norris_vitsi():
    """
    Hakee satunnaisen Chuck Norris -vitsin API:sta ja tulostaa sen.
    Jos pyyntö epäonnistuu, tulostetaan virheilmoitus.
    """
    url = "https://api.chucknorris.io/jokes/random"  # API-osoite, josta haetaan vitsi
    try:
        vastaus = requests.get(url)  # Lähetetään GET-pyyntö API:lle
        vastaus.raise_for_status()  # Tarkistetaan, että vastaus on onnistunut (statuskoodi 200)
        data = vastaus.json()  # Muutetaan JSON-muotoinen vastaus Pythonin sanakirjaksi
        print("Chuck Norris -vitsi:")  # Tulostetaan otsikko
        print(data["value"])  # Tulostetaan vitsin teksti
    except requests.exceptions.RequestException as e:
        print("Virhe haettaessa vitsiä:", e)  # Tulostetaan mahdollinen virheilmoitus

# Käynnistetään ohjelma
if __name__ == "__main__":
    hae_chuck_norris_vitsi()  # Kutsutaan funktiota, joka hakee ja tulostaa vitsin
