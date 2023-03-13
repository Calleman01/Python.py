import math
år = int(input("Skriv vilket årtal: "))
folkmängd = 26_000
for i in range(2020, år+1):
    folkmängd = folkmängd + math.ceil(300 - 325 + folkmängd*(0.7-0.6)/100)
print(f'Beräknad folkmängd {folkmängd}')
