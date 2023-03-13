


s = input("Skriv en text: ")
for i in range(0, len(s)):
    if s[i] == ' ' or s[i] == '\t':
        print(f'Det första vita tecknet finns på {i:d}')
        break
else: 
    print("Det finns inga vita tal")