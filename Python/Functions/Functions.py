def countWordsFromFile():
    fileName = input("Enter the name of file: \n")
    numberOfWords = 0
    file = open(fileName, "r+")

    for line in file:
        word = line.split()
        numberOfWords = numberOfWords + len(word)
        print(word)

    file.write("This is how we should write")
    print("the number of words is: " + str(numberOfWords))


countWordsFromFile()
