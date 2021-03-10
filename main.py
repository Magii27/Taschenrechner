
print("Hey, was soll ich dir ausrechnen?")

var_try = 1
while var_try == 1:

    var_start = input("Hanbuch (h) - Weiter zum Taschenrechner (t) \n")

    if var_start == "h" or var_start == "H" or var_start == "t" or var_start == "T":
        if var_start == "h" or var_start == "H":
            print("")
            print("Der Taschenrechner ist folgendermaßen aufgebaut und hat diese Funktionen:")
            print("Bei der Eingabe der Zahlen können nur numerische Eingaben getätigt werden")
            print("Ausnahmen sind: \n")
            print("Potenzen die mit '^' und mit der nachfolgender Potenz geschrieben werden")
            print("  Bei der ersten Eingabe, kann ausgewählt werden ob mit dieser weiter gerechnet wird oder nur umgerechnet wird")
            print("Wurzeln die mit 'w' und mit der nachfolgenden Zahl geschrieben werden \n")
            input("'Enter' klicken um fortzufahren")
            var_try = 0
        var_try = 0
    else:
        print("Tut mir leid, das habe ich nicht verstanden, versuchs nochmal :)")
        var_try = 1

var_op = ["+", "-", "*", "/"]

x = 0
var_repeat = ""
var_try = 0
while var_try == 0:
    var_try = 1

    while var_try == 1:
        var_try = 0

        try:
            if var_repeat == "r":
                print("Erste Zahl:")
                print(var_z1)
            else:
                print(" ")
                var_z1 = input("Erste Zahl:\n")

                if var_z1.find("w") >= 0 and var_z1.find("^") >= 2:
                    print("Umgerechnet: ")
                    if var_z1.find("w") >= 1:
                        var_posp = int(var_z1[var_z1.find("^") + 1:len(var_z1)])
                        var_zp = float(var_z1[var_z1.find("w") + 1:var_z1.find("^")])
                        var_zv = float(var_z1[0:var_z1.find("w")])
                        var_z1 = var_zv * ((var_zp ** var_posp) ** 0.5)
                        print(var_z1)
                    else:
                        var_posp = int(var_z1[var_z1.find("^") + 1:len(var_z1)])
                        var_zp = float(var_z1[var_z1.find("w") + 1:var_z1.find("^")])

                        var_z1 = float((var_zp ** var_posp) ** 0.5)
                        print(var_z1)

                elif var_z1.find("w") == 0:
                    print("Umgerechnet: ")
                    var_zw = int(var_z1[var_z1.find("w")+1:len(var_z1)])

                    var_z1 = float(var_zw**0.5)
                    print(var_z1)
                elif var_z1.find("^") >= 1:
                    print("Umgerechnet: ")
                    var_posp = int(var_z1[var_z1.find("^")+1:len(var_z1)])
                    var_zp = float(var_z1[0:var_z1.find("^")])

                    var_z1 = var_zp**var_posp
                    print(var_z1)
                else:
                    var_z1 = float(var_z1)

        except ValueError:
            print("Bitte nur numerische Eingaben machen!")
            var_try = 1

    var_try = 1
    while var_try == 1:
        var_try = 0
        var_inp = input("Welcher Operator:\n")
        if var_inp not in var_op:
            print("Bitte gebe nur richtige Operatoren an: + - * /")
            var_try = 1

    var_try = 1
    while var_try == 1:
        var_try = 0
        try:

            var_z2 = input("Zweite Zahl:\n")

            if var_z2.find("w") >= 0 or var_z2.find("^") >= 2:
                print("Umgerechnet: ")
                if var_z2.find("w") >= 1:
                    var_posp = int(var_z2[var_z2.find("^") + 1:len(var_z2)])
                    var_zp = float(var_z2[var_z2.find("w") + 1:var_z2.find("^")])
                    var_zv = float(var_z2[0:var_z2.find("w")])
                    var_z2 = var_zv * ((var_zp ** var_posp) ** 0.5)
                    print(var_z2)
                else:
                    var_posp = int(var_z2[var_z2.find("^") + 1:len(var_z2)])
                    var_zp = float(var_z2[var_z2.find("w") + 1:var_z2.find("^")])

                    var_z2 = float((var_zp ** var_posp) ** 0.5)
                    print(var_z2)

            elif var_z2.find("w") >= 0:
                print("Umgerechnet: ")
                var_zw = int(var_z2[var_z2.find("w") + 1:len(var_z2)])

                var_z2 = float(var_zw ** 0.5)
                print(var_z2)
            elif var_z2.find("^") >= 1:
                print("Umgerechnet: ")
                var_posp = int(var_z2[var_z2.find("^") + 1:len(var_z2)])
                var_zp = float(var_z2[0:var_z2.find("^")])

                var_z2 = var_zp ** var_posp
                print(var_z2)
            else:
                var_z2 = float(var_z2)

        except ValueError:
            print("Bitte nur numerische Eingaben machen!")
            print(" ")
            var_try = 1

    if var_inp == "+":
        var_erg = var_z1 + var_z2
        print("Dein Ergebnis ist: ", var_erg)
    elif var_inp == "-":
        var_erg = var_z1 - var_z2
        print("Dein Ergebnis ist: ", var_erg)
    elif var_inp == "*":
        var_erg = var_z1 * var_z2
        print("Dein Ergebnis ist: ", var_erg)
    elif var_inp == "/":
        if var_z2 == 0:
            print("Man kann keine Zahl durch 0 teilen")
        else:
            var_erg = var_z1 / var_z2
            print("Dein Ergebnis ist: ", var_erg)
    else:
        print("Gib einen richtigen Operator ein! \n")

    var_try = 1
    while var_try == 1:
            print(" ")
            print("Neue Rechnung starten (t)")
            print("Mit dem Ergebnis weiterrechnen (r)")
            print("Das Programm beenden (e)")
            var_repeat = input()
            if var_repeat == "t" or var_repeat == "T":
                var_try = 0
            elif var_repeat == "r" or var_repeat == "R":
                var_z1 = var_erg
                var_try = 0
            elif var_repeat == "e" or var_repeat == "E":
                print("Auf Wiedersehen!")
                exit()
            else:
                var_try = 1