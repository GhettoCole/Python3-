import os

with open("data.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("I love programming, It's like writing poetry, it soothes your mind!\n"
                 "One day I wanna write my own project"
                 ".\nCoding is the only activity that energises me and give me a reason to do something")

with open("data.txt", encoding="utf-8") as myFile:
    print(myFile.read())

print(myFile.name)  # Checking the file name
print(myFile.mode)  # Returns 'r' for read mode

os.rename("data.txt", "coding.txt")
os.remove("coding.txt")
os.mkdir("Test")
os.chdir("Test")
print("Current directory: ", os.getcwd())
os.chdir("..")
print("Current directory: ", os.getcwd())
os.rmdir("Test")