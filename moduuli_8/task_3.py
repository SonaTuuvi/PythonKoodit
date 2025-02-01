import mariadb
from geopy.distance import geodesic

# Yhdistä tietokantaan
conn = mariadb.connect(
    host="****",# anna host
    user="****",# anna user nimi
    password="****",#anna salasana
    database="flight_game"
)
cursor = conn.cursor()  # Luo kursori tietokantakyselyjä varten

# Lentokenttien välisen etäisyyden laskeminen
def laske_etaisyys():
    icao1 = input("Syötä ensimmäisen lentoaseman ICAO-koodi: ")
    icao2 = input("Syötä toisen lentoaseman ICAO-koodi: ")
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao1,))
    paikka1 = cursor.fetchone()
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao2,))
    paikka2 = cursor.fetchone()
    if paikka1 and paikka2:
        etaisyys = geodesic((paikka1[0], paikka1[1]), (paikka2[0], paikka2[1])).kilometers
        print(f"Lentokenttien välinen etäisyys on {etaisyys:.2f} km")
    else:
        print("Jompaakumpaa lentoasemaa ei löytynyt tietokannasta.")

laske_etaisyys()