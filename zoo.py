class Zoo:

    def __init__(self):
        self.name = "Mr. Considine's Zoo"
        self.habitats = ["plains", "jungle", "wetlands"]
        self.animals = ["Zebra", "Leopard", "Frog"]

    def getHabitats(self):
        return self.habitats

    def getAnimals(self):
        return self.animals

    def getHabitat(self, animal):
        for i in range(len(self.animals)):
            if self.animals[i] == animal:
                return self.habitats[i]

    def getAnimal(self, habitat):
        i = self.habitats.index(habitat)
        return self.animals[i]
    
    def addAnimalAndHabitat(self, animal, habitat):
        self.habitats.append(habitat)
        self.animals.append(animal)
    
def main():

    Z = Zoo()
    animal = "Leopard"
    print("The " + animal + " lives in the " + Z.getHabitat(animal))

    habitat = "wetlands"
    print("In the " + habitat + " there is a " + Z.getAnimal(habitat))

    Z.addAnimalAndHabitat("Monkey", "trees")

    print("Here are all of the habitats:")
    print(Z.getHabitats())
    print("Here are all of the animals:")
    print(Z.getAnimals())


if __name__ == "__main__":
    main()
