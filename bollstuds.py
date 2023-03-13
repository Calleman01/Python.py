while True:
    resultat = int(input("Vilken höjd (Meter) släpps bollen ifrån?: "))
    i = 0
    while resultat > 0.01:
        resultat = resultat * 0.7
        i = i + 1
    print(f'Den studsar {i}')
    if resultat < 0:
        break
