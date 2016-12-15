import os
import time
import ctypes
os.system("start C:/Users/Kaspar/Desktop/desktop2/kaktus1.jpg")

nimi = input("Mis su nimi on?")
ctypes.windll.user32.MessageBoxW(0, "Kas sa oled võitluseks valmis, " + nimi.title() + "?", "Küsimus", 4)
vastane = input("Kes on su vastane?")
print("Kui lahendad kõik matemaatikaülesanded õigesti, lööd vastase knockouti." + "\n" + "Iga õige vastuse eest saad ühe punkti, viimase eest aga kaks.")
skoor = 0
ctypes.windll.user32.MessageBoxW(0, "Siit tuleb esimene tehe, " + nimi.title() + "!", "Round 1", 1)
start = str(time.clock())

esimene = float(input("4+2="))
while skoor <=2:
    if esimene == 6:
        skoor +=1
        print("Lõid vastasele ribidesse")
    else:
        skoor-=1
        print(vastane.title() + " lõi sulle ribidesse")

    teine = float(input("Teine tehe= 4x11="))
    if teine == 44:
        skoor +=1
        print("Lõid vastasele säärde")
    else:
        skoor -=1
        print(vastane.title() + " lõi sulle säärde")

    kolmas = float(input("Kolmas tehe, topeltpunktid= 1600:20="))
    if kolmas==80:
        skoor+=2
        print("Jooksid vastase selja taha")
    else:
        skoor-=1
        print(vastane.title() + " jooksis su selja taha")
        
if skoor >= 3:
    os.system("start C:/Users/Kaspar/Desktop/desktop2/punch.wav")
    ctypes.windll.user32.MessageBoxW(0, "Hea töö, lõid vastase viimase löögiga otse knockouti, " + nimi.title() + "!" + "\n" + "Selleks kulus vaid " + (str(int(time.clock()))) + " sekundit." + "\n" + vastane.title() + " ongi pikali maas.", "Sa võitsid!", 1)
elif skoor < 3:
    os.system("start C:/Users/Kaspar/Desktop/desktop2/punch.wav")
    ctypes.windll.user32.MessageBoxW(0, "Knockout, said paremhaagi otse kahe silma vahele, " + nimi.title() + "!" + "\n" + "Selleks kulus vaid " + (str(int(time.clock()))) + " sekundit.", "Sa kaotasid!", 1)
print("Sinu koguskoor on " + str(skoor) + ".")
