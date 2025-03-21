class Hissi:
    """
    Hissi-luokka edustaa hissiä, joka liikkuu alimman ja ylimmän kerroksen välillä.
    """

    def __init__(self, alin_kerros, ylin_kerros):
        """
        Alustaa uuden hissin.

        :param alin_kerros: Hissin alin mahdollinen kerros (kokonaisluku).
        :param ylin_kerros: Hissin ylin mahdollinen kerros (kokonaisluku).
        """
        self.alin_kerros = alin_kerros  # Määritetään alin kerros
        self.ylin_kerros = ylin_kerros  # Määritetään ylin kerros
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
        Siirtää hissin haluttuun kerrokseen kutsumalla kerros_ylos- ja kerros_alas-metodeja.

        :param kohde_kerros: Kerros, johon hissi halutaan siirtää.
        """
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()


# Pääohjelma
if __name__ == "__main__":
    # Luodaan hissi, jonka alin kerros on 1 ja ylin kerros on 10
    testihissi = Hissi(1, 10)

    # Siirretään hissi viidenteen kerrokseen
    print("\nSiirretään hissi viidenteen kerrokseen:")
    testihissi.siirry_kerrokseen(5)

    # Siirretään hissi takaisin alimpaan kerrokseen
    print("\nSiirretään hissi takaisin alimpaan kerrokseen:")
    testihissi.siirry_kerrokseen(1)
