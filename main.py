def rechnen(eingabe):
    try:
        if eingabe.find("w") >= 0 and eingabe.find("^") >= 2:
            if eingabe.find("w") >= 1:
                print("Umgerechnet: ")
                potenz = int(eingabe[eingabe.find("^") + 1:len(eingabe)])
                zahlvp = float(eingabe[eingabe.find("w") + 1:eingabe.find("^")])
                zahlvw = float(eingabe[0:eingabe.find("w")])
                eingabe = zahlvw * ((zahlvp ** potenz) ** 0.5)
                print(eingabe)
            else:
                print("Umgerechnet: ")
                potenz = int(eingabe[eingabe.find("^") + 1:len(eingabe)])
                zahlvp = float(eingabe[eingabe.find("w") + 1:eingabe.find("^")])

                eingabe = float((zahlvp ** potenz) ** 0.5)
                print(eingabe)

        elif eingabe.find("w") >= 1:
            print("Umgerechnet: ")
            zahlw = int(eingabe[eingabe.find("w") + 1:len(eingabe)])
            zahlvw = int(eingabe[0:eingabe.find("w")])

            eingabe = float(zahlvw * (zahlw ** 0.5))
            print(eingabe)

        elif eingabe.find("w") == 0:
            print("Umgerechnet: ")
            zahlw = int(eingabe[eingabe.find("w") + 1:len(eingabe)])

            eingabe = float(zahlw ** 0.5)
            print(eingabe)

        elif eingabe.find("^") >= 1:
            print("Umgerechnet: ")
            potenz = int(eingabe[eingabe.find("^") + 1:len(eingabe)])
            zahlvp = float(eingabe[0:eingabe.find("^")])

            eingabe = zahlvp ** potenz
            print(eingabe)
        else:
            eingabe = float(eingabe)

    except ValueError:
        print("Bitte nur numerische Eingaben machen!")
    return eingabe;


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
var_repeat = ""

while var_try == 0:
    var_try = 1

    while var_try == 1:
        var_try = 0

        if var_repeat == "r":
            print("Erste Zahl:")
            print(var_z1)
        else:
            print(" ")
            var_z1 = input("Erste Zahl:\n")
            try:
                var_z1 = float(rechnen(var_z1))
            except ValueError:
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

        var_z2 = input("Zweite Zahl:\n")
        try:
            var_z2 = float(rechnen(var_z2))
        except ValueError:
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
