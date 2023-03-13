
import math
Radie = int(input("Vad är Radien: "))
if Radie > 0:
    o = 2 * math.pi * Radie
    a = math.pi * Radie**2
    print(f'Omkrets: {o:.3f}')
    print(f'Area: {a:.3f}')
else:
    print("Radien kan ej vara 0")


