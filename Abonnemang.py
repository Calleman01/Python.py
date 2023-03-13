min = int(input("Hur många minuter ringer du per månad? :"))
if min < 33:
    print("Välj Kontantkort")
if min >= 33 and min < 66:
    print("Välj Normal")
if min >= 66: 
    print("Välj Plus")
