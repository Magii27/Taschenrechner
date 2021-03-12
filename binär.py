def binär(eingabe):
    eingabestr = str(eingabe)
    eingabeint = int(eingabe)
    count = 0
    ausgabe = 0
    for x in eingabestr:
        print(x)
        if x == "1" or x == "0":
            var_prüf = 0
            count += 1
        else:
            var_prüf = 1
            break
    count = 1
    if var_prüf == 0:
        for x in eingabestr:
            var_zw = int(x) * (2 ** (len(eingabestr) - count))
            ausgabe = int(ausgabe + var_zw)
            count = count + 1
    else:
        while eingabeint == 0:
            eingabeint

        print("moin")
        ausgabe = 2
    return ausgabe;


var = input()
print(binär(var))
