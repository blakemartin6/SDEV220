# Blake Martin:
# Martin_M02_Lab
# This program is intended to accept student names and GPAs
# then test to see if they qualify for the deans list or honor roll


while True:
    name = input("Enter your last name here: ")

    if name == "ZZZ":  # quit
        break
    gpa = float(input("Enter your GPA here: "))
    if gpa >= 3.5:
        print("Congradulations " + name + "you have made the Dean's list! ")
    elif gpa > 3.5 and gpa > 3.25:
        print("Congradulations " + name + "you have made the Honor Roll ")
    else:
        print("Sorry you didn't make the honor roll ")
        continue
