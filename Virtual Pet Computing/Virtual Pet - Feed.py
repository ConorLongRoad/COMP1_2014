class VirtualPet:
    """a representation of a pet"""

    def __init__(self,name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        print("My name is {0}".format(name))
    #methods
    def talk(self):
        print("Hi, I'm your virtual pet")

    def feed(self, food):
        self.hunger = self.hunger - 1
        print("I just ate a {0}".format(food))
        self.energy = self.energy + 1
        
def main():
    name = input("Please enter a name: ")
    pet_one = VirtualPet(name)
    selected = False
    while not selected:
    #Creates an instance of the class
    #Calls the talk method
        pet_one.talk()
        Food = input("What would you like to feed your pet?")
        print(pet_one.energy)
        pet_one.feed(Food)
        print(pet_one.energy)

if __name__ == "__main__":
    main()

def DisplayMenu():
    print()
    print("Would would you like to do with your pet? ")
    print()
    print("1. Feed your pet food")
    print("2. Talk to your pet")
    print("3. Play with your pet")
    print("4. Take your pet to the gym")
    print("5. Take your pet on a quest")
    print("6. Buy your pet something")
    print("7. Check your pets stats")
    print("8. Check your pets loot")
    print("9. Take your pet to the hospital")
    print("0. Exit")
