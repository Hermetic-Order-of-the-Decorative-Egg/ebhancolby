import random
def choose_number():
    x = input(">")
    x = float(x)
    if (x>1):
        print("This number is far too large, my nibbeux.")
    elif (x<1):
        print("Too small!")
    else:
        print("Perfection.")
    return x

def coin_flip():
    c = random.uniform(0,1)
    if (c<0.5):
        print("[congratulates the user on being lucky]")
    else:
        print("Go heck yourself!")

def counter(n=10):
    for i in range(5,n):
        print(i)


if __name__ == "__main__":
    # b = choose_number()

    # if (b>1):
    #     coin_flip()
    #     counter()
    running = True
    while running:
        x = input(">")
        if (x=="choose"):
            choose_number()
        elif (x=="coin"):
            coin_flip()
        elif (x=="counter"):
            counter()
        elif (x=="exit"):
            running = False
        else:
            print("You really are a simple man, aren't you?")