import math 
a = float(input("Längden för första sidan?: "))
b = float(input("Längden för andra sidan?: "))
v = float(input("Vinkeln mellan sidorna?: "))
if a < 0:
    exit()
elif b < 0:
    exit()
alfa = v * 2 * math.pi / 360
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(alfa))
if c == a == b:
    print("Triangeln är liksidig")
elif c == a or b == c or a == b:
    print("Triangeln är likbent")
else: 
    print("Triangeln är oliksidig")
