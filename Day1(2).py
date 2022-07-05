fir = "Anu"
sec = "Nallatt"
ini = "N"
first = input("Enter your first name:")
if fir == first:
    second = input("Enter your second name:")
    if sec == second:
        initial = input("Enter your initial:")
        if ini == initial:
            print(first, second, initial)
        else:
            print("You entered a wrong initial")
    else:
        print("You entered wrong second name")
else:
    print("you entered wrong name")
