Å = int(input("Pris för årskort?: "))
B = int(input("Pris för biljett?: "))
A = int(input("Antal besök?"))
if B * A <= Å:
    print("Köp biljett!")
elif B * A > Å:
    print("Köp Årskort!")

