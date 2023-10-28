def add (x, y):
    return x + y
def subtract (x, y):
    return x - y
def multiply (x, y):
    return x * y
def divide (x,y):
    return x / y
 
print("mimateba")
print("gamokleba")
print("gamravleba")
print("gayofa")

priveli_ricxvi = float(input("pirveli ricxvi: "))
meore_ricxvi = float(input("meore ricxvi: "))


zzz=input("operacia: mimateba, gamokleba, gamravleba, gayofa")

if zzz == "mimateba":
 print(add(priveli_ricxvi, meore_ricxvi))
if zzz == "gamokleba":
 print(subtract(priveli_ricxvi, meore_ricxvi))
if zzz == "gamravleba":
   print(multiply(priveli_ricxvi, meore_ricxvi))
if zzz == "gayofa":
   print(divide(priveli_ricxvi, meore_ricxvi))