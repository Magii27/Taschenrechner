import formel
import binär

print("Hey, was soll ich dir ausrechnen?")

var_try = 1
while var_try == 1:

    var_start = input("Hanbuch (h) - Weiter zum Taschenrechner (t) - Weiter zur Umrechnung (u) \n")

    if var_start == "h" or var_start == "H" or var_start == "t" or var_start == "T" or var_start == "u" or var_start == "U":
        if var_start == "h" or var_start == "H":
            print("")
            print("Der Taschenrechner ist folgendermaßen aufgebaut und hat diese Funktionen:")
            print("Bei der Eingabe der Zahlen können nur numerische Eingaben getätigt werden")
            print("Ausnahmen sind: \n")
            print("Potenzen die mit '^' und mit der nachfolgender Potenz geschrieben werden")
            print("  Bei der ersten Eingabe, kann ausgewählt werden ob mit dieser weiter gerechnet wird oder nur umgerechnet wird")
            print("Wurzeln die mit 'w' und mit der nachfolgenden Zahl geschrieben werden \n")
            input("'Enter' klicken um fortzufahren")
            var_try = 1
        elif var_start == "u" or var_start == "U":
            var_try = 2
        else:
            var_try = 0
    else:
        print("Tut mir leid, das habe ich nicht verstanden, versuchs nochmal :)")
        var_try = 1

    while var_try == 2:

        try:
            var_z = input("Welche Zahl darf ich dir umrechnen? \n")
            print(binär.binär(var_z))
            var_try = 4
        except ValueError:
            var_try = 2
        while var_try == 4:
                print(" ")
                print("Neue Zahl umrechnen (u)")
                print("Zurück zum Start (s)")
                print("Das Programm beenden (e)")
                var_repeat = input()
                if var_repeat == "u" or var_repeat == "U":
                    var_try = 2
                elif var_repeat == "s" or var_repeat == "S":
                    var_try = 1
                elif var_repeat == "e" or var_repeat == "E":
                    print("Auf Wiedersehen!")
                    exit()
                else:
                    var_try = 3

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
                    var_z1 = float(formel.rechnen(var_z1))
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
                var_z2 = float(formel.rechnen(var_z2))
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

        var_try = 5
        while var_try == 5:
                print(" ")
                print("Neue Rechnung starten (t)")
                print("Mit dem Ergebnis weiterrechnen (r)")
                print("Zurück zum Start (s)")
                print("Das Programm beenden (e)")
                var_repeat = input()
                if var_repeat == "t" or var_repeat == "T":
                    var_try = 0
                elif var_repeat == "r" or var_repeat == "R":
                    var_z1 = var_erg
                    var_try = 0
                elif var_repeat == "s" or var_repeat == "S":
                    var_try = 1
                elif var_repeat == "e" or var_repeat == "E":
                    print("Auf Wiedersehen!")
                    exit()
                else:
                    var_try = 5
