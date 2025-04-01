#ukol a
jidloJedna = input("")
jidloDva = input("")
jidloTri = input("")

kalorieJedna = int(input(""))
kalorieDva = int(input(""))
kalorieTri = int(input(""))

soucet = kalorieJedna + kalorieDva + kalorieTri
celkove_kalorie = soucet
print (celkove_kalorie)

#ukol b 
aktivitaJedna = input("")
aktivitaDve = input("")
delkaAktivityJedna = int(input(""))
delkaAktivityDva = int(input(""))
delka = delkaAktivityJedna + delkaAktivityDva
celkovy_vydej = delka*5
print(celkovy_vydej)

#spolecny ukol 
#Adam Lucák #Lukáš Smetana
print(celkove_kalorie)
spaleni = celkove_kalorie - celkovy_vydej
if (spaleni>0):
    print("prebytek" and spaleni)
else:
    print("nedostatek" and spaleni)
  
    