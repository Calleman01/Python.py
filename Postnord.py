b = int(input("Hur brett är ditt paket? Svara i mm: "))
l = int(input("Hur långt är ditt paket? Svara i mm: "))
t = int(input("Hur tjockt är ditt paket? Svara i mm: "))
if b+l+t >= 140 and b+l+t <= 900:
    print("Ok mått")
else:
    print("Felaktiga mått")

