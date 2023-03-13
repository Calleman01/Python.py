rader = int(input("Hur många rader: "))
for i in range(1, rader+1):
    for j in range(1, rader+1):
        print(f"{i*j:4d}", end="")
    print()