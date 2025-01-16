vuosi = int(input("Anna kysyy vuosiluku? "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(f"Vuosi {vuosi} on karkausvuosi.")
else:
    print(f"Vuosi {vuosi} ei ole karkausvuosi.")