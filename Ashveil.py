############################################ LIBRARIES AND GLOBAL VARIABLES ############################################
import random
import urllib.request
import re
from collections import Counter

source = "https://rawcdn.githack.com/uberspot/OpenTriviaQA/master/categories/general"
karma = 0
bag = ["potion", "poison"]

############################################ ASCII ART TITLES FOR GAME, LEVELS AND FINISHES ############################################
def show_intro():
    print("\033[38;5;214m***********************************************************************************\033[0m")
    print("\033[38;5;214m***********************************************************************************\033[0m")
    print("\033[38;5;214m***********************************************************************************\033[0m")
    art = r"""
          __        ________  __    __  ___      ___  _______   __    ___       
         /""\      /"       )/" |  | "\|"  \    /"  |/"     "| |" \  |"  |      
        /    \    (:   \___/(:  (__)  :)\   \  //  /(: ______) ||  | ||  |      
       /' /\  \    \___  \   \/      \/  \\  \/. ./  \/    |   |:  | |:  |      
      //  __'  \    __/  \\  //  __  \\   \.    //   // ___)_  |.  |  \  |___   
     /   /  \\  \  /" \   :)(:  (  )  :)   \\   /   (:      "| /\  |\( \_|:  \  
    (___/    \___)(_______/  \__|  |__/     \__/     \_______)(__\_|_)\_______) 
    
    """
    print(f"\033[38;5;214m{art}\033[0m")
    print("\033[38;5;214m***********************************************************************************\033[0m")
    print("\033[38;5;214m***********************************************************************************\033[0m")
    print("\033[38;5;214m***********************************************************************************\033[0m")
    print("You wake up in a strange place...")
    print("You equip a sword and open the door. The light blinds you.")
    print(f"\n\033[1;4;33mInn\033[0m")

def level_one():
    print("\033[38;5;68m==============================================================\033[0m")
    print("\033[38;5;68m==============================================================\033[0m")
    print("\033[38;5;68m==============================================================\033[0m")
    art = r"""
           _                   _    ___             
          | |    _____   _____| |  / _ \ _ __   ___ 
          | |   / _ \ \ / / _ \ | | | | | '_ \ / _ \
          | |__|  __/\ V /  __/ | | |_| | | | |  __/
          |_____\___| \_/ \___|_|  \___/|_| |_|\___|
        
        """
    print(f"\033[38;5;68m{art}\033[0m")
    print("\033[38;5;68m==============================================================\033[0m")
    print("\033[38;5;68m==============================================================\033[0m")
    print("\033[38;5;68m==============================================================\033[0m")

def level_two():
    print("\033[36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
    print("\033[36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
    print("\033[36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
    art = r"""
            _                   _   _____               
           | |    _____   _____| | |_   _|_      _____  
           | |   / _ \ \ / / _ \ |   | | \ \ /\ / / _ \ 
           | |__|  __/\ V /  __/ |   | |  \ V  V / (_) |
           |_____\___| \_/ \___|_|   |_|   \_/\_/ \___/ 
        
        """
    print(f"\033[36m{art}\033[0m")
    print("\033[36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
    print("\033[36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
    print("\033[36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")

def level_three():
    print("\033[31m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[0m")
    print("\033[31m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[0m")
    print("\033[31m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[0m")
    art = r"""
          _                   _   _____ _                   
         | |    _____   _____| | |_   _| |__  _ __ ___  ___ 
         | |   / _ \ \ / / _ \ |   | | | '_ \| '__/ _ \/ _ \
         | |__|  __/\ V /  __/ |   | | | | | | | |  __/  __/
         |_____\___| \_/ \___|_|   |_| |_| |_|_|  \___|\___| 
        
        """
    print(f"\033[31m{art}\033[0m")
    print("\033[31m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[0m")
    print("\033[31m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[0m")
    print("\033[31m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[0m")

def bad_ending():
    print("\033[38;5;52m----------------------------------------------------------\033[0m")
    print("\033[38;5;52m----------------------------------------------------------\033[0m")
    print("\033[38;5;52m----------------------------------------------------------\033[0m")
    art = r"""
        
          █████▒██▓ ███▄    █  ██▓  ██████  ██░ ██ 
        ▓██   ▒▓██▒ ██ ▀█   █ ▓██▒▒██    ▒ ▓██░ ██▒
        ▒████ ░▒██▒▓██  ▀█ ██▒▒██▒░ ▓██▄   ▒██▀▀██░
        ░▓█▒  ░░██░▓██▒  ▐▌██▒░██░  ▒   ██▒░▓█ ░██ 
        ░▒█░   ░██░▒██░   ▓██░░██░▒██████▒▒░▓█▒░██▓
         ▒ ░   ░▓  ░ ▒░   ▒ ▒ ░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒
        ░      ▒ ░░ ░░   ░ ▒░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░
        ░ ░    ▒ ░   ░   ░ ░  ▒ ░░  ░  ░   ░  ░░ ░
        ░           ░  ░        ░   ░  ░  ░
        
        """
    print(f"\033[38;5;52m{art}\033[0m")
    print("\033[38;5;52m----------------------------------------------------------\033[0m")
    print("\033[38;5;52m----------------------------------------------------------\033[0m")
    print("\033[38;5;52m----------------------------------------------------------\033[0m")

def good_ending():
    print("\033[38;5;172m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m")
    print("\033[38;5;172m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m")
    print("\033[38;5;172m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m")
    art = r"""
       ._______.___ .______  .___ .________.___.__  
        :_ ____/: __|:      \ : __||    ___/:   |  \ 
        |   _/  | : ||       || : ||___    \|   :   |
        |   |   |   ||   |   ||   ||       /|   .   |
        |_. |   |   ||___|   ||   ||__:___/ |___|   |
          :/    |___|    |___||___|   :         |___|
          :    

        """
    print(f"\033[38;5;172m{art}\033[0m")
    print("\033[38;5;172m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m")
    print("\033[38;5;172m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m")
    print("\033[38;5;172m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m")

############################################ GAME MECHANICS ############################################
def questions(source):
    with urllib.request.urlopen(source) as response:
        result = response.read().decode("utf-8", errors="replace")

    blocks = result.strip().split("\n\n")

    def randomise():
        block = random.choice(blocks)
        filtered_lines = []
        answer = []
        correct = None
        option_index = 0

        for line in block.splitlines():
            line = line.strip()

            if line.startswith("^"):
                correct = line[1:].strip()
                continue
            if line.startswith("#Q"):
                formatted_line = f"\033[1;4m{line}\033[0m"
                print(formatted_line)
                filtered_lines.append(formatted_line)
            else:
                display_line = re.sub(r"^[A-Z]\s*", "", line)
                label = chr(65 + option_index)
                print(f"{label}) {display_line}")
                filtered_lines.append(f"{label}) {display_line}")
                answer.append(display_line)
                option_index += 1

        return "\n".join(filtered_lines), block
    
    return randomise

randomise = questions(source)

def health_bar(player_health, villain_health, villain_status=None, max_health= 100):
    def colour_bar(health, status=None):
        bar = ("=" * health) + (" " * (max_health - health))
        if health == 0:
            colour = 130
            # orange 184 forespace 8-bit colour.
        elif 0 < health <= 25:
            colour = 224
            # Blue-ish light pink 224 forespace 8-bit colour.
        elif 26 < health < 50:
            colour = 38
            # Light light yellow 38 forespace 8-bit colour.
        elif 50 <= health < max_health:
            colour = 157
            # Light light green 157 forespace 8-bit colour.
        else:
            # Sharp green 118 forespace 8-bit colour.
            colour = 118
        
        status_text = ""
        if status and status.get("poison"):
            return f"\033[38;5;{colour}m[{bar}] {status['poison']}\033[0m"
        return f"\033[38;5;{colour}m[{bar}{status_text}]\033[0m"
        
    return colour_bar(player_health), colour_bar(villain_health, status = villain_status)

def potion(player_health):
    potion = 50
    player_health += potion
    return player_health

def poison(villian_health, poison_status=None, target_name="Enemy"):

    if poison_status is None:
        poison_status = {
            'poison': "\033[95m(psn)\033[0m",
            'turns': 3,
            'damage': random.randint(5, 15)
        }    
        print(f"\n{target_name} has been poisoned!")
        return villian_health, poison_status

    if poison_status['turns'] > 0:
        villian_health -= poison_status['damage']
        poison_status['turns'] -= 1
        villian_health = max(villian_health, 0)
        print(f"The poison burns! Royal Guard takes {poison_status['damage']} damage ({poison_status['turns']} turns left).")
    else:
        print("The poison has worn off.")
        poison_status = None
    
    return villian_health, poison_status
    
def reward():
    items = ["potion", "poison"]

    reward = random.choice(items)

    return reward

def check_bag(bag):
    for k, v in Counter(bag).items():
        if v > 1:
            print(f"{k}: {v}")
        else:
            print(f"{k}")
    return ""

def items(bag, reward):
    bag.append(reward)
    return bag

def damage():
    damage = random.randint(1, 100)
    return damage

def correct_answer(block):
    lines = [line.strip() for line in block.splitlines() if line.strip()]
    options = []
    correct_text = None
    for line in lines:
        if line.startswith("#Q"):
            continue
        if line.startswith("^"):
            correct_text = line[1:].strip()
        else:
            option_text = re.sub(r"^[A-Z]\s*", "", line)
            options.append(option_text)
    if correct_text is not None:
        correct_index = options.index(correct_text)
        return chr(65 + correct_index)
    return None

def update_karma(change):
    global karma
    karma += change
    return karma

def karma_check(king, princess, dragon, character):
    global karma
    if karma >= 0:
        return cycles_end_good(king, princess, dragon, character)
    else:
        return cycles_end_bad(king, princess, character)
    
def town_names():
    suffixes = ["brook", "shire", "ham", "hamp", "er", "bridge", "brig", "hall", "pool", "don", "ton", "sey", "bry", "cas", "cast", "den", "din"]
    prefixes = ["north", "nor", "ast", "wes", "west", "sud", "pemb", "pem", "cow", "har", "hart", "tren", "pev", "mal", "exe"]
    return random.choice(prefixes).capitalize() + random.choice(suffixes)

def village_names():
    suffixes = ["stoke", "stead", "strat", "wic", "wich", "win", "ray", "day", "say", "ter", "ard", "bed", "de", "tel", "cas", "mer", "shaw", "swin", "tarn", "thorp", "wold", "ward"]
    prefixes = ["ond", "on", "green", "black", "az", "yor", "avon", "ac", "auc", "auck", "ash", "a", "ab", "ad", "ar", "ard", "car", "cros"]
    return random.choice(prefixes).capitalize() + random.choice(suffixes)

def dragon_names():
    dragon_names = ["Drogon", "Rhaegal", "Viserion", "Smaug", "Ancalagon", "Firnen", "Glaedr", "Niner", "Norberta", "Saphira"]

    return random.choice(dragon_names)

dragon = dragon_names()

def female_names(): 
    female_names = ["Yvonnyna,", "Wulfhgytha", "Victricia", "Ursulilla", "Theophanissa", "Susannotte", "Rosiana", "Prudentota", "Osthrith", "Nicholaa", "Melisendyna", "Linet", "Katherinelle", "Julela", "Isotte", "Hrothswith", "Godlgytha", "Florilla", "Etheldreda", "Dominyna", "Cyneflaed", "Bryhtthrith", "Aveletta"]

    return random.choice(female_names)

def male_names():
    male_names = ["Aelfbald", "Beornwald", "Ceolric", "Ealdswith", "Godefroy", "Heward", "Isembert","Jourdyn", "Kjartan", "Laurentius", "Manfredus", "Nigellus", "Ordnoth", "Perceval", "Quentin", "Reymond", "Seaxlaf", "Thurston", "Ulfketil", "Vaughan", "Walterus", "Yrmenwig" ]
    return random.choice(male_names)

def villager_names():
    villager_names = ["Athelric", "Bartholomew", "Cenhelm", "Digory", "Eamon", "Frithuwulf", "Godhere", "Halfdan", "Iohannes", "Johnus", "Kenric", "Leofgar", "Maurice", "Nicolas", "Odda", "Payne", "Quarto", "Radulf", "Sigbald", "Thome", "Uthred", "Vidar", "Wigbert", "Yngvar"]
    return random.choice(villager_names)

def read():
    while True:
        read = input("\n\033[3;38;5;173mContinue?\033[0m \033[96m(Yes/No):\033[0m ").casefold().strip()
        if read == 'yes':
            return True
        elif read == 'no':
            print("You pause, admiring the scenery.")
            continue
        else:
            print("You hesitate.")
            continue

############################################ LEVEL THREE AND GAME END ############################################
def king_fight(king, princess, character):
    print(f"\n\033[1;4;33mCycle's End\033[0m")
    print(f"After hours of travelling you reach the foot of the volcano this will be the final battleground where you will fight King {king}. As you approach the volcano, the king awaits in full armour ready for the final battle. As the volcano roars you stand menacingly as you stare down the king slowly tigtening the grip on your sword.")
    read()

    boss, player = 100, 100
    boss_poisoned = None
    print(f"\n\033[1;4;91m{character}vs. King {king}\033[0m\n")
    while boss > 0 and player > 0:
    
        if boss_poisoned is not None:
            boss, boss_poisoned = poison(boss, boss_poisoned, target_name=f"King {king}")

        player_bar, boss_bar = health_bar(player_health=player, villain_health=boss, villain_status=boss_poisoned)
        print(f"{character}: {player_bar}\nKing {king} {boss_bar}\n")

        option = input("What will you do? (Fight/Use Item): ").casefold().strip()
        if option == "use item":
            itinerary = check_bag(bag)
            print(itinerary)
            item = input("Please select your item: ").casefold().strip()
            match item:
                case "potion":
                    player = potion(player)
                    bag.remove("potion")
                    continue
                case "poison":
                    if boss_poisoned is None:
                        boss, boss_poisoned = poison(boss, None, target_name=f"King {king}")
                    else:
                        print(f"King {king} is already poisoned!")
                    bag.remove("poison")
                    continue
                case _:
                    print("You changed your mind.\n")
                    continue

        elif option == "fight":
            hit = damage()
            query, original_block = randomise()
            correct = correct_answer(original_block)

            answer = input(f"Please select your answer: ").strip().upper()
            if answer == correct:
                print("\nThat is the correct answer!\n")
                boss -= hit
                boss = max(boss, 0)
                continue
            else:
                print(f"\nIncorrect, the correct answer was {correct}\n")
                player -= hit
                player = max(player, 0)
                continue

    if player <= 0:
        print(f"You were defeated by King {king}.\n\n\033[1;38;5;93mKing {king}:\033[0m 'Any last words?'")
        read()
        return cycles_end_bad(king, princess, character)
    else:
        reward_item = reward()
        print(f"King {king} was defeated!\nFor fighting valiantly, you found a {reward_item}.\n")
        inventory = items(bag, reward_item)
        print(f"Updated inventory: {inventory}.")
        read()
        print(f"After you killed King {king} you return to his kingdom to claim the throne for yourself you rule the land with an iron fist.\n")
        print("You were the villain of the story.\n")
        return bad_ending()

def dragon_fight(king, character, dragon, princess):
    print(f"\n\033[1;4;33mCycle's End\033[0m")
    print(f"After hours of travelling you reach the foot of the volcano and have one thing in your mind to slay {dragon}, a quest entrusted to you given by King {king}.\n")
    print("As I approach the volcano, a colossal dragon swoops down with tremendous force. As the volcano roars you stand trembling as you stare down the dragon slowly tigtening the grip on your sword.")
    read()

    boss, player = 100, 100
    boss_poisoned = None
    print(f"\n\033[1;4;91m{character}vs. {dragon}\033[0m\n")
    while boss > 0 and player > 0:
        
        if boss_poisoned is not None:
            boss, boss_poisoned = poison(boss, boss_poisoned, target_name=f"{dragon}")

        player_bar, boss_bar = health_bar(player_health=player, villain_health=boss, villain_status=boss_poisoned)
        print(f"{character}: {player_bar}\n{dragon} {boss_bar}\n")

        option = input("What will you do? (Fight/Use Item): ").casefold().strip()
        if option == "use item":
            itinerary = check_bag(bag)
            print(itinerary)
            item = input("Please select your item: ").casefold().strip()
            match item:
                case "potion":
                    player = potion(player)
                    bag.remove("potion")
                    continue
                case "poison":
                    if boss_poisoned is None:
                        boss, boss_poisoned = poison(boss, None, target_name=f"{dragon}")
                    else:
                        print(f"{dragon} is already poisoned!")
                    bag.remove("poison")
                    continue
                case _:
                    print("You changed your mind.\n")
                    continue

        elif option == "fight":
            hit = damage()
            query, original_block = randomise()
            correct = correct_answer(original_block)

            answer = input(f"Please select your answer: ").strip().upper()
            if answer == correct:
                print("\nThat is the correct answer!\n")
                boss -= hit
                boss = max(boss, 0)
                continue
            else:
                print(f"\nIncorrect, the correct answer was {correct}\n")
                player -= hit
                player = max(player, 0)
                continue

    if player <= 0:
        print(f"You were defeated by the {dragon}. The grab you and throw you up in the air. You land inside its mouth and are swallowed whole.")
        read()
        return cycles_end_good(king, princess, dragon, character)
    else:
        reward_item = reward()
        print(f"The Dragon was defeated!\nFor fighting valiantly, you found a {reward_item}.\n")
        inventory = items(bag, reward_item)
        print(f"Updated inventory: {inventory}.")
        print(f"\n{dragon} falls into the running lava, sinking until there is nothing left to see.\n")
        read()
        print(f"After the dragon has been defeated you go back to the castle to report to King {king} then you marry Princess {princess}.\n")
        print("You were the hero of the story \n")
        return good_ending()

def cycles_end_good(king, princess, dragon, character):
    level_three()

    print(f"\n\033[1;4;33mFoot of volcano\033[0m")
    print(f"You follow the instructions of the dragon through the harshest of lands to get here. This is no mere mountain, it is the scar of a forgotten war, where the earth cracked open and never healed. Its peak is jagged and blackened, crowned with fire that dances like cursed flame. Thunder rolls from its depths, not from storm, but from something ancient stirring below. The ground trembles in its presence. Rivers run dry. Birds flee. Even the bravest warriors speak its name only in hushed tones. The sky split with a roar like a thousand war drums. The volcano has awakened. From its jagged crown burst a pillar of fire and ash, blotting out the sun and casting the land into crimson twilight. Rivers of molten rock surged down its flanks, devouring forest and fortress alike. The ground trembled as if the gods themselves recoiled, and the air turned thick with smoke and fury.Lightning danced through the ash clouds, illuminating the silhouette of the mountain—no longer dormant, but alive with wrath. Villages miles away felt the heat. The wind carried screams and embers. And in the heart of the inferno, some swear they saw a shape rise—wreathed in flame, born of stone and vengeance.")
    read()
    return dragon_fight(king, character, dragon, princess)

def cycles_end_bad(king, princess, character):
    level_three()

    print(f"\n\033[1;4;33mFoot of volcano\033[0m")
    print(f"You chase King {king} through the harshest of lands to get here. This is no mere mountain, it is the scar of a forgotten war, where the earth cracked open and never healed. Its peak is jagged and blackened, crowned with fire that dances like cursed flame. Thunder rolls from its depths, not from storm, but from something ancient stirring below. The ground trembles in its presence. Rivers run dry. Birds flee. Even the bravest warriors speak its name only in hushed tones. The sky split with a roar like a thousand war drums. The volcano has awakened. From its jagged crown burst a pillar of fire and ash, blotting out the sun and casting the land into crimson twilight. Rivers of molten rock surged down its flanks, devouring forest and fortress alike. The ground trembled as if the gods themselves recoiled, and the air turned thick with smoke and fury.Lightning danced through the ash clouds, illuminating the silhouette of the mountain—no longer dormant, but alive with wrath. Villages miles away felt the heat. The wind carried screams and embers. And in the heart of the inferno, some swear they saw a shape rise—wreathed in flame, born of stone and vengeance.")
    read()
    return king_fight(king, princess, character)

############################################ LEVEL THREE START ############################################

############################################ LEVEL TWO END ############################################
def deny_quest(king, wizard, princess, town, character, dragon): 
    guard, player = 100, 100
    guard_poisoned = None

    print(f"\nYou refuse the quest. King {king} eyes you suspiciously.\n\n\033[1;38;5;93mKing {king}:\033[0m 'If not for the kindness of your heart, the rewards is generous. However I must ask. if you are not here for the request, what brings you to this place? To my throne room?'\n\nHe looks to his guards. They have tightened their grip on around their hilts. The servants start to vacate the room. The air has become menacing. King {king} stands, showing his imposing figure.\n\n\033[1;38;5;93mKing {king}:\033[0m 'Perhaps you are here on {wizard}'s behest. Guards, sieze them! You shan't make a fool of me twice.'\n\nThe guards rush at you. They fall to their knees as you fight back. In Royal Guard appears in gold armour, distinguishing them from the others. You brace for impact.")
    read()
    print(f"\n\033[1;4;91m{character}vs. Royal Guard\033[0m\n")
    while guard > 0 and player > 0:
        
        if guard_poisoned is not None:
            guard, guard_poisoned = poison(guard, guard_poisoned, target_name="Royal Guard")

        player_bar, guard_bar = health_bar(player_health=player, villain_health=guard, villain_status=guard_poisoned)
        print(f"{character}: {player_bar}\nRoyal Guard: {guard_bar}\n")

        option = input("What will you do? (Fight/Use Item): ").casefold().strip()
        if option == "use item":
            itinerary = check_bag(bag)
            print(itinerary)
            item = input("Please select your item: ").casefold().strip()
            match item:
                case "potion":
                    player = potion(player)
                    bag.remove("potion")
                    continue
                case "poison":
                    if guard_poisoned is None:
                        guard, guard_poisoned = poison(guard, None, target_name="Royal Guard")
                    else:
                        print("Royal Guard is already poisoned!")
                    bag.remove("poison")
                    continue
                case _:
                    print("You changed your mind.\n")
                    continue
                
        elif option == "fight":
            hit = damage()    
            query, original_block = randomise()
            correct = correct_answer(original_block)

            answer = input(f"\nPlease select your answer: ").strip().upper()
            if answer == correct:
                print("\nThat is the correct answer!\n")
                guard -= hit
                guard = max(guard, 0)
                continue
            else:
                print(f"\nIncorrect, the correct answer was {correct}\n")
                player -= hit
                player = max(player, 0)
                continue

    if player <= 0:
        print(f"You were defeated by the Royal Guard. Satisfied, King {king} thanks the Royal Guard and looms over your weakned body.\n\n\033[1;38;5;93mKing {king}:\033[0m 'Take them to the dungeon where Inquisitor and the Physician can prepare him for questioning.'")
        read()
        return throne_room(king, town, princess, character, dragon)
    else:
        reward_item = reward()
        print(f"The Royal Guard was defeated!\nFor fighting valiantly, you found a {reward_item}.\n")
        inventory = items(bag, reward_item)
        print(f"Updated inventory: {inventory}.")
        print(f"\nThe Royal Guard collapses. They expect the worst but you spare the bloodshed. King {king} holds his sword and shield up defiantly.\n\n\033[1;38;5;93mKing {king}:\033[0m 'I refuse to surrender so meekly. En guarde!'")
        read()
        return karma_check(king, princess, dragon, character)

def courtyard(princess, wizard, king, dragon, character):
    print(f"\n\033[1;4;33mKing {king} Courtyard\n\033[0m")
    print(f"You meet King {king} and inform him of the news.\n\n\033[1;38;5;93mKing {king}:\033[0m 'So it was the great {dragon} who orchestrated all this, not {wizard}. My, they were but a fairytale, a story told through the generations. Who would have believe they existed.'\n\nKing {king} looks at you and the determination in your eyes.")
    read()
    return karma_check(king, princess, dragon, character)
    
def wizards_lair_entrance(princess, wizard, king, character, dragon):
    print(f"\n\033[1;4;33m{wizard}'s Lair Entrance\n\033[0m")
    print(f"You guide Princess {princess} through the icy terrain. The downhill poses a different challenge to the last. She grips you tightly as you make it down the mountain together.\n\nSuddenly, a horrifying screech traverses through the clouds. An ominous shadow becomes larger until it fully emerges from the clouds. A black dragon charges at you, knocking you to the ground. When you recover, Princess {princess} is no where to be found. Her screams catch your attention.\n\n\033[1;38;5;214m{dragon}:\033[0m 'It seems {wizard} has not held his end of the deal. No matter. If you dare to face me, I shall be at Cycle's End.'\n\n{dragon} flies away with Princess {princess} in tow.")
    read()
    return courtyard(princess, wizard, king, dragon, character)

def wizards_lair(mountain, wizard, princess, king, town, character, dragon):
    enemy, player = 100, 100
    enemy_poisoned = None

    print(f"\n\033[1;4;33m{wizard}'s Lair\033[0m")
    print(f"You see a structure of brick and mortar. A menacing place that withstands the bitter cold of {mountain}. The screaming continues. You find a small crevice in one of the outer walls and crawl inside.\n\nThe interior suddenly warms you up. You have landed in a corridor. After surveying the area, you confirm there is no threat.\n\nA voice bellows: 'There's no one to hear you for days.'\n\nYou head over to the direction of the new voice. From there, you observe a gangly man creating potions. The smell is revolting. You see some stairs and descend them.\n\nThey led you to a dungeon. You hear crying in the background. Pinpointing the source, you see a young woman. She sees you and is stunned. You bring your pointer finger to your lips to motion her to stay quiet.\n\n\033[1;38;5;140mPrincess {princess}:\033[0m 'Are you here to rescue me?'")
    read()
    if wizard == king:
        print(f"\nYou nod in response.\n\n\033[1;38;5;140mPrincess {princess}:\033[0m 'Thank you! You will have to pry the keys from {wizard}, he keeps them in his study where he brews those disgusting potions.'\n\nYou leave the dungeon. However as you are about to reach the door of the study, {wizard} await.\n\n\033[1;38;5;88m{wizard}:\033[0m 'So there's someone amongst that copycat's ranks who is capable after all.'")
    else:
        print(f"\nYou nod in response.\n\n\033[1;38;5;140mPrincess {princess}:\033[0m Thank you! You will have to pry the keys from {wizard}, he keeps them in his study where he brews those disgusting potions.\n\nYou leave the dungeon. However as you are about to reach the door of the study, {wizard} await.\n\n\033[1;38;5;88m{wizard}:\033[0m 'So there's someone amongst {king}'s ranks who is capable after all.'")
    read()
    print(f"\n\033[1;4;91m{character} vs. {wizard}\033[0m\n")
    while enemy > 0 and player > 0:
        
        if enemy_poisoned is not None:
            enemy, enemy_poisoned = poison(enemy, enemy_poisoned, target_name=wizard)

        player_bar, enemy_bar = health_bar(player_health=player, villain_health=enemy, villain_status=enemy_poisoned)
        print(f"{character}: {player_bar}\n{wizard}: {enemy_bar}\n")

        option = input("What will you do? (Fight/Use Item): ").casefold().strip()
        if option == "use item":
            itinerary = check_bag(bag)
            print(itinerary)
            item = input("Please select your item: ").casefold().strip()
            match item:
                case "potion":
                    player = potion(player)
                    bag.remove("potion")
                    continue
                case "poison":
                    if enemy_poisoned is None:
                        enemy, enemy_poisoned = poison(enemy, None, target_name=wizard)
                    else:
                        print(f"{wizard} is already poisoned!")
                    bag.remove("poison")
                    continue
                case _:
                    print("You changed your mind.\n")
                    continue
        elif option == "fight":
            hit = damage()    
            query, original_block = randomise()
            correct = correct_answer(original_block)
            answer = input(f"Please select your answer: ").strip().upper()
            if answer == correct:
                print("\nThat is the correct answer!\n")
                enemy -= hit
                enemy = max(enemy, 0)
                continue
            else:
                print(f"\nIncorrect, the correct answer was {correct}\n")
                player -= hit
                player = max(player, 0)
                continue
        else:
            pass

    if player <= 0:
        print(f"The final blow takes you out. {wizard} uses a levitation spell on you. As you lose conscious, {wizard} chuckles\n\n\033[1;38;5;88m{wizard}:\033[0m 'You shall make a fine specimen for my experiments.'")
        read()
        return throne_room(king, town, princess, character)
    else:
        reward_item = reward()
        print(f"{wizard} was defeated!\nFor fighting valiantly, you found a {reward_item}.\n")
        inventory = items(bag, reward_item)
        print(f"Updated inventory: {inventory}.")
        print(f"\n{wizard} has fallen. Their body dissolves into a sludge. Side-stepping the remains, you grab the keys from {wizard}'s desk and free Princess {princess} from her prison.'")
        read()
        return wizards_lair_entrance(princess, wizard, king, character, dragon)
    
def mountain_path(wizard, mountain, princess, king, town, character, dragon):
    print(f"\n\033[1;4;33m{mountain}\033[0m")
    print(f"The air is biting and the winds blow harshly. The steep terrain has deterred but the bravest of warriors. As you climb, the ground beneath your feet seems to crumble ever so slightly. Despite this, you press on forward.\n\nFaintly, you hear the exhausted screams of a woman. You rush over to the direction of the voice.")
    read()
    return wizards_lair(mountain, wizard, princess, king, town, character, dragon)

def accept_quest(king, wizard, princess, town, character, dragon):
    peaks = ["Annapurna I", "Everest", "K2", "Mansalu", "Ben Nevis", "Kangchenjunga", "Cho Oyu", "Dhaulagiri I", "Nanga Parbat", "Lhotse", "Makalu"]
    mountain = random.choice(peaks)
    if mountain == 'Ben Nevis':
        print(f"\nYou graciously accept the quest. King {king} is pleased.\n\n\033[1;38;5;93mKing {king}:\033[0m 'That is wonderful. The last sighting of {wizard} was at Mt. {mountain}. An infamous peak, it is not to be underestimated. May the Gods bless you on this quest. You are welcome to rest in the guest chambers in preparation for the journey ahead.'")
    else:
        print(f"\nYou graciously accept the quest. King {king} is pleased.\n\n\033[1;38;5;93mKing {king}:\033[0m 'That is wonderful. The last sighting of {wizard} was at Mt. {mountain}. One of the legendary 10 peaks, it have proven to be an unruly mountain to ascend. May the Gods bless you on this quest. You are welcome to rest in the guest chambers in preparation for the journey ahead.'")
    read()
    return mountain_path(wizard, mountain, princess, king, town, character, dragon)

def throne_room(king, town, princess, character, dragon):
    wizard = male_names()

    print("\n\033[1;4;33mThrone Room\033[0m")
    print(f"The marbeled flooring and detailed tapestry illuminate the room. King {king} sits on the throne, servants and guards to keep him company. The throne besides him is vacant. He is an grandiose figure with eyes wise beyond his years. You kneel, introduce yourself and pay your respects.")
    read()
    
    if king == wizard:
        print(f"\n\033[1;38;5;93mKing {king}:\033[0m 'Hello {character}, welcome to {town}.\n\nWhile we are usually a peaceful kingdom, a great travesty has befallen us. As you may be aware, my daughter, Princess {princess} has been kidnapped by the licentious {wizard}. It is accursed we are to share the same name. He is a fiendish wizard who has plagued the lands, and my most trustworthy of knights have yet to rescue our beloved princess. Are you here for the request I had delivered across the realm? It is unbecoming to bequest the aid of strangers, but times are dire and we are in an increasing sense of desperation.\n\n{character}, please may you accept this quest? The reward shall be generous.'")
    else:
        print(f"\n\033[1;38;5;93mKing {king}:\033[0m 'Hello {character}, welcome to {town}.\n\nWhile we are usually a peaceful kingdom, a great travesty has befallen us. As you may be aware, my daughter, Princess {princess} has been kidnapped by the licentious {wizard}. He is a fiendish wizard who has plagued the lands, and my most trustworthy of knights have yet to rescue our beloved princess. Are you here for the request I had delivered across the realm? It is unbecoming to bequest the aid of strangers, but times are dire and we are in an increasing sense of desperation.\n\n{character}, please may you accept this quest? The reward shall be generous.'")

    choice = input(f"\n\033[3;38;5;106mDo you want to accept the quest by King {king}?\033[0m \033[96m(Yes/No):\033[0m ").casefold()
    while True:
        try:
            if choice == "yes":
                update_karma(+ 1)
                return accept_quest(king, wizard, princess, town, character, dragon)
            elif choice == "no":
                update_karma(- 3)
                return deny_quest(king, wizard, princess, town, character, dragon)
            else:
                raise ValueError(f"King {king} failed to comprehend your response.\n")
        except ValueError as e:
            print(e)

def castle(character, dragon):
    king = male_names()
    princess = female_names()
    town = town_names()

    print("\n\033[1;4;33mCastle\033[0m")
    print(f"You have reached {town}. It is enclosed by walls of stone and mortar. The guards inform you this is the abode of King {king}. They eye you warily, inspecting your itinerary. They see you pose no harm and allow you to enter.\n\nIt is a modestly wealthy kingdom, with lucious greens in the markets and fine fabrics in the garnment shops. The children laugh as they play together in peace. In the centre of the town, a group of villagers pray to the statue of a God.\n\n'Please return Princess {princess} to safety.'\n\nThe phrase echoes amongst their prayers. You walk forward and reach the castle at the end of the enclosure. The home of King {king}.")
    read()
    return throne_room(king, town, princess, character, dragon)

def horse(character, dragon):
    level_two()

    print("\n\033[1;4;33mStation\033[0m")
    print("A lone horse is grazing the pasture. It bears a saddle and it's reins have been cut.\n")
    while True:
        transport = input("\033[3;38;5;106mPlease select your transportation method:\n\n\033[0mHorse\n\nAnswer: ").capitalize().strip()
        try: 
            if transport == "Horse":
                print("\nYou approach the horse steadily. At first, it observes you with caution but after smelling your scent, it appears to be welcoming. You mount the horse and ride through the barren fields.")
                read()
                return castle(character, dragon)
            else:
                raise ValueError("\nThe next destination is too far to venture forth by foot.\n")
        except ValueError as e:
            print(e)

############################################ LEVEL TWO START ############################################

############################################ LEVEL ONE END ############################################
def townsperson_fight(character, thief, village, dragon):
    print(f"\n\033[1;4;33m{thief}'s Plan\033[0m")
    lord = villager_names()
    print(f"\n\033[1;38;5;93m{thief}\033[0m 'It is good to hear there is another who fights for the people. The knights are supposed to help us but they're too busy taxing the poor.'\n\nHe points to a townsperson adorned in fine fabrics.\n\n\033[1;38;5;93m{thief}\033[0m 'I have set my eyes on this person. Their manner of dress differs from the regulars of this town. I imagine they wouldn't be at a loss if they were to spare us a few coin.\n\n{thief} approaches the townsperson. However, they are quickly overwhelmed.\n\n\033[1;38;5;222mTownsperson\033[0m 'Do you truly believe I came to this town unprepared for the likes of you? I, Lord {lord}, was trained by the finest of swordmasters, your knife is but a child's toy in my presence.\n\nLord {lord} lunges at you.")
    read()

    townsperson, player = 100, 100
    townsperson_poisoned = None

    print(f"\n\033[1;4;91m{character} vs. Lord {lord}\033[0m\n")
    while townsperson > 0 and player > 0:
        
        if townsperson_poisoned is not None:
            townsperson, townsperson_poisoned = poison(townsperson, townsperson_poisoned, target_name=f"Lord {lord}")

        player_bar, townsperson_bar = health_bar(player_health=player, villain_health=townsperson, villain_status=townsperson_poisoned)
        print(f"{character}: {player_bar}\nLord {lord}: {townsperson_bar}\n")

        option = input("What will you do? (Fight/Use Item): ").casefold().strip()
        if option == "use item":
            itinerary = check_bag(bag)
            print(itinerary)
            item = input("Please select your item: ").casefold().strip()
            match item:
                case "potion":
                    player = potion(player)
                    bag.remove("potion")
                    continue
                case "poison":
                    if townsperson_poisoned is None:
                        townsperson, townsperson_poisoned = poison(townsperson, None, target_name=f"Lord {lord}")
                    else:
                        print(f"Lord {lord} is already poisoned!")
                    bag.remove("poison")
                    continue
                case _:
                    print("You changed your mind.\n")
                    continue
        elif option == "fight":
            hit = damage()    
            query, original_block = randomise()
            correct = correct_answer(original_block)

            answer = input(f"Please select your answer: ").strip().upper()
            if answer == correct:
                print("\nThat is the correct answer!\n")
                townsperson -= hit
                townsperson = max(townsperson, 0)
                continue
            else:
                print(f"\nIncorrect, the correct answer was {correct}\n")
                player -= hit
                player = max(player, 0)
                continue

    if player <= 0:
        print(f"You were defeated by Lord {lord}.\n\n\033[1;38;5;222mLord {lord}\033[0m 'What a pitiful display, begone with you!\n\nLord {lord} raises his sword. The glean of its edge is the last image you see.")
        read()
        return bandit_chat(character, village, dragon)
    else:
        reward_item = reward()
        print(f"Lord {lord} was defeated!\nFor fighting valiantly, you found a {reward_item}.\n")
        inventory = items(bag, reward_item)
        print(f"Updated inventory: {inventory}.")
        print(f"Lord {lord}'s sword shatters on the last blow.\n\n\033[1;38;5;222mLord {lord}\033[0m 'What an honour to have duelled with such a fine opponent. Please accept this dowry as a token of my respect for your swordsmenship.'\n\nHe gives you a generous sum which you give to {thief}.\n\n\033[1;38;5;172m{thief}:\033[0m 'Thank you for your help. I am in a haste to spe-- to donate to the less fortunate. May the Gods bless you on your travels.'\n\nHe scurries into the darkened alleways of the town without a trace in sight.")
        read()
        return horse(character, dragon)

def bandit_fight(character, thief, village, dragon):
    print(f"\n\033[1;4;33mSuddenly...\033[0m")
    bandit, player = 100, 100
    bandit_poisoned = None

    print(f"\n\033[1;38;5;172m{thief}\033[0m 'Unfortunately since you have seen me, I cannot allow you to walk freely.'\n\nThey charge at you but you block, held at a bind.")
    read()
    print(f"\n\033[1;4;91m{character} vs. {thief} the Bandit\033[0m\n")
    while bandit > 0 and player > 0:
        
        if bandit_poisoned is not None:
            bandit, bandit_poisoned = poison(bandit, bandit_poisoned, target_name=f"{thief} the Bandit")

        player_bar, bandit_bar = health_bar(player_health=player, villain_health=bandit, villain_status=bandit_poisoned)
        print(f"{character}: {player_bar}\n{thief} the Bandit: {bandit_bar}\n")

        option = input("What will you do? (Fight/Use Item): ").casefold().strip()
        if option == "use item":
            itinerary = check_bag(bag)
            print(itinerary)
            item = input("Please select your item: ").casefold().strip()
            match item:
                case "potion":
                    player = potion(player)
                    bag.remove("potion")
                    continue
                case "poison":
                    if bandit_poisoned is None:
                        bandit, bandit_poisoned = poison(bandit, None, target_name=f"{thief} the Bandit")
                    else:
                        print(f"{thief} the Bandit is already poisoned!")
                    bag.remove("poison")
                    continue
                case _:
                    print("You changed your mind.\n")
                    continue
        elif option == "fight":
            hit = damage()    
            query, original_block = randomise()
            correct = correct_answer(original_block)

            answer = input(f"Please select your answer: ").strip().upper()
            if answer == correct:
                print("\nThat is the correct answer!\n")
                bandit -= hit
                bandit = max(bandit, 0)
                continue
            else:
                print(f"\nIncorrect, the correct answer was {correct}\n")
                player -= hit
                player = max(player, 0)
                continue

    if player <= 0:
        print(f"You were defeated by {thief} the Bandit. Some knights come over and see you on the floor.\n\n\033[1;38;5;172m{thief}:\033[0m 'That person is a thief! Please take him away.'\n\nYou're too weak to speak for yourself. Anyone who could have vouched for you is no longer around. Due to the lack of pushback, the knights seize you and throw you in the back of a carriage. The light closes on you when the doors shut.")
        read()
        return town(character, village, dragon)
    else:
        reward_item = reward()
        print(f"{thief} the Bandit was defeated!\nFor fighting valiantly, you found a {reward_item}.\n")
        inventory = items(bag, reward_item)
        print(f"Updated inventory: {inventory}.")
        print(f"\n{thief} loses his grip on his knife. You kick it away, stopping him from reaching it. A group of knights come over and arrests {thief}. \n\n\033[1;38;5;172m{thief}\033[0m 'Curse you, curse you all! May the Gods enact righteous justice!'\n\nHe disppears with the knights and the town continues its way of life.")
        read()
        return horse(character, dragon)
    
def bandit_chat(character, village, dragon):
    print(f"\n\033[1;4;33mTalk with a Bandit\033[0m")
    thief = villager_names()
    print(f"\nYou move over to the man in the black mask. He notices your presence.\n\n\033[1;38;5;160mBandit:\033[0m 'My name is {thief}. And you are? ...I see. {character}, you look like a strong person. I've been eyeing that guy over there who seems to be in good fortune. The people of this town are living in squalor and it would be nice to share a bit of that wealth with others. Please may you help me?'\n")

    while True:
        response = input(f"Do you choose to help {thief}? (Yes/No): ").casefold().strip()
        if response == "no":
            update_karma(+ 1)
            print(f"\n\033[1;38;5;172m{thief}\033[0m 'I guess I will have to find someone else that is willing to help.'")
            return bandit_fight(character, thief, village, dragon)
        elif response == "yes":
            update_karma(- 1)
            print(f"\n\033[1;38;5;172m{thief}\033[0m 'Thank you.'")
            return townsperson_fight(character, thief, village, dragon)
        else:
            print(f"\n\033[1;38;5;172m{thief}:\033[0m 'Sorry, I could not hear your answer.'\n")
            continue

def knight_fight(character, lord, village, dragon):
    print(f"\n\033[1;4;33mEscape attempt\033[0m")

    print(f"\nYou leave Lord {lord} to fend for himself. However you don't travel far as a Knight blocks your path.\n\n\033[1;38;5;27mKnight\033[0m 'Not a loyal one aren't you, leaving your accomplice on their own.\n\nYou look back and see Lord {lord} has made quick work of the bandit. They flee from the scene.\n\n\033[1;38;5;27mKnight\033[0m 'I shall take you in for questioning!'")
    read()

    knight, player = 100, 100
    knight_poisoned = None

    print(f"\n\033[1;4;91m{character} vs. Knight\033[0m\n")
    while knight > 0 and player > 0:
        
        if knight_poisoned is not None:
            knight, knight_poisoned = poison(knight, knight_poisoned, target_name="Knight")

        player_bar, knight_bar = health_bar(player_health=player, villain_health=knight, villain_status=knight_poisoned)
        print(f"{character}: {player_bar}\nKnight: {knight_bar}\n")

        option = input("What will you do? (Fight/Use Item): ").casefold().strip()
        if option == "use item":
            itinerary = check_bag(bag)
            print(itinerary)
            item = input("Please select your item: ").casefold().strip()
            match item:
                case "potion":
                    player = potion(player)
                    bag.remove("potion")
                    continue
                case "poison":
                    if knight_poisoned is None:
                        knight, knight_poisoned = poison(knight, None, target_name="Knight")
                    else:
                        print("The Knight is already poisoned!")
                    bag.remove("poison")
                    continue
                case _:
                    print("You changed your mind.\n")
                    continue
        elif option == "fight":
            hit = damage()    
            query, original_block = randomise()
            correct = correct_answer(original_block)

            answer = input(f"Please select your answer: ").strip().upper()
            if answer == correct:
                print("\nThat is the correct answer!\n")
                knight -= hit
                knight = max(knight, 0)
                continue
            else:
                print(f"\nIncorrect, the correct answer was {correct}\n")
                player -= hit
                player = max(player, 0)
                continue

    if player <= 0:
        print(f"You were defeated by the Knight. More knights come over and throw your weakened body in the back of a carriage. The light closes on you when the doors shut.")
        read()
        return town(character, village)
    else:
        reward_item = reward()
        print(f"The knight was defeated!\nFor fighting valiantly, you found a {reward_item}.\n")
        inventory = items(bag, reward_item)
        print(f"Updated inventory: {inventory}.")
        print("The Knight stumbles to the ground. He lies unconscious. You observe the audience around you. The townspeople look at you in fear. Sensing you are no longer welcome, you leave immediately.")
        read()
        return horse(character, dragon)

def lord_chat(character, village, dragon):
    print(f"\n\033[1;4;33mTalk with a Lord\033[0m")
    thief, lord = villager_names(), villager_names()
    print(f"\nYou move over to the man in the fine hat. He examines you. Seeing you do not pose a threat, he extends his hand.\n\n\033[1;38;5;222mLord {lord}\033[0m 'Good greetings, I am Lord {lord}. I see you are not of this town either. What is your name may I ask? ... I see. {character}, sorry to mistrust you but this place is known for being a home of thieves. One cannot be too cautious within this land.'\n\nHe subtly gestures to shifty individuals near a ginnel. \n\n\033[1;38;5;222mLord {lord}\033[0m 'What brings you to this land, young one?\n\nBefore you can answer, a man with a mask approaches you with a knife.\n\n\033[1;38;5;160mBandit:\033[0m 'Give us your gold now!'\n\nLord {lord} has his hand on his hilt.\n")

    while True:
        allegiance = input("Do you choose to do? (Help/Flee) ").casefold().strip()
        if allegiance == 'help':
            update_karma(+ 1)
            return bandit_fight(character, thief, village, dragon)
        elif allegiance == "flee":
            update_karma(- 1)
            return knight_fight(character, lord, village, dragon)
        else:
            print("\nThe nerves keep you still.\n")
            continue

def town(character, village, dragon):
    level_one()

    print(f"\n\033[1;4;33m{village}\033[0m")
    print("It's a cozy little town. The air is fresh and the birds are singing. The children merrily sing rhymes and the townsfolk go about their day-to-day. While not filled with abundance, there is a familiar sense of community that lingers. You see two men ahead of you. One with a black mask and one wearing a fine hat.\n")

    while True:
        person = input("Do you speak with the man in the hat or the man in the mask? (Mask/Hat) ").casefold().strip()
        if person == "hat":
            return lord_chat(character, village, dragon)
        elif person == "mask":
            return bandit_chat(character, village, dragon)
        else:
            print("\nYou do some stretches.")
            continue
############################################ LEVEL ONE START ############################################ 

############################################ CHARACTER CREATION END ############################################   
def main(dragon):
    village = village_names()

    show_intro()
    print("\nIt appears to be a sleepy morning. The innkeeper hails you over.\n\n\033[1;38;5;116mInnkeeper:\033[0m 'Good morning there! I hope you had a good rest. Please may I get your name so I can check you out?'\n")
    while True:
        character = input("Please insert your name: ").strip().capitalize()
        confirm = input(f"\nIs {character} correct? (Yes/No) ").strip().casefold()
        if confirm == "yes":
            print(f"\n\033[1;38;5;116mInnkeeper:\033[0m '{character}, aye. Fine name that is. Enjoy the rest of your visit at {village}!'")
            return town(character, village, dragon)
        else:
            print("\nYou yawn through your answer.\n\n\033[1;38;5;116mInnkeeper:\033[0m 'Sorry, I couldn't catch that.'\n")
            continue

############################################ CHARACTER CREATION START ############################################       
if __name__ == "__main__":
    main(dragon)
############################################ MAIN GAME START ############################################