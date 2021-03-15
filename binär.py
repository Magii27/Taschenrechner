def binär(eingabe):
    eingabestr = str(eingabe)
    eingabeint = int(eingabe)
    counter = 0
    ausgabe = 0

    for x in eingabestr:

        if x == "1" or x == "0":
            prüfung = 0
            counter += 1
        else:
            prüfung = 1
            break

    if prüfung == 0:
        versuch = 1
        while versuch == 1:
            abfrage = input("Ist das deine Dezimalzahl (d) oder eine Binärzahl (b)? \n")

            if abfrage == "b" or input == "B":
                umrechnenbi(eingabestr)
                versuch = 0
            elif abfrage == "d" or input == "D":
                umrechnende(eingabeint)
                versuch = 0
            else:
                print("Sorry ich hab dich nicht verstanden")
                versuch = 1
    else:
        umrechnende(eingabeint)

    return ausgabe;


def umrechnenbi(eingabe):
    counter = 1
    ausgabe = 0
    for x in eingabe:
        zahlzw = int(x) * (2 ** (len(eingabe) - counter))
        ausgabe = int(ausgabe + zahlzw)
        counter += 1
    print("Umgerechnet in dezimal: ")
    print(ausgabe)

    return;


def umrechnende(x):
    ausgabe = 0
    while x >= 1:
        zahlzw = x % 2
        x = x // 2
        zahlzw = str(zahlzw)
        ausgabe = str(ausgabe) + zahlzw

    ausgabe = ausgabe[::-1]
    ausgabe = ausgabe[0:len(ausgabe) - 1]
    print("Umgerechnet in binär: ")
    print(ausgabe)

    return;