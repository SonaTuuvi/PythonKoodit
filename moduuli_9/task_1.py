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
        self.kuljettu_matka = 0  # Aluksi autolla ei ole ajettua matkaa

    def __str__(self):
        """
        Palauttaa Auto-olion merkkijonoesityksen.

        :return: Auton tiedot merkkijonona.
        """
        return (f"Auto: {self.rekisteritunnus}\n"
                f"Huippunopeus: {self.huippunopeus} km/h\n"
                f"Tämänhetkinen nopeus: {self.nopeus} km/h\n"
                f"Kuljettu matka: {self.kuljettu_matka} km")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan uusi Auto-olio rekisteritunnuksella "ABC-123" ja huippunopeudella 142 km/h
    auto = Auto("ABC-123", 142)

    # Tulostetaan auton tiedot __str__-metodin avulla
    print(auto)
