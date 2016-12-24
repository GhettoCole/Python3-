#  Given's way

print("Exercise - 7 (Derek banas test)\n")

# Make a unicode encryption program

norm_string = input("Enter a string to hide in uppercase: ")  # Prompt the user for input in uppercase

secret_string = ""  # Variable set to nothing
for char in norm_string:  # for each letter in the norm_string
    secret_string += str(ord(char))  # increment the secret_string by each character with a unicode string

print("Secret message: ", secret_string)  # finally print the unicode string altogether

norm_string = ""  # set the norm_string to nothing
for i in range(0, len(secret_string) - 1, 2):  # starting at 0 and decrementing the length, take 2 numbers as unicode
    char_code = secret_string[i] + secret_string[i + 1]  # make new variable and set it secret string
    # indexed by i(2 numbers of unicode) and index secret string by another i + one to increment the length
    norm_string += chr(int(char_code))  # normal message = each char of an integer of the char_code converted to (chr)

print("Original message: ", norm_string)  # finally print the normal string altogether

norm_string = input("Enter a string (case-insensitive): ")  # Prompt the user for input in uppercase

secret_string = ""  # Variable set to nothing
for char in norm_string:  # for each letter in the norm_string
    secret_string += str(ord(char) - 23)  # increment the secret_string by each character with a unicode string

print("Secret message: ", secret_string)  # finally print the unicode string altogether

norm_string = ""  # set the norm_string to nothing
for i in range(0, len(secret_string) - 1, 2):  # starting at 0 and decrementing the length, take 2 numbers as unicode
    char_code = secret_string[i] + secret_string[i + 1]  # make new variable and set it secret string
    # indexed by i(2 numbers of unicode) and index secret string by another i + one to increment the length
    norm_string += chr(
        int(char_code) + 23)  # normal message = each char of an integer of the char_code converted to (chr)

print("Original message: ", norm_string)  # finally print the normal string altogether
