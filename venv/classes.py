# omogucava grupisanje funkcija u jednu jedinicu, isto kao u JS

#__init__ method omogucava kreiranje svakog instance klase sa specificnim parametrima
#self carijavla omogucava da se lako dele informacije

class Person:
    def __init__(self, firstname, lastname, health, status):
        """ initialize attributes to be used in available for all class methods 
        in this class, and for class objects created by this class"""

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("Hello, my name is {} {}.".format(self.firstname, self.lastname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >=76:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >=40:
            print("{} goes to the doctor.".format(self.firstname))
        else:
            print("{} is unconscious".format(self.firstname))

Maria = Person("Maria", "Ana", 94, status=True)
Ray = Person("Ray", "Baronne", 45, status=True)
Lee = Person("Lee", "Lu", 88, status=False)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Lee.firstname, Lee.status))

Maria.introduce()
Ray.introduce()
Lee.introduce()

Maria.status_change()
Ray.status_change()
Lee.status_change()


#inheritance
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -=5
        print(other.health)

    def insult(self, other):
        if other.health <=80:
            print("{} you are tired and weak.".format(other.firstname))

    def steal(self, other):
        print("Ha, ha, ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False

Alex = Enemy("rock", "Alex", "Wayne", 75, status =False)
Alex.hurt(Maria)
Alex.insult(Ray)
Alex.steal(Lee)

