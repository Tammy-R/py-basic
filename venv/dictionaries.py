# isto sto je objekat u JS
from turtle import st


stuff ={"food": 15, "energy": 100, "enemies": 3}

#dobijanje vrednosti nekog key-a
print(stuff.get("food"))

#izlistavanje parova key-value koje sadrzi diksneri
print(stuff.items())

#izlistavanje svih key-eva 
print(stuff.keys())

#brisanje poslednjeg key-value para
print(stuff.popitem())
print(stuff)

#provera da li item postoji i njegovu vrednost i dodavanje novog para key-value
print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 102))
print(stuff)

#update sa drugim dic
new_items = {"rock": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

stuff.update(food = 450, cookies = 6)
print(stuff)