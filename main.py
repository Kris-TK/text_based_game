import time

BLOCK_LINE = "-------------------------------------\n"

class Player:
    def __init__(self, name = None, role = None):
        self.name = name
        self.role = role
        self.intelligence = 0
        self.charm = 0
        self.agility = 0
        self.phys_attack = 5
        self.mag_attack = 5
        self.HP = 50
        self.MP = 10
        self.lost_index = 0
        self.spirit = 0
        self.item = []

def list_of_roles():
    print("...Oki, I would suppose that you might hit your head and lost your memories.")
    time.sleep(1)

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
    player_choice = input('1. "What do you mean by that?" 2. "Oh Emm... I can\'t recall." 3. "Why should I tell you?"')
    time.sleep(2)
    if player_choice[0] == "1":
        list_of_roles()


if __name__ == "__main__":
    player = Player(None, None)
    intro_and_setup(player)
