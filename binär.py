def binär(eingabe):
    eingabestr = str(eingabe)
    eingabeint = int(eingabe)
    count = 0
    for x in eingabestr:
        print(x)
        if eingabe[count:count] == 1 or eingabe[count:count] == 0:
            var_prüf = 0
            count += 1
        else:
            var_prüf = 1
            break

    var_erg = 0
    if var_prüf == 0:
        for x in eingabestr:
            var_zw = int(eingabeint[x:x] * (2 ** x))
            ausgabe = int(ausgabe + var_zw)
    else:
        print("moin")
        ausgabe = 2
        return ausgabe;


var = str(input())
print(binär(var))
