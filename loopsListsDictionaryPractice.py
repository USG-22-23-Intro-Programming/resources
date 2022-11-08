
def startS(myList):

    for fruit in myList:
        firstChar = fruit[0]

        if firstChar == "s":
            break

    print(fruit)

def main():

    '''L = []
    for i in range(11):
        x = i*2
        L.append(x)
    print(L)
    print(L[5])
    print(L[8])'''

    fruit = ["apple", "orange", "banana", "peach"]

    #startS(fruit)

    D = {"Zuri" : 10,
         "Emily" : 9,
         "Cathy" : 9,
         "Trinity" : 9,
         "Jaewon" : 10,
         "Mr. C" : 24}

    #print(D)
    names = D.keys()
    
    for n in names:
        curYear = D.get(n)
        D.update({n : curYear + 1})

    #print(D)
    

if __name__ == "__main__":
    main()
