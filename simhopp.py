antal = int(input("Ange antal domare: "))
if antal < 3:
    print("Felaktigt antal domare försök igen: ")
elif antal > 3:
    while True:
        svårighet = float(input("Hoppets svårighetsgrad?: "))
        if svårighet < 0:
            exit()
        sum = 0 
        max_poäng = 10
        min_poäng = 0 
        for i in range(1, antal + 1):
            poäng = float(input("Domarpoäng för domare nr {i}: "))
            if poäng < 0:
                exit()
            sum += poäng
            min_poäng = min(min_poäng, poäng)
            max_poäng = max(max_poäng, poäng)
        sum = sum - min_poäng - max_poäng
        hopp_poäng = sum / (antal-2) * 3 * svårighet
        print(f'Hoppets poäng: {hopp_poäng:.3f}')


