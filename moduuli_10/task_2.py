class Hissi:
    """
    Hissi-luokka edustaa hissiä, joka voi liikkua tietyn rakennuksen kerrosten välillä.
    """

    def __init__(self, alin_kerros, ylin_kerros):
        """
        Alustaa hissin ja asettaa sen alimpaan kerrokseen.

        :param alin_kerros: Rakennuksen alin kerros (kokonaisluku).
        :param ylin_kerros: Rakennuksen ylin kerros (kokonaisluku).
        """
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros  # Hissi alkaa alimmasta kerroksesta

    def kerros_ylos(self):
        """
        Siirtää hissiä yhden kerroksen ylöspäin, jos se ei ole jo ylimmässä kerroksessa.
        """
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi siirtyi kerrokseen {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        """
        Siirtää hissiä yhden kerroksen alaspäin, jos se ei ole jo alimmassa kerroksessa.
        """
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi siirtyi kerrokseen {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde_kerros):
        """
        Siirtää hissin haluttuun kerrokseen kutsumalla kerros_ylös- ja kerros_alas-metodeja.

        :param kohde_kerros: Kerros, johon hissi halutaan siirtää.
        """
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

    def palaa_alimpaan_kerrokseen(self):
        """
        Palauttaa hissin alimpaan kerrokseen.
        """
        print("Hissi palaa alimpaan kerrokseen...")
        while self.nykyinen_kerros > self.alin_kerros:
            self.kerros_alas()


class Talo:
    """
    Talo-luokka sisältää useita hissejä ja tarjoaa metodeja niiden käyttämiseen.
    """

    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        """
        Alustaa talon ja luo määritellyn määrän hissejä.

        :param alin_kerros: Rakennuksen alin kerros (kokonaisluku).
        :param ylin_kerros: Rakennuksen ylin kerros (kokonaisluku).
        :param hissien_lukumäärä: Kuinka monta hissiä talossa on.
        """
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lukumäärä)]

    def aja_hissia(self, hissin_numero, kohde_kerros):
        """
        Ajaa valittua hissiä haluttuun kerrokseen.

        :param hissin_numero: Hissin numero (1-pohjainen numerointi).
        :param kohde_kerros: Kerros, johon hissi halutaan siirtää.
        """
        hissin_indeksi = hissin_numero - 1  # Muutetaan hissin numerointi alkamaan 1:stä
        if 0 <= hissin_indeksi < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero} kerrokseen {kohde_kerros}")
            self.hissit[hissin_indeksi].siirry_kerrokseen(kohde_kerros)
            # Palautetaan hissi takaisin alimpaan kerrokseen
            self.hissit[hissin_indeksi].palaa_alimpaan_kerrokseen()
        else:
            print("Virheellinen hissinumero.")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan talo, jossa on 3 hissiä ja kerrokset 1-10
    talo = Talo(1, 10, 3)

    # Ajetaan eri hissejä eri kerroksiin ja palautetaan ne takaisin alimpaan kerrokseen
    print("\n--- Ajetaan ensimmäistä hissiä ---")
    talo.aja_hissia(1, 5)  # Ensimmäinen hissi viidenteen kerrokseen ja takaisin

    print("\n--- Ajetaan toista hissiä ---")
    talo.aja_hissia(2, 8)  # Toinen hissi kahdeksanteen kerrokseen ja takaisin

    print("\n--- Ajetaan kolmatta hissiä ---")
    talo.aja_hissia(3, 3)  # Kolmas hissi kolmanteen kerrokseen ja takaisin
