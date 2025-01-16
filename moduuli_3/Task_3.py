# Kysytään käyttäjältä sukupuoli ja hemoglobiiniarvo
sukupuoli = input("Anna biologinen sukupuolesi (nainen/mies): ").strip().lower()
hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= hemoglobiini <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
else:
    print("Virheellinen sukupuoli.")


