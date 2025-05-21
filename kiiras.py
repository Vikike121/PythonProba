import random

ellenfel = input("Gép vagy játékos ellen játszol? (g, j): ")

sajatlap1 = random.randint(2, 11)
sajatlap2 = random.randint(2, 11)

if ellenfel == "g":
    geplap1 = random.randint(2, 11)
    geplap2 = random.randint(2, 11)
    print(f"A gép lapjai: {geplap1}, {geplap2}")
    gep_osszeg = geplap1 + geplap2
    if gep_osszeg > 21:
        print("A gép vesztett!")
    elif sajatlap1 + sajatlap2 > gep_osszeg:
        print("Te nyertél!")
    elif sajatlap1 + sajatlap2 < gep_osszeg:
        print("A gép nyert!")
    else:
        print("Döntetlen!")

else:
    jatekoslap1 = random.randint(2, 11)
    jatekoslap2 = random.randint(2, 11)
    print(f"A másik játékos lapjaii: {jatekoslap1}, {jatekoslap2}")
    jatekos_osszeg = jatekoslap1 + jatekoslap2
    if jatekos_osszeg > 21:
        print("A másik játékos vesztett!")
    elif sajatlap1 + sajatlap2 > jatekos_osszeg:
        print("Te nyertél!")
    elif sajatlap1 + sajatlap2 < jatekos_osszeg:
        print("A másik játékos nyert!")
    else:
        print("Döntetlen!")
