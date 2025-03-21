import random


class Auto:
    """
    Auto-luokka edustaa autoa, jolla on rekisteritunnus, huippunopeus,
    tämänhetkinen nopeus ja kuljettu matka.
    """

    def __init__(self, rekisteritunnus, huippunopeus):
        """
        Alustaa uuden Auto-olion.

        :param rekisteritunnus: Auton rekisteritunnus (merkkijono).
        :param huippunopeus: Auton huippunopeus km/h (kokonaisluku tai liukuluku).
        """
        self.rekisteritunnus = rekisteritunnus  # Asetetaan rekisteritunnus
        self.huippunopeus = huippunopeus  # Asetetaan huippunopeus
        self.nopeus = 0  # Aluksi auton nopeus on 0 km/h
        self.kuljettu_matka = 2000  # Alustetaan kuljettu matka (esim. 2000 km)

    def __str__(self):
        """
        Palauttaa Auto-olion merkkijonoesityksen.

        :return: Auton tiedot merkkijonona.
        """
        return (f"Auto: {self.rekisteritunnus}\n"
                f"Huippunopeus: {self.huippunopeus} km/h\n"
                f"Tämänhetkinen nopeus: {self.nopeus} km/h\n"
                f"Kuljettu matka: {self.kuljettu_matka} km")

    def kiihdyta(self, muutos):
        """
        Muuttaa auton nopeutta annetulla määrällä.

        :param muutos: Nopeuden muutos (positiivinen = kiihdytys, negatiivinen = hidastus).
        """
        self.nopeus += muutos  # Lisätään nopeuden muutos
        if self.nopeus > self.huippunopeus:  # Tarkistetaan, ettei ylitetä huippunopeutta
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:  # Nopeus ei voi olla negatiivinen
            self.nopeus = 0

    def kulje(self, tuntimäärät):
        """
        Lisää kuljettua matkaa nykyisen nopeuden perusteella.

        :param tuntimäärät: Aika (tuntia), jonka auto liikkuu.
        """
        self.kuljettu_matka += self.nopeus * tuntimäärät  # Päivitetään kuljettu matka


# Pääohjelma
if __name__ == "__main__":
    # Luodaan lista 10 auto-oliosta
    autot = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

    kilpailu_kaynnissa = True
    while kilpailu_kaynnissa:
        for auto in autot:
            # Arvotaan nopeuden muutos (-10 ja +15 km/h välillä)
            auto.kiihdyta(random.randint(-10, 15))
            # Auto liikkuu yhden tunnin ajan
            auto.kulje(1)
            # Tarkistetaan, onko jokin auto saavuttanut 10 000 km
            if auto.kuljettu_matka >= 10000:
                kilpailu_kaynnissa = False
                break

    # Järjestetään autot kuljetun matkan mukaan (voittaja ensin, hävinnyt viimeisenä)
    autot.sort(key=lambda x: x.kuljettu_matka, reverse=True)

    # Tulostetaan kaikkien autojen tiedot taulukkomuodossa
    print("{:<10} {:<15} {:<20} {:<15}".format("Rek.Tunnus", "Huippunopeus", "Tämänhetkinen nopeus", "Kuljettu matka"))
    print("-" * 60)
    for auto in autot:
        print("{:<10} {:<15} {:<20} {:<15}".format(auto.rekisteritunnus, auto.huippunopeus, auto.nopeus,
                                                   auto.kuljettu_matka))
