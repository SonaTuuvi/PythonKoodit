class Auto:
    """
    Auto-luokka toimii yliluokkana kaikille ajoneuvoille.
    Se sisältää rekisteritunnuksen, huippunopeuden, nykyisen nopeuden ja kuljetun matkan.
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


class Sähköauto(Auto):
    """
    Sähköauto-luokka perii Auto-luokan ja lisää akkukapasiteettiominaisuuden.
    """

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        """
        Alustaa sähköauton ja määrittää akkukapasiteetin.

        :param rekisteritunnus: Auton rekisteritunnus (merkkijono).
        :param huippunopeus: Auton huippunopeus km/h (kokonaisluku tai liukuluku).
        :param akkukapasiteetti: Akkukapasiteetti kWh (liukuluku).
        """
        super().__init__(rekisteritunnus, huippunopeus)  # Kutsutaan yliluokan konstruktoria
        self.akkukapasiteetti = akkukapasiteetti  # Tallennetaan akkukapasiteetti


class Polttomoottoriauto(Auto):
    """
    Polttomoottoriauto-luokka perii Auto-luokan ja lisää bensatankin ominaisuuden.
    """

    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        """
        Alustaa polttomoottoriauton ja määrittää bensatankin koon.

        :param rekisteritunnus: Auton rekisteritunnus (merkkijono).
        :param huippunopeus: Auton huippunopeus km/h (kokonaisluku tai liukuluku).
        :param bensatankin_koko: Bensatankin koko litroina (liukuluku).
        """
        super().__init__(rekisteritunnus, huippunopeus)  # Kutsutaan yliluokan konstruktoria
        self.bensatankin_koko = bensatankin_koko  # Tallennetaan bensatankin koko


# Pääohjelma
if __name__ == "__main__":
    # Luodaan sähköauto ja polttomoottoriauto
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    # Asetetaan nopeudet
    sahkoauto.kiihdyta(100)  # Sähköauton nopeus nostetaan 100 km/h
    polttomoottoriauto.kiihdyta(120)  # Polttomoottoriauton nopeus nostetaan 120 km/h

    # Ajetaan 3 tuntia
    sahkoauto.kulje(3)
    polttomoottoriauto.kulje(3)

    # Tulostetaan matkamittarilukemat
    print(f"Sähköauton kuljettu matka: {sahkoauto.kuljettu_matka} km")
    print(f"Polttomoottoriauton kuljettu matka: {polttomoottoriauto.kuljettu_matka} km")
