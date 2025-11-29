"""
Kérj be két számot, és írd ki az összegüket.
"""

# szam1 = int(input("Kérlek Adj meg egy számot: "))
# szam2 = int(input("Kérlek Adj meg még egy számot: "))
# print(f"A két szám összege {szam1+szam2}.")

#--------------------------------------------------------------

""""
Kérj be egy számot, és döntsd el, hogy páros-e.
"""

# szam1 = int(input("Kérlek Adj meg egy számot: "))
# if szam1 % 2 == 0 and szam1 > 0:
#     print("A beírt szám páros")
# elif szam1 == 0:
#     print("A beírt szám a 0")
# else:
#     print("A beírt szám páratlan")

#--------------------------------------------------------------

"""
Kérj be három számot, és írd ki melyik a legnagyobb.
"""

# szam1 = int(input("Kérlek adj meg egy számot: "))
# szam2 = int(input("Kérlek adj meg még egy számot: "))
# szam3 = int(input("Kérlek adj meg még egy számot: "))
# if szam1 > szam2 and szam1 > szam3:
#     print(f"Az első szám a {szam1} a legnagyobb")
# elif szam2 > szam3:
#     print(f"A második szám a {szam2} a legnagyobb")
# else:
#     if szam1 == szam2 and szam1 == szam3 and szam3 == szam2:
#         print("A három szám egyforma")
#     else:
#         print(f"A harmadik szám a {szam3} a legnagyobb")

#--------------------------------------------------------------

"""
Kérj be egy N értéket, majd írd ki 1-től N-ig a számokat egy ciklussal.
"""

# N = int(input("Kérlek adj meg egy számot: "))
# for i in range(1,N+1):
#     print(i)

#--------------------------------------------------------------

"""
Kérj be egy N számot, majd számold ki a 1..N közötti számok összegét.
"""

# N = int(input("Kérlek adj meg egy számot: "))
# szam = 1
# osszeg = 0
# while szam <= N:
#     osszeg = osszeg + szam
#     szam += 1

# print(osszeg) 

#--------------------------------------------------------------

"""
Kérj be 5 darab számot, tedd őket listába, majd számold ki az átlagukat.
"""

# szamlista =[]
# for i in range(5):
#     szamok = int(input("Kérlek adj meg egy számot: "))
#     szamlista.append(szamok)
# print(szamlista)
# osszeg = 0
# for db in szamlista:
#     osszeg = osszeg + db
# print(osszeg / len(szamlista))

#--------------------------------------------------------------

"""
Adj meg egy listát tetszőleges egész számokkal, majd írd ki:
a legnagyobb értéket
a legkisebb értéket
"""

# szamlista =[25,32,105,147,23,14,35]
# print(f"A lista legkisebb eleme a {min(szamlista)}")
# print(f"A lista legnagyobb eleme a {max(szamlista)}")

#--------------------------------------------------------------

"""
Kérj be egy számot és döntsd el, hogy benne van-e az előre adott listában.
"""

# szamlista =[25,32,105,147,23,14,35]
# megadottSzam = int(input("Kérlek adj meg egy számot: "))

# if megadottSzam in szamlista:
#     print("A szám megtalálható a listában")
# else:
#     print("A szám nincs benne a listában")

#--------------------------------------------------------------

"""
Adott egy lista számokkal. Készíts új listát, amelyben csak a páros számok szerepelnek.
"""

szamlista =[25,32,105,147,23,14,35]
parosLista = []

for szam in szamlista:
    if szam % 2 == 0:
        parosLista.append(szam)
print(parosLista)

  
