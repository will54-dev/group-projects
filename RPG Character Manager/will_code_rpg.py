# WH 2nd 

class character:
    class_ch = str()
    race = str()
    level = int()
    strength = str()
    dexterity = str()
    wisdom = str()
    charisma = str()
    intelligence = str()
    constitution =str()
    inventory = dict()
    weapons = dict()
    spells = dict()
    Equipment_slots = dict()

def help_isint_input(text):
    want = input(text)
    try:
        return int(want)
    except:
        try:
            return float(want)
        except:
            print("Not a number.")

def modifier_selector(text, modifer_list):
    pass
def character_creator(characters):
    character_name = input("What is the new character's name?")
    new_character = character
    text = ["level","strength","dexterity","wisdom","charisma","intelligence","constitution"]
    modifier = [new_character.level,new_character.strength,new_character.dexterity,new_character.level,new_character.level,new_character.level]
    for item in range(len(text)):
        new_character.level = help_isint_input(f"")