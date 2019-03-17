# The following program, bouncer.py, determines whether the user can enter the club or not.

age = input("How old are you: ")

if age:
    age = int(age)
    if 18 <= age < 21: # if age >= 18 and age < 21:
        print("You can enter, but need a wristband!")
    elif age >= 21:
        print("You are good to enter and can drink!")
    else:
        print("You can't come in, little one! :(")
else:
    print("Please enter an age!")
