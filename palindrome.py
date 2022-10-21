
def palindrome():
    s = input("Type in a palindrome you want to test")

    length = len(s)

    #for loop to repeat
    #i starts at 0, and it adds one each time
    for i in range(length):
        if s[i] != s[length - 1 - i]:
            return False
        
    return True




def isMultiple(num1, num2):
    if num1 % num2 == 0:
        print(str(num1) + " is a multiple of " + str(num2))
    else:
        print(str(num1) + "is not a multiple of " + str(num2))

def main():
    isMultiple(100, 25)

    answer = palindrome()
    print(answer)



    

if __name__ == "__main__":
    main()
    
