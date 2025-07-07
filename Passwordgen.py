
import random
import pyperclip

passwordrequest = input("Would you like to generate a password? (Y or N): ")

passwordcharacters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "=", "+"
]
if passwordrequest.lower() == "y":
    length = 24
    password = "".join(random.choice(passwordcharacters) for _ in range(length))
    print ("password: ", password)
    
elif passwordrequest.lower() == "n":
    print ("Goodbye.")


if passwordrequest.lower() == "n":
    exit()
else:
    clipboard = input("Would you like to copy to clipboard? (Y or N): ")
if clipboard.lower() == "y":
    pyperclip.copy(password)
    print ("Copied to clipboard.")
else:
    print ("Goodbye.")


