def rechnen(eingabe):
    ausgabe = 0
    try:
        if eingabe.find("w") >= 0 and eingabe.find("^") >= 2:
            if eingabe.find("w") >= 1:
                print("Umgerechnet: ")
                potenz = int(eingabe[eingabe.find("^") + 1:len(eingabe)])
                zahlvp = float(eingabe[eingabe.find("w") + 1:eingabe.find("^")])
                zahlvw = float(eingabe[0:eingabe.find("w")])
                ausgabe = zahlvw * ((zahlvp ** potenz) ** 0.5)
                print(ausgabe)
            else:
                print("Umgerechnet: ")
                potenz = int(eingabe[eingabe.find("^") + 1:len(eingabe)])
                zahlvp = float(eingabe[eingabe.find("w") + 1:eingabe.find("^")])

                ausgabe = float((zahlvp ** potenz) ** 0.5)
                print(ausgabe)

        elif eingabe.find("w") >= 1:
            print("Umgerechnet: ")
            zahlw = int(eingabe[eingabe.find("w") + 1:len(eingabe)])
            zahlvw = int(eingabe[0:eingabe.find("w")])

            ausgabe = float(zahlvw * (zahlw ** 0.5))
            print(ausgabe)

        elif eingabe.find("w") == 0:
            print("Umgerechnet: ")
            zahlw = int(eingabe[eingabe.find("w") + 1:len(eingabe)])

            ausgabe = float(zahlw ** 0.5)
            print(ausgabe)

        elif eingabe.find("^") >= 1:
            print("Umgerechnet: ")
            potenz = int(eingabe[eingabe.find("^") + 1:len(eingabe)])
            zahlvp = float(eingabe[0:eingabe.find("^")])

            ausgabe = float(zahlvp ** potenz)
            print(ausgabe)
        else:
            ausgabe = float(eingabe)

    except ValueError:
        print("Bitte nur numerische Eingaben machen!")
    return ausgabe;