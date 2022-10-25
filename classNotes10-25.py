#class definition

'''class Person:

    #define a constructor
    def __init__(self, age, name):
        self.hairColor = "black"
        self.age = age
        self.name = name

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def drinkWater(self, volume):
        print("Wow I just drank " + str(volume) + " liters of water!")'''
        



#main method
def main():

    '''Lyzane = Person(15, "Lyzane")

    mrC = Person(75, "Considine")
    Jaewon = Person(15, "J-Money")

    print(Lyzane.getName() + " is " + str(Lyzane.getAge()) + " years old")
    print(mrC.getName() + " is " + str(mrC.getAge()) + " years old")
    print(Jaewon.getName() + " is " + str(Jaewon.getAge()) + " years old")

    Lyzane.drinkWater(2)

    #strings are an array of characters. each character has a position. starts at 0
    myS = "Hello World"

    #myS = myS[:2] + myS[3:]
    print(myS)

    char = myS[7]
    print(char)

    ind = myS.index("o")
    print(ind)

    #index can also take in a starting position and ending position
    ind2 = myS.index("o", 5, 9)
    print(ind2)

    count = myS.count("o")
    print(count)

    count = myS.count("z")
    print(count)

    #removes white space that is leading or trailing the string
    newS = "    this example was scuffed           "
    newS = newS.strip()
    print(newS)

    newS2 = "    !aabbbMr. ConsidineqqmM  "
    newS2 = newS2.strip(" !abqmM")
    print(newS2)

    #replace all instances of a substring with another substring
    print(newS2.replace("i", "A"))'''


    #for loop: repeat something a specific amount of times

    '''for i in range(5):
        print("hello")
        print(i)

    for i in range(10, 20):
        print("yellow")
        print(i)

    name = "The coolest school in the PNW"
    for i in range(len(name)):
        print(name[i])

    answer = "I don't know"
    for x in answer:
        print(x)'''


    y = 50
    while (y > 10):
        print("this value: " + str(y))
        y = y -2


    S = "never leave class"
    i = 0
    while True:
        print(S)
        check = S[i]
        if check == "c":
            break
        else:
            i = i+1










    


if __name__ == "__main__":
    main()

#string methods
#   -index
#   -count
#   -capitalize
#   -strip
#   -replace


#loops
#   -for i in range
#   -while
#   -while True


