t = float(input("Temp?: "))
if t < 18:
    print("Det är kallt")
    print("Sätt på värmen")
    if t < 12 and t >=6:
        print("Sätt på jackan")
else :
    print("Det är varmt")
    if t >= 22 and t <=35:
        print("Stäng av värmen")
if t <6:
    print("Svinkallt") 
if t >35:
    print("Ökenhett")
print(f'Det är {t:.1f} grader')