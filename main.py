import time


def intro():
    print("Once upon a time...")
    time.sleep(1.5)
    print("In a world where dwelf lives and dragon flies...")
    time.sleep(2)
    print("Once you fell from the sky and opened your eyes... You heard someone whispering:")
    time.sleep(2)
    print('"What\'s your name?" says a cat hanging on the tree')
    time.sleep(2)
    name = input("(You recall that your name is...)")
    time.sleep(1)
    print ("Oh ok so. " + name +", I need you to do me a favor...")

if __name__ == "__main__":
    intro()
