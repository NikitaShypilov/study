import string
import keyword

name = input("Input name of variable: ")

if name in keyword.kwlist:
    print(False)

elif name and name[0].isdigit():
    print(False)

elif any(ch.isupper() for ch in name):
    print(False)

elif any(ch in string.punctuation.replace("_", "") or ch.isspace() for ch in name):
    print(False)

elif name.count("_") > 1:
    print(False)

elif "__" in name:
    print(False)

elif not name:
    print(False)

else:
    print(True)
