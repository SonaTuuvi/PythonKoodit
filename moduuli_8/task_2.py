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

# Lentokenttien lukumäärät tyypeittäin
def laske_lentokentat():
    maakoodi = input("Syötä maakoodi (esim. FI): ")
    cursor.execute("SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type", (maakoodi,))
    tulokset = cursor.fetchall()
    print(f"Lentokenttien lukumäärät maassa {maakoodi} tyypeittäin:")
    for tyyppi, maara in tulokset:
        print(f"{tyyppi}: {maara} kappaletta")

laske_lentokentat()