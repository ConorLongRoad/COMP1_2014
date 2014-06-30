class VirtualPet:
    """a representation of a pet"""

    def __init__(self,name):
        self.name = name
        print("My name is {0}".format(name))
    #methods
    def talk(self):
        print("Hi, I'm your virtual pet")

def main():
    name = input("Please enter a name: ")
    #Creates an instance of the class
    pet_one = VirtualPet(name)
    #Calls the talk method
    pet_one.talk()

if __name__ == "__main__":
    main()
