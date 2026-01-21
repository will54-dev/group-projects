#Weapon Dictionary
weapons={

}
dictionaries=[]

def select(dictionaries):
    print
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
        print(f"{key}:{dictionary[key]}")
#Add function (asks user for Weapon name, asks user for Weapon info, adds them to a dictionary)
def plus(dictionary):
    name=input(f"What is the name of the item you would like to add to your inventory?\n")
    info=input(f"What is information you would like to give {name}?\n")
    dictionary[name]=info
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
                print(f"{key[i]}:{dictionary[key[i]]}")
            else:
                continue
#main function for loop
def main(dictionary):
    while True:
        print(f"1:View your weapons\n2:add weapon to inventory\n3:remove item from inventory\n4:search inventory for specific weapon/attribute\n5:Exit calculator\nWhich option do you want to use?")
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

main(weapons)