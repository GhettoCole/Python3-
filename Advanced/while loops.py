# Given's way 

print("Exercise - 8 (Derek banas test)")

# Instructions 
# Create a guessing game that prompts the user to guess a number between 0 and 10 
# And continuously ask the user for the number until they guess it
secret_number = 7

while True:
    # noinspection PyBroadException
    try:
        guess = int(input("Guess the number between 1 & 10: "))  # Prompting user for input

        if guess == secret_number:  # conditional to check provided data
            print("Congrats You Guessed it")
            break
        elif guess > secret_number:
            print("Guess lower than that")

        elif guess < secret_number:
            print("Guess higher than that")

    except:
        print("An error occurred due to the data type entered!")
