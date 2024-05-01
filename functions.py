import random

def selection():
    # The menu of ancestries
    common_ancestry = ["Dwarf", "Elf", "Gnome", "Goblin", "Halfling", "Leshy", "Orc"]
    uncommon_ancestry = ["Azarketi", "Catfolk", "Fetchling", "Gnoll", "Grippli", "Hobgoblin",
                         "Kitsune", "Kobold", "Lizardfolk", "Nagaji", "Ratfolk", "Tengu",
                         "Vanara"]
    rare_ancestry = ["Anadi", "Android", "Automaton", "Conrasu", "Fleshwarp", "Ghoran", "Goloma",
                     "Kashrishi", "Poppet", "Shisk", "Shoony", "Skeleton", "Sprite", "Strix", "Vishkanya"]

    # Creates the gender
    gender_select = random.randrange(start=1, stop=10)
    gender = ""
    if gender_select in range(1,4):
        gender = "Male"
    elif gender_select in range (5,9):
        gender =  "Female"
    else:
        gender = "Other"

    # Finds out what ancestry the NPC is
    ancestry = ""
    human_chance = random.randrange(start=1, stop=10)
    if human_chance in range(1,5):
        ancestry = "Human"
    else:
        commonality = random.randrange(start=1, stop=10)
        if commonality in range(1,7):
            ancestry = random.choice(common_ancestry)
        elif commonality in range(8,9):
            ancestry = random.choice(uncommon_ancestry)
        else:
            ancestry = random.choice(rare_ancestry)

    # Print it
    npc = f"The NPC is a {gender} {ancestry}"
    return npc

def print_NPCs():
    num_input = int(input("How many NPCs do you want to create? "))
    for i in range(num_input):
        print(selection())