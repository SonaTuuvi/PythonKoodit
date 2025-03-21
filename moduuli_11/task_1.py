class Julkaisu:
    """
    Julkaisu-luokka on yliluokka, joka edustaa yleistä julkaisua.
    """

    def __init__(self, nimi):
        """
        Alustaa julkaisun nimen.

        :param nimi: Julkaisun nimi (merkkijono).
        """
        self.nimi = nimi

    def tulosta_tiedot(self):
        """
        Tulostaa julkaisun tiedot.
        Tämä metodi voidaan korvata aliluokissa.
        """
        print(f"Julkaisu: {self.nimi}")


class Kirja(Julkaisu):
    """
    Kirja-luokka perii Julkaisu-luokan ja edustaa kirjaa, jolla on kirjoittaja ja sivumäärä.
    """

    def __init__(self, nimi, kirjoittaja, sivumaara):
        """
        Alustaa kirjan nimen, kirjoittajan ja sivumäärän.

        :param nimi: Kirjan nimi (merkkijono).
        :param kirjoittaja: Kirjan kirjoittaja (merkkijono).
        :param sivumaara: Kirjan sivumäärä (kokonaisluku).
        """
        super().__init__(nimi)  # Kutsutaan yliluokan konstruktoria
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        """
        Tulostaa kirjan tiedot, mukaan lukien kirjoittajan ja sivumäärän.
        """
        print(f"Kirja: {self.nimi}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumaara}\n")


class Lehti(Julkaisu):
    """
    Lehti-luokka perii Julkaisu-luokan ja edustaa lehteä, jolla on päätoimittaja.
    """

    def __init__(self, nimi, paatoimittaja):
        """
        Alustaa lehden nimen ja päätoimittajan.

        :param nimi: Lehden nimi (merkkijono).
        :param paatoimittaja: Lehden päätoimittaja (merkkijono).
        """
        super().__init__(nimi)  # Kutsutaan yliluokan konstruktoria
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        """
        Tulostaa lehden tiedot, mukaan lukien päätoimittajan.
        """
        print(f"Lehti: {self.nimi}\nPäätoimittaja: {self.paatoimittaja}\n")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan Lehti- ja Kirja-oliot
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti_no6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    # Tulostetaan molempien julkaisujen tiedot
    aku_ankka.tulosta_tiedot()
    hytti_no6.tulosta_tiedot()
