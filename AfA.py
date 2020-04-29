'''Imports'''
import time
import configparser

'''Config'''
config = configparser.ConfigParser()
config.read('config.ini')

#Volljahres Berechnung (VJB) also von Januar bis zum Juni.
VJB = int(config['Monate']['VJB'])
#Halbjahres Berechung (HJB) also von Juli bis zum Dezember.
HJB = int(config['Monate']['HJB'])
#Variablen für die Obergenzen der geringwertigen Wirtschaftsgüter in den kommen Jahren und die momentane Obergrenze, kommt später in eine config file.
#geringwertige Wirtschaftsgüter Obergrenze 2019/2020/2021 = gWgO2019/gWgO2020/gWgO2021
gWgO2019 = int(config['gWgO']['gWgO2019'])
gWgO2020 = int(config['gWgO']['gWgO2020'])
gWgO2021 = int(config['gWgO']['gWgO2021'])

'''Funktionen'''
## Mit dieser Funktion nehmen wir eine Eingabeüberprüfung vor, nur Eingaben die int sind sowie nicht negativ.
##Eingabeüberprüfung int nicht negativ = Eueinn
def Eueinn(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Keine Zahl angegeben.")
            continue

        if value < 0:
            print("Eingabe ist negativ.")
            continue
        else:
            break
    return value

## Mit dieser Funktion nehmen wir eine Eingabeüberprüfung vor, nur Eingaben die float sind sowie nicht negativ.
## Eingabeüberprüfung float nicht negativ = Euefnn
def Euefnn(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Keine Zahl angegeben.")
            continue

        if value < 0:
            print("Eingabe ist negativ.")
            continue
        else:
            break
    return value


print("Geben Sie den Wert des Gegenstandes (mit MwSt.) ein, dessen jährliche Abschreibung berechnet werden soll. Den Punkt als Kommatrennzeichen verwenden.")
# Variablen kürzen wir mit den jeweiligen Anfangsbuchstaben der Beschreibung ab, sprich Wert des Gegenstandes = WdG.
WdG = Euefnn("Bitte geben Sie den Wert des Gegenstandes ein: ")

print("Geben Sie das Kaufjahr in normaler Schreibweise an, z.B. 2020.")
#Vollständiges Kaufjahr = VKJ
VKJ = Eueinn("Bitte geben Sie das Kaufjahr ein: ")

print("Geben Sie den Kaufmonat in numerischer Schreibweise an, z.B. 7 für Juli.")
#Numerischer Kaufmonat
NKM = Eueinn("Bitte geben sie den Kaufmonat ein: ")

print("Geben Sie den Prozentsatz ein, zu welchem der Gegenstand für gewerbliche Zwecke genutzt wird, z.B. 40.")
#Prozentsatz der gewerblichen Nutzung = PdgN.
PdgN = Euefnn("Bitte geben Sie den Prozentsatz ein: ")

print("Geben Sie die Nutzungdauer in vollen Jahren an z.B. 3.")
#Nutzungsdauer in Jahren = NiJ
NiJ = Eueinn("Bitte geben Sie die Nutzungsdauer ein: ")

#Die AfA wird berechnet in dem der Preis des Gegenstandes durch 100 geteilt wird und anschlißend mit dem Prozentsatz der gerwerblichen Nutzung mutlipliziert wird.
#AfA Insgesamt = AfAInsG
AfAInsG = ((WdG / 100) * PdgN)
#Aufrunden der gesamten AfA auf zwei Kommastellen.
#die gesamte AfA gerundet = VJAfAg
AfAInsGg = ("%.2f" % AfAInsG)

#Die AfA des Volljahres berechnen, AfAInsG durch die Nutzungsdauer in Jahren.
#Volljahres AfA = VJAfA
VJAfA = (AfAInsG / NiJ)
#Aufrunden der Volljahres AfA auf zwei Kommastellen.
#Volljahres AfA gerundet = VJAfAg
VJAfAg = ("%.2f" % VJAfA)

#Addition des Kaufjahres mit der Nutzungsdauer um das Enddatum der Abschreibung zu ermitteln, sowie die 
#Enddatum der Abschreibung = EdA
EdA = int(VKJ + NiJ)

#NiJ in einer Liste = list_NiJ
list_NiJ = list(range(VKJ, EdA))

#Wenn der Wert des Gegenstandes weniger als 400/800/1000 ist und der Gegenstand im Jahre 2019/2020/2019 gekauft wurde, dann gib die gesamte AfA gleich gerundet aus.
if (WdG < gWgO2019 and VKJ == 2019) or (WdG < gWgO2020 and VKJ == 2020) or (WdG < gWgO2021 and VKJ == 2021):
    print("Die komplette Abschreibung findet im Jahr", VKJ, 'in der Höhe von', AfAInsGg, 'statt.')

#Wenn der Kaufmonat kleiner oder gleich groß ist wie der Juni (6. Monat), dann berechne die volle AfA (Volljahres).
elif NKM <= VJB:

    #Für jedes Jahr der Nutzungdauer, drucke eine neue Zeile mit dem jeweiligen Jahr sowie der gerundeten Volljahres AfA.
    [print("AfA im Jahr", i, 'beträgt: €', VJAfAg) for i in list_NiJ]

#Wenn der Kaufmonat größer oder gleich groß ist wie der Juli (7. Monat), dann berechne die halbe AfA (Halbjahres) und dann die Ganzjahres.       
elif NKM >= HJB:
    #Die AfA des ersten sowie des letzten Halbjahres berechnen, AfAInsG durch die Nutzungsdauer in Jahren, das Ergebnis durch 2.
    #Halbjahres AfA = HJAfA
    VJAfA = ((AfAInsG / NiJ) / 2)
    #Aufrunden der Halbjahres AfA auf zwei Kommastellen.
    #Halbjahres AfA gerrundet = HJAfAg
    HJAfAg = ("%.2f" % VJAfA)
    print("AfA im Jahr", VKJ, 'beträgt: €', HJAfAg)
    #Entfernung des ersten und letzten Eintrages der list_EdA, da diese Jahre nicht mit der vollen AfA berechnet werden
    list_NiJ.pop(0)
    #Für jedes Jahr der übrig gebliebenen Nutzungdauer, drucke eine neue Zeile mit dem jeweiligen Jahr sowie der gerundeten Volljahres AfA.
    [print("AfA im Jahr", i, 'beträgt: €', VJAfAg) for i in list_NiJ]
    #Die Ausgabe der letzten Halbjahres AfA
    #In diesem Fall wird das EdA um ein Jahr erhöht, da sich die eigentliche Volljahres AfA auf zwei Jahre aufteilt.
    print("AfA im Jahr", EdA+1, 'beträgt: €', HJAfAg)
    
#Zum Schluss geben wir in jedem Fall die gesamte über die ganze Nutzungsdauer aus.    
print("Die gesamte AfA beträgt dabei: €", AfAInsGg)

time.sleep(10)