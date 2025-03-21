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
    # Luodaan uusi Auto-olio rekisteritunnuksella "ABC-123" ja huippunopeudella 142 km/h
    auto = Auto("ABC-123", 142)

    # Kiihdytetään autoa useita kertoja
    auto.kiihdyta(30)  # +30 km/h
    auto.kiihdyta(70)  # +70 km/h
    auto.kiihdyta(50)  # +50 km/h (pitäisi rajoittua 142 km/h)
    print(f"Nopeus kiihdytyksen jälkeen: {auto.nopeus} km/h")  # Tulostetaan nopeus

    # Hätäjarrutus (nopeuden pitäisi mennä 0 km/h)
    auto.kiihdyta(-200)
    print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")  # Nopeuden pitäisi olla 0 km/h

    # Ajetaan 1.5 tuntia nopeudella 60 km/h
    auto.kiihdyta(60)  # Nostetaan nopeus esim. 60 km/h
    print(f"Kuljettu matka ennen ajoa: {auto.kuljettu_matka} km")  # Tulostetaan matkamittarin lukema
    auto.kulje(1.5)  # Auto liikkuu 1.5 tuntia nykyisellä nopeudella
    print(f"Kuljettu matka ajon jälkeen: {auto.kuljettu_matka} km")  # Päivitetty matka
