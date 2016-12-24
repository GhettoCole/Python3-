try:
	myFile = open("mydata2.txt", encoding="utf-8")
	#myFile2 = open("mydata3.txt", encoding="utf-16") # Demostrating an error

except FileNotFoundError as ex:
	print("That file isn't found")

	print(ex.args)

else:
	print("File:\n", myFile.read())
	myFile.close()

finally:
	print("Finished working with the file")
