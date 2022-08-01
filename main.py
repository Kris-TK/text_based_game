import time
BLOCK_LINE = "--------------------------------------\n"
SYS_LINE = "----------------SYSTEM----------------"

class Player:
    def __init__(self, name = None, role = None):
        self.name = name
        self.role = role
        self.attrbt_upper = {"intelligence" : 0, 
        "charm" : 0, "agility" : 0,
        "phys_attack" : 5, "mag_attack" : 5,
        "HP" : 50, "MP" : 10,
        "lost_index" : 0, "spirit" : 0,
        "item" : {}}
        self.attrbt_curr = {"intelligence" : 0, 
        "charm" : 0, "agility" : 0,
        "phys_attack" : 5, "mag_attack" : 5,
        "HP" : 50, "MP" : 10,
        "lost_index" : 0, "spirit" : 0,
        "item" : {}}
    def increase_attrbt(self, amount, attrbt):
        self.attrbt_upper[attrbt] += amount
        self.attrbt_curr[attrbt] += amount
        print("Your max " + attrbt + " has incremented by " + str(amount))
        print("Your current " + attrbt + " status is: " + str(self.attrbt_curr[attrbt]) + "/" + str(self.attrbt_upper[attrbt]))
    """ def recover_attrbt(self, amount, attrbt):
        if self.attrbt_curr[attrbt] """


def list_of_roles():
    print("\"...Oki, I would suppose that you might hit your head and lost your memories.\"")
    time.sleep(2)
    print("\"Normally, elves are magician, they have agility high enough to cast the most powerful spells...\"")
    time.sleep(3)
    print("\"Dragons, in contrast, are born to become the most strenghtful warriors in the world. They destroy the mountain by simply attacking it.\"")
    time.sleep(3)
    print("\"Dwelves...not known for aggresiveness though, are the most skillful at building all kinds of crafts.\"")
    time.sleep(3)
    print("\"And dark elves... who charm everything they encountered and make its power their own...\"\n")
    time.sleep(3)
    print("\"I am asking you, because, you're a human, I couldn't tell what you do from your apperance.\"")
    time.sleep(3)
    print("\"So what do you do? Or, what you would like to do in the future? Since you've lost all your memories...\"")
    time.sleep(3)
    print(BLOCK_LINE + "Once your mind is determined, there would be no way back.")
    print("1. Magician: Casts spells to attack/defend/add buff or debuff, demands MP and requires high agility.")
    print("2. Warrior: Has high physical attacking harm and high defense to physical attack, sensitive to buff and debuff.")
# intro_and_setup(Player) provides the background and intro to the world of game and 
#        asks player for fundamental setup
def intro_and_setup(player: Player) -> None:
    print("Once upon a time...")
    time.sleep(1.5)
    print("In a world where dwelf lives and dragon flies...")
    time.sleep(2)
    print("Once you fell from the sky and opened your eyes... You heard someone whispering:")
    time.sleep(2)
    print('"What\'s your name human? It\'s rare to see something like you these days." says a cat hanging on the tree')
    time.sleep(3)
    player.name = input(BLOCK_LINE + "(You recall that your name is...)\n")
    time.sleep(1)
    print("\x1B[3m" + "\"You can call me " + player.name + ".\" you replied" + "\x1B[0m\n" + BLOCK_LINE) 
    time.sleep(1.5)
    print ("Oh ok so. " + player.name +", I need you to do me a favor...")
    time.sleep(2)
    print("Actually, before that, would you mind me asking what do you do for a living?")
    time.sleep(2)
    player_choice = input('1. "What do you mean by that?" 2. "Oh Emm... I can\'t recall." 3. "Why should I tell you?"\n')
    time.sleep(1)
    if player_choice[0] == "1":
        print(SYS_LINE)
        player.increase_attrbt(1, "intelligence")
        player.increase_attrbt(10, "HP")
        print(BLOCK_LINE)
        time.sleep(1)
        list_of_roles()



if __name__ == "__main__":
    player = Player(None, None)
    intro_and_setup(player)
