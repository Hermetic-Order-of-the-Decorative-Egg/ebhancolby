import player
import time
if __name__ == "__main__":
    name = input("What is your name, adventurer?\n>")
    print("\nAs you walk through the city streets, you witness the robbery of an innocent woman. What do you do?")
    print("1. You rush to the woman's aid, instantly crushing the assailant's skull between your bare hands.")
    print("2. You seize the opportunity the moment has presented to you and deftly mug the woman first.")
    print("3. You summon a portal to Hell, burning both of them alive with an unholy barrage of Hellfire.")
    pclass = int(input(">"))
    while pclass not in range(1,4):
        print("Please enter a valid answer, smartypants.")
        pclass = int(input(">"))
    p = player.Player(name,pclass-1)
    print("You are a {} named {}.".format(player.classes[p.pclass],p.name))
    print("After dealing with the robbery, you decide that it's about time you go out on an adventure of your own. The options are limitless (*limitless = limited).\n")
    time.sleep(2)
    print ("Conveniently, you are approached by a hooded figure who proposes a quest which promises fame and fortune.\n")
    time.sleep(2)
    print("1. Go eat dirt, old man. I have everything I need right here.\n")
    print("2. Though your breath reeks of liquor and sin, you have my attention.\n")
    choice1 = int(input(">"))
    while choice1 not in range(1,3):
        print("For the love of Pete. Can you stop fooling around?")
        choice1 = int(input(">"))
    if choice1 == 1:
        print("Wrong answer, you inbred crack whore! Game over.")
    elif choice1 == 2:
        print("You fool. There was no quest! Muahaha!")
        