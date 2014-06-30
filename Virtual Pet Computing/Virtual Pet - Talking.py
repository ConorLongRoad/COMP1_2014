class VirtualPet:
    """a representation of a pet"""

    #methods
    def talk(self):
        print("Hi, I'm your virtual pet")

def main():
    #Creates an instance of the class
    pet_one = VirtualPet()
    #Calls the talk method
    pet_one.talk()

if __name__ == "__main__":
    main()
