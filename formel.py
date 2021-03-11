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