import mariadb
from geopy.distance import geodesic

conn = mariadb.connect(
    host="****",# anna host
    user="****",# anna user nimi
    password="****",#anna salasana
    database="flight_game"
)

cursor = conn.cursor()

# Lentokentän nimen ja sijaintikunnan haku ICAO-koodilla
def hae_lentoasema():
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao,))
    tulos = cursor.fetchone()
    if tulos:
        print(f"Lentoasema: {tulos[0]}, Sijaintikunta: {tulos[1]}")
    else:
        print("Lentoasemaa ei löytynyt.")

hae_lentoasema()