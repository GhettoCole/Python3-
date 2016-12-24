with open("data.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("I love programming, It's like writing poetry, it soothes your mind!\n"
                 "One day I wanna write my own project"
                 ".\nCoding is the only activity that energises me and give me a reason to do something")

with open("data.txt", encoding="utf-8") as myFile:
    line_num = 1
    while True:
        line = myFile.readline()
        if not line:  # if the lines are no longer available
            break
        print("Line", line_num, ": ", len(line), end="\n")
        line_num += 1

print("\nDerek bana's way\n")
with open("data.txt", encoding="utf-8") as myFile:
    line_num = 1
    while True:
        line = myFile.readline()
        if not line:  # if the lines are no longer available
            break
        print("Line ", line_num)
        wordList = line.split()
        print("Number of words: ", len(wordList))
        charCount = 0
        for word in wordList:
            for char in word:
                charCount += 1
        avg = charCount / len(wordList)
        print("Average word length: {:.2}".format(avg))
        line_num += 1
