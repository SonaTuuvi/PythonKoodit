# ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan

class Authenticator:

    def __init__(self, username, password, max_attempts=5):
        self.correct_username = username  # Oikea käyttäjätunnus
        self.correct_password = password  # Oikea salasana
        self.max_attempts = max_attempts  # Maksimiyritysten määrä
        self.attempts = 0  # Yritysten laskuri

    def authenticate(self):
        while self.attempts < self.max_attempts:  # Jatka, kunnes yritykset täyttyvät

            print(f"Yritys {self.attempts + 1}. Simulla on vielä  {self.max_attempts - self.attempts - 1} yritystä jäljellä.")  # Tulostetaan yritysten määrä

            username = input("Anna käyttäjätunnus: ")  # Pyydetään käyttäjätunnus
            password = input("Anna salasana: ")  # Pyydetään salasana

            if username == self.correct_username and password == self.correct_password:
                print("Tervetuloa!")  # Onnistunut kirjautuminen
                return True

            print("Virheellinen käyttäjätunnus tai salasana.")  # Virheellinen kirjautuminen
            self.attempts += 1  # Lisätään yrityslaskuria

        print("Pääsy evätty.")  # Liian monta yritystä
        return False


if __name__ == "__main__":
    auth = Authenticator(username="python", password="rules")  # Luodaan Authenticator-olio
    auth.authenticate()  # Suoritetaan kirjautumisprosessi


