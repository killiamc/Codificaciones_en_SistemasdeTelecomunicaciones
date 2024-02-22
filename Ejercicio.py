user_word = input("Ingresa tu palabra: ")
# user_word = user_word.upper()
segunda = ""

for letter in user_word:
    if letter == "a" or letter =="A":
        letter = ""
    elif letter == "e" or letter =="E":
        letter = ""
    elif letter == "i" or letter =="I":
        letter = ""
    elif letter == "o" or letter =="O":
        letter = ""
    elif letter == "u" or letter =="U":
        letter = ""
    else:
        letter = letter
    segunda = segunda+letter

print(segunda)