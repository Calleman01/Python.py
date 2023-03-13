kpi_10 = [['År', 'Jan', 'Feb', 'Mar', 'Apr', 'Maj', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'], ['2019', '328.56', '331.02', '331.79', '334.11', '334.95', '334.47', '335.8', '334.39', '335.95', '336.04', '336.36', '337.68'], ['2018', '322.51', '324.87', '325.76', '327.1', '327.86', '328.62', '330.33', '329.63', '331.14', '330.72', '330.4', '331.87'], ['2017', '317.5', '319.73', '319.68', '321.54', '321.74', '321.97', '323.69', '323.18', '323.62', '323.38', '324.04', '325.23'], ['2016', '313.13', '314.14', '315.7', '315.64', '316.21', '316.54', '316.73', '316.38', '316.91', '318', '318.1', '319.68'], ['2015', '310.75', '312.93', '313.19', '313.16', '314.24', '313.33', '313.43', '312.81', '314.06', '314.29', '313.75', '314.21'], ['2014', '311.39', '312.7', '312.68', '313.89', '314.05', '314.7', '313.67', '313.35', '313.85', '314.02', '313.56', '314.05'], ['2013', '312', '313.39', '314.65', '314.03', '314.54', '313.99', '313.55', '313.84', '315.05', '314.4', '314.2', '315.04'], ['2012', '311.85', '313.92', '314.8', '315.49', '315.23', '314.45', '313.23', '313.55', '314.81', '314.59', '313.82', '314.61'], ['2011', '306.15', '308.02', '310.11', '311.44', '312.02', '311.28', '311.13', '311.23', '313.41', '313.42', '314.16', '314.78'], ['2010', '299.79', '301.59', '302.32', '302.36', '302.92', '302.97', '302.04', '302.06', '304.6', '305.57', '306.58', '308.73']]

def print_kpi_10(): #Skriver ut listan kpi_10

    print('\nHela kpi_10\n') 
    print(kpi_10) # Skriver ut hela listan i en utskrift utan radbrytning för varje rad

    print('\nkpi_10 radvis\n')
    for row in kpi_10: # Skriver ut hela listan med radbrytning för varje rad
        print(row)

# Skriv din kod här:

print("Meny: ")
print("Val 1: Skriv ut listan")
print("Val 2: Beräkna summa")
print("Val 3: Beräkna medelvärdet")
print("Val 4: Hitta största värdet")
print("val 5: Hitta minsta värdet")
print("Val 6: Avsluta")

def skriv_ut(): #Definierar en ny tom lista "skriv_ut" som innehåller en loop.
    for x in kpi_10:
        print(x)

def summa(st): #Definierar en ny tom lista "summa" med argumentet "st". 
    result = [] 
    for row in st[1:]: #Initerar en 2D-lista "st" samt utför en åtgärd för varje rad i listan. 
        sum = 0 #Sätter summan till 0. 
        for value in row[1:]: #Används för att loopa över varje element i listan row, från det andra elementet till slutet. 
            sum += float(value) #Finns för att summera talen i loopen. 
        print([row[0], sum]) 
   

def mean_list(a_list): #Skapar en kopia av och beräknar medelvärder radvis för en 2D-lista.
    #Argument : En 2D-lista med rubriker i första raden och första kolumnen att kopiera och beräkna.
    #Returparameter : En kopia av ursprungslistan med en extra kolumn med medelvärden sist i listan. 
    new_list = [] #Definierar en ny tom lista med namnet "new_list"
    for i, row in enumerate (a_list): #Används för att iterera över en lista a_list och hämta både indexet och värdet för varje element i listan samtidigt.
        temp_list = [] #Definierar en ny tom lista med namnet "temp_list"
        for kolumn in row: #Loopar över varje kolumn i raden.
            temp_list.append(kolumn) #Lägger till "medelvärde" i "temp_list".
        if i == 0: #En if sats som skriver textsträng "Medelvärde" i "temp_list", när i = 0. 
            temp_list.append("Medelvärde") #Lägger till "Medelvärde" i den temporära listan. 
        else: 
            x = 0 #Skapar en variabel för att räkna summan av värdena i raden. 
            for value in temp_list[1:]: #Loopar över varje varje element i "temp_list" utom det frösta elementet. 
                x += float(value) #Adderar värdet i elementet till summan.
            means = x/(len(temp_list)-1) #Beräknar medelvärdet för raden. 
            temp_list.append(round(means,2)) #Lägger till medelvärdet i "temp_list".
            print([row[0], means]) #Skriver ut årtal samt medelvärdet. 
        new_list.append(temp_list)

    
def max_rows(st): #Definierar en ny tom lista "max_rows" med argumentet "st".
    for row in st[1:]: #Finns för att initiera en 2D-lista "st" samt utföra en åtgärd för varje rad i listan. 
        max_value = float(row[1]) #Sätt det första värdet i raden som max-värdet
        for value in row[2:]: #Loopa över varje element i raden förutom den första.
            max_value = max(max_value, float(value)) #Max-värdet uppdateras ifall det hittas ett större. 
        print([row[0], max_value]) #Skriver ut årtal samt max-värdet. 


def min_rows(st): #Definierar en ny tom lista "min_rows" med argumentet "st".
    for row in st[1:]: #Finns för att initera en 2D-lista "st" samt utföra en åtgärd för varje rad i listan. 
        min_value = float(row[1]) #Sätt det första värdet i raden som min-värdet. 
        for value in row[2:]: #Loopa över varje element i raden förutom den första. 
            min_value = min(min_value, float(value)) #Min-värdet uppdateras ifall det hittas ett mindre. 
        print([row[0], min_value]) #Skriver ut årtal samt min-värdet. 


while True:
    Val = int(input("Välj alternativ 1-6: "))
    if Val == 1:
        skriv_ut()
    elif Val == 2:
        print("Beräknar summan")
        summa(kpi_10)
    elif Val == 3: 
        print("Beräknar medelvärdet")
        mean_list(kpi_10)
        
    elif Val == 4: 
        print("Hittar största värdet")
        max_rows(kpi_10)
    elif Val == 5: 
        print("Hittar minsta värdet")
        min_rows(kpi_10)
    elif Val == 6:
        print("Avslutar programmet")
        break