print("Activity - 10 (derek banas test)")

message = input("Enter message: ")  # Prompt the user to enter a message
key = int(input("How many letters to shift: "))  # The shift of numbers from 1 to 26

secret = ""  # secret is set to nothing

for char in message:  # For each character in the message entered
    if char.isalpha():  # If each of the characters are alphabets
        char_code = ord(char)  # Then set the variable (char_code) to the the unicode of the character
        char_code += key  # And then increment the character by the number of keys entered!

        if char.isupper():  # If the character is uppercase
            if char_code > ord("Z"):  # And the unicode of the character is > than unicode Z
                char_code -= 26  # Then simply just decrement the character by 26

            if char_code < ord("A"):  # And if the unicode of the character is  < than unicode A
                char_code += 26  # Then simply just increment the character by 26

        else:
            if char_code > ord("z"):  # Else(-if) the unicode of the character is > z
                char_code -= 26  # Then decrement by 26

            if char_code < ord("a"):  # Else(-if) the unicode of the character is < a
                char_code += 26  # Then incrememt by 26
        secret += chr(char_code)  # And finally increment the secret by the original character of its unicode
    else:
        secret += char  # Else(unless) the character entered by the user is not a text-type, then leave as is

print("Encrypted: ", secret)  # Finally print out the encrypted message

key = -key  # Decrement the key entered to return to the original value
original = ""  # Set the original to nothing

for char in secret:  # If the character in the secret
    if char.isalpha():  # is an alphabet then
        char_code = ord(char)  # set the char_code to the unicode of the character of the secret message
        char_code += key  # increment the char_code by the -key so that it can shift back to the original form

        if char.isupper():  # If the char of the secret is uppercase
            if char_code > ord("Z"):  # And if the char_code is > unicode of Z
                char_code -= 26  # then decrement the value by 26

            if char_code < ord("A"):  # And if the char_code is < unicode of A
                char_code += 26  # then increment the value by 26

        else:
            if char_code > ord("z"):  # And if the char_code is > unicode of z
                char_code -= 26  # then decrement the value by 26

            if char_code < ord("a"):  # And if the char_code is < unicode of z
                char_code += 26  # then increment the value by 26
        original += chr(char_code)  # And finally increment the secret by the original character of its unicode
    else:
        original += char  # Else(unless) the character entered by the user is not a text-type, then leave as is
print("Decrypted: ", original)  # Finally print out the Decrypted message
