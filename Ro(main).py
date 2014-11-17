a=input("Pour utiliser le convertisseur Arabe a Romain tapez '1' Pour utiliser le convertisseur Romain a Arabe tapez '2' : ")
if a=="1":
    arabe=int(input("entrez un nombre < ou = a 3999: "))
    I, IV, V, IX, X, XL, L, XC, C, CD, D, CM, M = 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000
    nch=''
    if arabe == 0:
        print(" Il n'y a pas de zero dans les chiffres romains ")
    elif arabe <= 3999:
        while(arabe - M >= 0):
            arabe -= M
            nch=nch+"M"
        while(arabe - CM >= 0):
            arabe -= CM
            nch=nch+"CM"
        while(arabe - D >= 0):
            arabe -= D
            nch=nch+"D"
        while(arabe - CD >= 0):
            arabe -= CD
            nch=nch+"CD"
        while(arabe - C >= 0):
            arabe -= C
            nch=nch+"C"
        while(arabe - XC >= 0):
            arabe -= XC
            nch=nch+"XC"
        while(arabe - L >= 0):
            arabe -= L
            nch=nch+"L"
        while(arabe - XL >= 0):
            arabe -= XL
            nch=nch+"XL"
        while(arabe - X >= 0):
            arabe -= X
            nch=nch+"X"
        while(arabe - IX >= 0):
            arabe -= IX
            nch=nch+"IX"
        while(arabe - V >= 0):
            arabe -= V
            nch=nch+"V"
        while(arabe - IV >= 0):
            arabe -= IV
            nch=nch+"IV"
        while(arabe - I >= 0):
            arabe -= I
            nch=nch+"I"
        print(nch)

    elif arabe > 3999:
        print("il n'existe pas de nombre au dela de 3999 en romain. Veuillez entre un nombre < ou = a 3999")
elif a=="2":
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_number = 0
    st_roman_number =input("entrez votre chiffre romain: ")
    lst_substract = []

    n = len(st_roman_number)
    for i in range(n-1):
      ch = st_roman_number[i]
      ch2 = st_roman_number[i+1]
      if (romans[ch] < romans[ch2]):
        lst_substract.append(i)
    for i in range(n):
      ch = st_roman_number[i]
      if (i in lst_substract):
        arabic_number -= romans[ch]
      else:
        arabic_number += romans[ch]
    print (arabic_number)


