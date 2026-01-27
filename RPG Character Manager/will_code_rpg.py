# WH 2nd 

characters = dict()
modifer_list = {
    "human": (1,2,3,4,5,6,7)

}

def help_isint_input(text):
    while True:
        want = input(text)
        try:
            return int(want)
        except:
            try:
                return float(want)
            except:
                print("Not a number.")

def modifier_selector(text, modifer_list):
    print(f"what {text} do you want?")
    count = 0
    list_to_modifer = list()
    for class_race in modifer_list.keys():
        list_to_modifer.append(class_race)
        count += 1
        print(f"{count}: {class_race}")
    want = input()

    try:
        class_race = modifer_list[want.strip()]
        class_race = want
    except:
        try:
            class_race = modifer_list[]

def character_creator(characters = dict):
    character_name = input("What is the new character's name?\n")
    new_character = dict()
    text = ["level","strength","dexterity","wisdom","charisma","intelligence","constitution"]
    for item in text:
        new_character[item] = help_isint_input(f"What is {character_name}'s {item}?\n")
    characters[character_name] = new_character
    return characters

modifier_selector("race",modifer_list)