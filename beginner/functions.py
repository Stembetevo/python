
def parent_function(person,coins):
    def play_game():
        nonlocal coins
        coins -=1
        if coins > 1:
            message = "\n%s has %s coins left." % (person, coins)
            print(message)
        elif coins == 1:
            print("\n" + person + " has " + str(coins)+"coins left")
        else:  
            print("\n"+"You are out of coins!")
    return play_game
tommy = parent_function("tommy",9)
jane = parent_function("jane",3)
tommy()
tommy()