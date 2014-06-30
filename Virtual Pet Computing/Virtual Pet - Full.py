class VirtualPet:
    """A representation of a pet"""

    def __init__(self,name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        print("My name is {0}".format(name))
    #methods
    def talk(self):
        print("Hi, I'm your virtual pet")

    def Feed(self):
        print("What would you like me to eat?")
        Food = input()
        if Food == "":
            print("You fed your pet nothing. You cruel person")
        else:
            print("I just ate a {0}".format(Food))
            self.hunger = self.hunger + 1
            self.energy = self.energy + 1
        
def main():
    PetName = GetName()
    print(PetName)
    PetName = VirtualPet(PetName)
    Chosen = False
    while not Chosen:
        DisplayMenu()
        Choice = input()
        if Choice == 1:
            Feed()
        elif Choice == 2:
            Talk()
        elif Choice == 3:
            Play()
        elif Choice == 4:
            Gym()
        elif Choice == 5:
            Quest()
        elif Choice == 6:
            Shop()
        elif Choice == 7:
            Stats()
        elif Choice == 8:
            Inventory()
        elif Choice == 9:
            Hospital()
        elif Choice == 0:
            exit

def GetName():
    valid = False
    print("Welcome to Tomodachi Life. First we need to name your pet.")
    print("What would you like to call your pet?")
    while not valid:
        Name = input()
        if Name == "":
            print("Please type something for the name")
        else:
            return Name
    
def DisplayMenu():
    print("*** Tomodachi Life ***")
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
    print()

if __name__ == "__main__":
    main()
