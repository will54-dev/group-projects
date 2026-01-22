#Dictionaries 
weapons={ #weapons that character has

}
inventory={ #items that player has

}
skills={ #class/race/feat Features

}
spells={ #spells and their descriptions

}
#lists
prof=[] #proficiencies in weapons, tools, armor, shields and skills

#tuples
dictionaries=() #tuple of the dictionary names


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
#view function (prints dictionary contents name and info)
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
#Search (ask what they want to search by (effect or name) and print any weapons that fulfil the requirements)
def search(dictionary):
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
#main function for selection how you are editing the dictionary
def edit(dictionary,tuple,num):
    while True:
        print(f"1:View your {tuple[num]}\n2:add to {tuple[num]}\n3:remove a {tuple[num]}\n4:search {tuple[num]} for specific name/attribute\n5:Exit editor\nWhich option do you want to use?")
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
    return dictionary
#User input for choosing dictionary to edit
def choice(tuple,weapons,skills,inventory,spells):
    print(f"What would you like to edit?")
    for i in range(0,len(tuple)):
        print(f"{i+1}:{tuple[i]}")
    inp=ensure(1,len(tuple)+1)
    if inp==1:
        edit(weapons,tuple,0)
        return weapons
    if inp==2:
        edit(skills,tuple,1)
        return skills
    if inp==3:
        edit(inventory,tuple,2)
        return inventory
    if inp==4:
        edit(spells,tuple,3)
        return spells
edit(weapons)