#Dictionaries 
weapons={ #weapons that character has

}
inventory={ #items that player has

}
spells={ #spells and their descriptions

}



cls="wizard"
#tuples
if cls=="wizard":
    dictionaries=(weapons,inventory,spells) #tuple of the dictionary names
else:
    dictionaries=(weapons,inventory)

#number ensure function (make sure user input is a number)
def insure():
    while True:
        num=input()
        if f"{num}".isnumeric() and  int(num):
            return int(num)
        else:
                print("Please enter a valid input")
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
def view(dictionary,dictname):
    for key in dictionary:
        if dictname=="weapons"or"inventory":
            print(f"{key}:{dictionary[key][0]}, value:{dictionary[key][1]}, weight:{dictionary[key][2]}")
        elif dictname=="spells":
            print(f"{key}:{dictionary[key][0]}, level:{dictionary[key][1]}, casting:{dictionary[key][2]}")
#Add function (asks user for Weapon name, asks user for Weapon info, adds them to a dictionary)
def plus(dictionary,dictname):
    name=input(f"What is the name of the item you would like to add to your inventory?\n")
    info=input(f"What is information you would like to give {name}?\n")
    match dictname:
        case "weapons":
            print(f"What is the value of {name}?")
            value=insure()
            print(f"What is the weight of {name}?")
            weight=insure()
            dictionary[name]=[info,value,weight]
            print(f"{name} added to inventory")
        case "inventory":
            print(f"What is the value of {name}?")
            value=insure()
            print(f"What is the weight of {name}?")
            weight=insure()
            dictionary[name]=[info,value,weight]
            print(f"{name} added to inventory")
        case "spells":
            print(f"What level of spell is {name}?")
            spellev=insure()
            time=input(f"What is the casting time of {name}?")
            dictionary[name]=[info,spellev,time]
            print(f"{name} added to inventory")
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
            print(f"{inp}:{dictionary[inp][0]}, value:{dictionary[inp][1]}, weight:{dictionary[inp][2]} ")
        else:
            print(f"{inp} not in inventory")
    if bol==2:
        for i in range(0,len(key)):
            if f'{inp}' in dictionary[key[i]][0]:
                print(f"{key[i]}:{dictionary[key[i]][0]}, value:{dictionary[key[i]][1]}, weight:{dictionary[key[i]][2]}")
            else:
                continue
#main function for selection how you are editing the dictionary
def edit(dictionary,dictname):
    while True:
        print(f"1:View your {dictname}\n2:add to {dictname}\n3:remove a {dictname}\n4:search {dictname} for specific name/attribute\n5:Exit editor\nWhich option do you want to use?")
        inp=ensure(1,6)
        if inp==1:
            view(dictionary,dictname)
        elif inp==2:
            plus(dictionary,dictname)
        elif inp==3:
            minus(dictionary)
        elif inp==4:
            search(dictionary)
        elif inp==5:
            break
    return dictionary
#User input for choosing dictionary to edit
def choice(tuple):
    print(f"What would you like to edit?\n1:weapons\n2:inventory")
    if cls=="wizard":
        print("3:spells")
    inp=ensure(1,len(tuple)+1)
    if inp==1:
        edit(weapons,"weapons")
        return weapons
    if inp==2:
        edit(inventory,"inventory")
        return inventory
    if inp==3:
        edit(spells,"spells")
        return spells
choice(dictionaries)