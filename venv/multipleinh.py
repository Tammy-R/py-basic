#PArent class
class Item():
    def __init__(self,sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))

#Parent class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garmen(self):
        print("The garment is in section {}, {}". format(self.section, self.type))

#Child class inh from both parents
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale".format(self.color, self.name))

Blouse = Shirts("00001", 43, "Tops", "Formal blouse", "White")
Blouse.print_sku()
Blouse.print_garmen()
Blouse.print_shirt()

#polymorphism - kada overvridujemo metodu u klasi, npr umamo metodu u parent klasi, u child definisjemo metodu sa istim imenom i izmenimo nesto, kada pozovemo ciled klasu sa tom metodom ona ce se koristiti a ne parent
