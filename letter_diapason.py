import string

diapason = input("Input 2 letters with (-) between them: ")

alphabet = string.ascii_letters

first_letter = diapason[0]
second_letter = diapason[2]

start = alphabet.index(first_letter)
end = alphabet.index(second_letter)

diapason = alphabet[start:end+1]
print(diapason)


