personnummer = input("Skriv ditt peronnummer (ÅÅMMDDNNNN): ")
if personnummer[-2] == 1 or 3 or 5 or 7 or 9:
    print("Du är en kille")
else:
    print("Du är en tjej")