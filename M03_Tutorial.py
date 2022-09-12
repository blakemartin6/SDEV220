# This is for M03 Tutorial - Functional Vs OOP

class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

# orange cat who likes lasagna
garfield = Cat("garfield", 8)
# might be jerry I'm not sure
tom = Cat("tom", 3)
# cat who showed up on our porch and has stayed for 10 years
frenzy = Cat("frenzy", 10)

# 2 Create a function that finds the oldest cat


def oldest_cat(*args):
    return max(args)


# 3 Print out the oldest aged cat
print(
    f"The oldest cat is {oldest_cat(garfield.age, tom.age, frenzy.age)} years old.")
