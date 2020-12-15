from pet import Pet, CuddlyPet
from toy import Toy
from treat import ColdPizza, Bacon, VeganSnack
from menu import Menu

pets = []

adoption_menu = [
    'Pet',
    'Cuddly Pet'
]

main_menu = [
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Give a Toy to all of your pets",
    "Give pet a treat",
    "Do nothing",
]

treat_menu = [
    "Cold Pizza",
    "Bacon",
    "VeganSnack"
]


def main():
    app = Menu("Please choose an option:", main_menu)
    types = Menu("Please choose a type of pet:", adoption_menu)
    treats = Menu("Please choose a treat:", treat_menu)
    # for each_treat in treats:
    #     Treat(each_treat, each_treat[0], each_treat_[1])
    while True:
        choice = app.get_user_choice()
        if choice == 1:
            pet_name = input("What would you like to name your pet? ")
            type_choice = types.get_user_choice()
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(CuddlyPet(pet_name))
            print("You now have %d pets" % len(pets))
        if choice == 2:
            for pet in pets:
                pet.get_love()
        if choice == 3:
            for pet in pets:
                pet.eat_food()
        if choice == 4:
            for pet in pets:
                print(pet)
        if choice == 5:
            for pet in pets:
                pet.get_toy(Toy())
        if choice == 6:
            treat_choice = treats.get_user_choice()
            if treat_choice == 1:
                for pet in pets:
                    pet.get_treat(ColdPizza())
            if treat_choice == 2:
                for pet in pets:
                    pet.get_treat(Bacon())
            if treat_choice == 3:
                for pet in pets:
                    pet.get_treat(VeganSnack())
        if choice == 6:
            for pet in pets:
                pet.be_alive()


main()
