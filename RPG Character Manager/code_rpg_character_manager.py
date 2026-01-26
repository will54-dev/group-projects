# WH, SH, JQ 2nd

from will_code_rpg import character_creator
class itme:
    weight = int()
    value = str()
    description = str()

class character:
    class_ch = str()
    race = str()
    level = int()
    strenght = str()
    dexterity = str()
    wisdom = str()
    charisma = str()
    intelligence = str()
    constitution =str()
    inventory = dict()
    weapons = dict()
    spells = dict()
    Equipment_slots = dict()

characters = dict()
races = {


}
classes = {


}

def main_menu():
    while True:
        match input("Do you ant to (as a number).\n1: Make a character \n2: Edit a character \n3: Compare a character \n4: Exit").strip():
            case "1":
                character_creator()
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case _:
                pass