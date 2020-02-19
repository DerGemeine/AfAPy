import time
#Volljahres Berechnung (VJB) also von Januar bis zum Juni.
VJB = int(6)
#Halbjahres Berechung (=HJB) also von Juli bis zum Dezember.
HJB = int(7)


print("Geben Sie den Wert des Gegenstandes (mit MwSt.) ein, dessen jährliche Abschreibung berechnet werden soll. Den Punkt als Kommatrennzeichen verwenden.")
# Variablen kürzen wir mit den jeweiligen Anfangsbuchstaben der Beschreibung ab, sprich Wert des Gegenstandes = WdG.
WdG = float(input("Bitte geben Sie den Wert ein: "))
print("Geben Sie den Prozentsatz ein, zu welchem der Gegenstand für gewerbliche Zwecke genutzt wird.")
#Prozentsatz der gewerblichen Nutzung = PdgN.
PdgN = float(input("Bitte geben Sie den Prozentsatz ein: "))

#Die AfA wird berechnet in dem der Preis des Gegenstandes durch 100 geteilt wird und anschlißend mit dem Prozentsatz der gerwerblichen Nutzung mutlipliziert wird.
#AfA Insgesamt = AfAInsG
AfAInsG = ((WdG / 100) * PdgN)

#print("Dies ergibt eine gesamte AfA in Euro:  ") ---!---> Wichtig zum Schluss einbauen
#Aufrunden der AfA auf zwei Kommastellen.
#AfA Insgesamt gerrundet = AfAInsGg
AfAInsGg = ("%.2f" % AfAInsG)
print

print("Geben Sie die Nutzungdauer in vollen Jahren an z.B. 3")
#Nutzungsdauer in Jahren = NiJ
NiJ = int(input("Bitte geben Sie die Nutzungsdauer ein: "))

print("Geben Sie das Kaufjahr in normaler Schreibweise an, z.B. 2020")
#Vollständiges Kaufjahr = VKJ
VKJ = int(input("Bitte geben Sie das Kaufjahr ein: "))

print("Geben Sie den Kaufmonat in numerischer Schreibweise an, z.B. 7 für Juli")
#Numerischer Kaufmonat
NKM = int(input("Bitte geben sie den Kaufmonat ein: "))

#Wenn der Kaufmonat kleiner oder gleich groß ist wie der Juni (6. Monat), dann berechne die volle AfA (Volljahres).
if NKM <= VJB:
    #Die AfA des Volljahres berechnen, AfAInsG durch die Nutzungsdauer in Jahren.
    #Volljahres AfA = VJAfA
    VJAfA = (AfAInsG / NiJ)
    #Aufrunden der Volljahres AfA auf zwei Kommastellen.
    #Volljahres AfA gerrundet = VJAfAg
    VJAfAg = ("%.2f" % VJAfA)

    #Addition des Kaufjahres mit der Nutzungsdauer um das Enddatum der Abschreibung zu ermitteln, sowie die 
    #Enddatum der Abschreibung = EdA
    EdA = int(VKJ + NiJ)
    list_EdA = list(range(VKJ, EdA))
    [print("AfA im Jahr", i, 'beträgt: ', VJAfAg) for i in list_EdA]

 #Wenn der Kaufmonat größer oder gleich groß ist wie der Juli (7. Monat), dann berechne die halbe AfA (Halbjahres).       
elif NKM >= HJB:
    #Die AfA des ersten sowie letzten Halbjahres berechnen, AfAInsG durch die Nutzungsdauer in Jahren.
    #Halbjahres AfA = HJAfA
    VJAfA = ((AfAInsG / NiJ) / 2)
    HJAfAg = ("%.2f" % VJAfA)
    print(HJAfAg)
time.sleep(10)




