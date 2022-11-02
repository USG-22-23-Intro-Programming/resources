def main():

    #recall lists like:
    fruits = ["apples", "oranges", "pluots", "tomatoes"]

    # dictionaries are lists where each element has a value associated with it

    # each element is a 'key : value'
    # works like a function ,  key = input ,  value = output
    fruits2 = {"apple" : 1.50, "banana" : 0.75, "watermelon" : 6.00, "strawberries" : 3.50}

    #add or change things about the dictionary
    fruits2.update({"kumquat" : 1.50})

    vegetables = {"lettuce" : 2.50,
                  "cabbage" : 3.25,
                  "scallions" : 0.99,
                  "onion" : 1.15,
                  "russet potato" : 2.50}

    # access the value based on a key
    print(vegetables.get("cabbage"))
    #print(vegetables)
    print(vegetables.pop("onion"))
    #print(vegetables)
    listOfKeys = vegetables.keys()
    listOfKeys = list(listOfKeys)

    for element in listOfKeys:
        print(element)

    


if __name__ == "__main__":
    main()
