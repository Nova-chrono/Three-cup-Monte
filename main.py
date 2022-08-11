from random import shuffle
print("Three-Cup Monte")

game_set = [
    " _", " _", "_", 
    "/ \ ", "/O\ ", "/ \ ",
    "~~~~~~~~~~~~~~~"
]
# print(game_set)

def display_game_set():
    print(" " + game_set[0] + "   " +  game_set[1] + "    " +  game_set[2])
    print(" " + game_set[3] + " " + game_set[4] + " " + game_set[5])
    print(game_set[6])

display_game_set()


cups = ["X", "O", "X"]

def shuffle_cups(cups):
    shuffle(cups)
    return(cups)


def player_guess():
    guess = ''
    cup_position = ["1", "2", "3"]

    while guess not in cup_position:
        guess = input("Guess a cup number from 1-3: ")
    return int(guess) - 1
monte = shuffle_cups(cups)
# print(monte)


def check_guess(monte, guess):

    if monte[guess] == "O":
        print(f"Correct! \n{monte}")
    else:
        print(f"Wrong Cup!! \n{monte}")

guess = player_guess()
check_guess(monte, guess)
