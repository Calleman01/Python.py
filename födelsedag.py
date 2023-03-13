import datetime
personnummer = input("Skriv ditt personnummer ÅÅMMDDNNNN: ")
födelsedag = personnummer[:6]
idag = datetime.datetime.now().strftime()
if födelsedag == idag:
    print("Grattis!")
else:
    print("Du fyller inte år idag. ")
