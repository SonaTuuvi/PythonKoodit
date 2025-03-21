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
        self.kuljettu_matka = 0  # Auto ei ole vielä kulkenut yhtään matkaa

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


class Kilpailu:
    """
    Kilpailu-luokka hallinnoi autokilpailua, jossa useat autot ajavat
    määritetyn matkan ja voittaja on ensimmäisenä maalissa.
    """

    def __init__(self, nimi, pituus, autot):
        """
        Alustaa kilpailun.

        :param nimi: Kilpailun nimi (merkkijono).
        :param pituus: Kilpailun kokonaispituus kilometreinä (kokonaisluku).
        :param autot: Lista kilpailuun osallistuvista autoista (Auto-olioita).
        """
        self.nimi = nimi  # Tallennetaan kilpailun nimi
        self.pituus = pituus  # Tallennetaan kilpailun pituus km
        self.autot = autot  # Lista kilpailuun osallistuvista autoista

    def tunti_kuluu(self):
        """
        Simuloi yhden kilpailutunnin kulumista.
        Jokaisen auton nopeutta muutetaan satunnaisesti ja ne liikkuvat yhden tunnin ajan.
        """
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))  # Muutetaan auton nopeutta satunnaisesti
            auto.kulje(1)  # Auto liikkuu yhden tunnin ajan

    def tulosta_tilanne(self):
        """
        Tulostaa kaikkien autojen sen hetkisen tilanteen taulukkomuodossa.
        """
        # Järjestetään autot kuljetun matkan mukaan (voittaja ensin)
        self.autot.sort(key=lambda x: x.kuljettu_matka, reverse=True)

        print("{:<10} {:<15} {:<20} {:<15}".format(
            "Rek.Tunnus", "Huippunopeus", "Tämänhetkinen nopeus", "Kuljettu matka"
        ))
        print("-" * 60)
        for auto in self.autot:
            print("{:<10} {:<15} {:<20} {:<15}".format(
                auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka
            ))
        print("\n")

    def kilpailu_ohi(self):
        """
        Tarkistaa, onko jokin auto saavuttanut kilpailun maaliviivan.
        :return: True, jos kilpailu on päättynyt, muuten False.
        """
        return any(auto.kuljettu_matka >= self.pituus for auto in self.autot)


# Pääohjelma
if __name__ == "__main__":
    # Luodaan lista 10 auto-oliosta satunnaisilla huippunopeuksilla
    autot = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

    # Luodaan 8000 km pitkä kilpailu nimeltä "Suuri romuralli"
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0  # Kilpailun aikamittari (tunnit)
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()  # Simuloidaan yhden tunnin kuluminen
        tunti += 1
        if tunti % 10 == 0:  # Tulostetaan tilanne 10 tunnin välein
            print(f"--- Tilanne {tunti} tunnin jälkeen ---")
            kilpailu.tulosta_tilanne()


     # Kun kilpailu päättyy, tulostetaan lopputulokset
    print("\n--- KILPAILU PÄÄTTYI! LOPPUTULOKSET ---")
    kilpailu.tulosta_tilanne()
