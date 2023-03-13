antal_dagar = 1
dagens_lön = 0.01
total_belopp = 0.01
while total_belopp < 10000000:
    antal_dagar += 1
    dagens_lön *= 2
    total_belopp = total_belopp + dagens_lön 
print(f'Du måste arbeta {antal_dagar} dagar')