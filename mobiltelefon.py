minuter = int(input("Hur många minuter ringer du per månad?: "))
if minuter < 33:
    print("Välj kontant")
elif minuter >= 33 and minuter < 66:
    print("Välj Normal")
elif minuter >= 66:
    print("Välj plus")