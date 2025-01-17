#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
import random

def guess_number():
    number = random.randint(1,10) # Tietokone arpoo satunnaisen kokonaisluvun väliltä 1..10

    while True: # Jatketaan silmukkaa, kunnes pelaaja arvaa oikein
        guess = int(input("Arvaa luku (1-10): "))  # Pyydetään pelaajalta arvausta

        if guess < number:  # Tarkistetaan, onko arvaus liian pieni
            print("Liian pieni arvaus.")
        elif guess > number:  # Tarkistetaan, onko arvaus liian suuri
            print("Liian suuri arvaus.")
        else:  # Jos arvaus on oikea
            print("Oikein! Onneksi olkoon!")
            break  # Lopetetaan silmukka, koska pelaaja arvasi oikein

# Käynnistetään peli
if __name__ == "__main__":
    guess_number()  # Kutsutaan peliä varten määriteltyä funktiota
