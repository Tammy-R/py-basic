fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years)

#dodavanje jednog itema u liostu
fruits.append("oranges")
print(fruits)

#dodavanje druge liste u prvu
fruits.extend(years)
print(fruits)

# brisanje itema iz liste
fruits.remove("oranges")
print(fruits)

fruits.pop(0)
print(fruits)

#sort moze da uporedjuje samo listu istih tipova podataka
numbers = [5, 1928, 4, 17, 73.76, 20.458]
numbers.sort()
print(numbers)

# provera d ali item postoji na listi
print("apple" in fruits)
print("apples" in fruits)

print(fruits.count("apples"))
print(fruits.index("apples"))