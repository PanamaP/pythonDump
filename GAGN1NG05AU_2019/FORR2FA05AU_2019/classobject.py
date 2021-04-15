class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Heiti: {self.name} Aldur: {self.age}"
    def sing(self, song):
        return f"{self.name} sings {song}"

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
#print(f"Blu is a {blu.__class__.species}")
#print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
#print("{} is {} years old".format( blu.name, blu.age))
#print("{} is {} years old".format( woo.name, woo.age))
print(blu.sing("heim"))
print(blu)