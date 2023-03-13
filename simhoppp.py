a = int(input("Antalet domare: "))
if a < 3:
    exit()
while True: 
    svårighetsgrad = float(input("Hoppets svårighetsgrad: "))
    sum = 0 
    min_poäng = 10
    max_poäng = 0
    for i in range(1, a+1):
        domarpoäng = float(input(f'Poäng från domare {i} '))
        if i < 0:
            exit()
        sum += domarpoäng
        min_poäng = min(min_poäng, domarpoäng)
        max_poäng = max(max_poäng, domarpoäng)
    sum = sum - min_poäng - max_poäng
    hopp_poäng = sum / (a-2) * 3 * svårighetsgrad
    print(f'Hoppets poäng {hopp_poäng:.3f}')


