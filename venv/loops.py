#for loop
fruits = ["apple", "orange", "pears", "grapes"]

for fruit in fruits:
    print("Would you like {} ?".format(fruit))

#umesto broja 7 prikazace se poruka
for number in range(1,11):
    if number == 7:
        print("We are skipping number 7")
        continue
    print("This is the number {}.".format(number))

#broj 3 ce biti preskocen, nece biti ispisana poruka
for number in range(1,11):
    if number == 3:
        pass
    else:
        print("This is the number {}.".format(number))

#while + kad uslov dodje do 33 zaustavice se program
temp_f = 40

while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break

    
#loop controls
""" 
Break - end the loop go to the next statement in the code outside the loop
Continue - skips current part of the loop, moves to the next part of the loop
Pass - skips any part of the loop where pass appears, best use for testing code. (remove it when the code is ready for prod)
"""

