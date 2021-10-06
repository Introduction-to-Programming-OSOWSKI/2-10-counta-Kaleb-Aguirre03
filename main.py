#Define the function countA() in order to count the number of "a's" in a string
def countA(w):

    w = w.lower()

    numberA = 0

    for i in range (0, len(w)):
        if w[i] == "a":
            numberA = numberA + 1

    return numberA

#print the function in order to test it
print (countA("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
