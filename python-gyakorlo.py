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

N = int(input("Kérlek adj meg egy számot: "))
szam = 1
osszeg = 0
while szam <= N:
    osszeg = osszeg + szam
    szam += 1

print(osszeg) 