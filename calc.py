while True:

    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    action = input("Enter the action + or - or * or /:")

    if action == "+":
        print(f"Result: {n1} + {n2} = {n1 + n2}")

    elif action == "-":
        print(f"Result: {n1} - {n2} = {n1 - n2}")

    elif action == "*":
        print(f"Result: {n1} * {n2} = {n1 * n2}")

    elif action == "/":
        if action == "/" and n2 == 0:
            print('Cant solve')
        else:
            print(f"Result: {n1} / {n2} = {n1 / n2}")

    cont = input("Want to continue? (y/n): ")
    if cont != "y":
        print("Bye!")
        break