#Weapon Dictionary
weapons={

}
dictionaries=[]


#number ensure function (make sure user input is a number(with parameters)
def ensure(l,h):
    while True:
        num=input()
        if l and h:
            if f"{num}".isnumeric() and  int(num) in range(l,h):
                return int(num)
            else:
                print("Please enter a valid input")
        else:
            if f"{num}".isnumeric():
                return int(num)
            else:
                print("Please enter a valid input")
#view function (prints Weapon name and info)
def view(dictionary):
    for key in dictionary:
        print(f"{key}:{dictionary[key][0]},{dictionary[key][1]},{dictionary[key][2]}")
#Add function (asks user for Weapon name, asks user for Weapon info, adds them to a dictionary)
def plus(dictionary):
    name=input(f"What is the name of the item you would like to add to your inventory?\n")
    info=input(f"What is information you would like to give {name}?\n")
    value=input(f"What is the value of {name}?\n")
    weight=input(f"What is the weight of {name}?\n")
    dictionary[name]=[info,value,weight]
    print(f"{name}:{dictionary[name]}")
    return dictionary
#Remove function (print dictionary, asks user for number Weapon that they want to remove,removes them to a dictionary)
def minus(dictionary):
    print("Note: If you remove it you will have to manually add it back!")
    name=input(f"Which item would you like to remove from your inventory?\n")
    if name in dictionary:
        del dictionary[name]
        print(f'{name} has been removed')
    else:
        print(f"{name} wasn't found in inventory")
    return dictionary
#Search (ask what they want to search by (effect or name) and print any weapons that fufil the requirements)
def search_inventory(dictionary):
    key=list(dict(dictionary).keys())
    print("How would you like to search your inventory\n1. name\n2. feature")
    bol=ensure(1,3)
    inp=input("What are you searching for?")
    if bol==1:
        if inp in dictionary:
            print(f"{inp}:{dictionary[inp]}")
        else:
            print(f"{inp} not in inventory")
    if bol==2:
        for i in range(0,len(key)):
            if f'{inp}' in dictionary[key[i]]:
                print(f"{key[i]}:{dictionary[key[i]][0]},{dictionary[key[i]][1]},{dictionary[key[i]][2]}")
            else:
                continue
def compare_characters:
    compare_first_character = input(characters, "Select your first character.\n")
    while compare_first_character not in characters:
        print("Try again. That character doesn't exit yet. :(")
        compare_first_character = input(characters, "Select your first character.\n")       
    compare_second_character = input(characters, "Select your second character.\n")
    while compare_second_character not in characters:
        print("Try again. That character doesn't exit yet. :(")
        compare_second_character = input(characters, "Select your first character.\n")  
def search_for_player:
    stat_to_search_by = input("What stat would you like to search by, race, class, level, str, dex, cha, int, or name?\n").strip().lower()
    if stat_to_search_by == "race":
        search_race = input("What is their race?\n").strip()
    elif stat_to_search_by == "class":
        search_class= input("What is their class?\n").strip()
    elif stat_to_search_by == "level":
        search_level= input("What is their level?\n").strip()
    elif stat_to_search_by == "str":
        search_str = input("What is their strength?\n").strip()
    elif stat_to_search_by == "dex":
        search_dex = input("What is their dexterity?\n").strip()
    elif stat_to_search_by == "cha":
        search_cha = input("What is their charisma?\n").strip()
    elif stat_to_search_by == "int":
        search_int = input("What is their intelligence?\n").strip()
    elif stat_to_search_by == "name":
        search_name = input("What is their name?\n").strip()
    else:
        print("That isn't a stat.")
#main function for loop
def edit(dictionary):
    while True:
        print(f"1:View your weapons\n2:Add weapon to inventory\n3:Remove item from inventory\n4:Search inventory for specific weapon/attribute\n5:Exit\n6:Compare characters\n7:Search for a player\nWhich option do you want to use?")
        inp=ensure(1,6)
        if inp==1:
            view(dictionary)
        elif inp==2:
            plus(dictionary)
        elif inp==3:
            minus(dictionary)
        elif inp==4:
            search(dictionary)
        elif inp==5:
            break
        elif inp==6:
            compare_characters
        elif inp==7:
            search_for_player
#User input for choosing dictionary to edit
def choice(list,weapons,spells,skills,inventory):
    pass

edit(weapons)