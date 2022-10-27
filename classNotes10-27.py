def main():

    #lists are like strings in that they hold a collection of elements in a specific
    #order. They use brackets

    '''names = ["Lyzane", "Zuri", "Jaein", "Olumat", "Eisha", "Nawal", "Jaein"]
    #first element
    print(names[0])
    #second element
    print(names[1])

    #add an element to the end of the list
    names.append("Serena")

    print("Last element:")
    print(names[-1])
    print(names[len(names)-1])

    print(names)

    #remove an element from the list
    names.remove("Jaein")
    print(names)'''

    names = ["Zuri", "Considine", "Hamilton", "Lafayette", "Galileo", "Aristotle"]

    for i in range(len(names)):
        print(names[i])

    print("---")

    #for each loop
    for name in names:
        if name == "Considine":
            print("Mr. Considine, here!")
        else:
            print("Hello, famous " + name)

    #get index (position) of an element in a list

    print(names.index("Galileo"))
    print(names.index("Zuri"))



    

if __name__ == "__main__":
    main()
