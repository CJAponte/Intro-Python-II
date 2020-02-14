from room import Room
from player import Player
from item import Item
import os
import time

def clear(num):
    time.sleep(num)
    os.system('cls')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].items += [Item("Torch", "A simple torch that should help light your way.")]
room['outside'].items += [Item("Key", "Maybe it opens something further in?")]
room['narrow'].items += [Item("Gold Coin", "Easy to miss at first, a small gold coin. Maybe theres more to be found.")]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

clear(.1)

Player = Player(input("What is your players name? "), room['outside'])


# clear(.5)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

clear(2)
print(f'Welcome {Player.name}! Let your journey begin. \nPlease use the keys "N", "S", "E", "W" to move through rooms. \nUse the "L" key to look around the room.')
print(f'Use "P" and the name of any items found to pick them up or "D" and the items name in your backback to drop it.')
print(f'To check what\'s in your backback, just use the "B" key.')
print(f'If you wish to end your journey, all you have to do is enter "Q" and you\'ll exit the game.')
print(f'\nLet the game begin, {Player.name}!')
print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# clear(25)

while True:
    print(Player.current_room)
    cmd = input("~~~> ").lower().split(' ', 1)
    if cmd[0] in ["n", "s", "e", "w"]:
        clear(.25)
        current_room = Player.current_room
        next_room = getattr(current_room, f"{cmd[0]}_to")
        if next_room is not None:
            Player.current_room = next_room
        else:
            print("You can't move that way.")
    elif cmd[0] == "l":
        clear(.25)
        if len(Player.current_room.items) != 0:
            for i in range(len(Player.current_room.items)):
                print(f"You look around and you find a {Player.current_room.items[i].name}")
            print(f'\n')
        else:
            print("You look around but find nothing of interest.\n")
    elif cmd[0] == "b":
        if len(Player.backpack) != 0:
            print("Currently in your backpack: ")
            for i in range(len(Player.backpack)):
                print(f'{Player.backpack[i].name} - {Player.backpack[i].desc}')
            print(f'\n')
        else:
            print("Your backpack is empty.\n")
    elif cmd[0] == "p":
        if len(Player.current_room.items) != 0:
            if len(cmd) > 1:
                for i in range(len(Player.current_room.items)):
                    if Player.current_room.items[i].name.lower() == cmd[1].lower():
                        Player.backpack.append(Player.current_room.items[i])
                        print(f'You\'ve picked up the {Player.current_room.items[i].name}.')
                        del Player.current_room.items[i]
                        clear(2.5)
                        break
                        
            else:
                print(f'Please select an item to pick up.')
                clear(2.5)
        else:
            print(f'There is nothing to pick up in this room.')
    elif cmd[0] == "d":
        if len(Player.backpack) != 0:
            if len(cmd) >1:
                for i in range(len(Player.backpack)):
                    if Player.backpack[i].name.lower() == cmd[1].lower():
                        Player.current_room.items.append(Player.backpack[i])
                        print(f'You\'ve dropped the {Player.backpack[i].name}.')
                        del Player.backpack[i]
                        clear(2.5)
                        break
            else:
                print(f'Select an item to drop.')
                clear(2.5)
        else:
            print(f'Your backpack is empty.')
            clear(2.5)
    elif cmd[0] == "q":
        print("Exiting Game")
        exit()
    else:
        print("Invalid command. Please try again.")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# while True:
#     print(Player.current_room)
#     cmd = input("~~~> ").lower()
#     if cmd in ["n", "s", "e", "w"]:
#         if cmd == "n":
#             if Player.current_room.n_to is not None:
#                 Player.current_room = Player.current_room.n_to
#             else:
#                 print("You can't go this way.")
#         elif cmd == "s":
#             if Player.current_room.s_to is not None:
#                 Player.current_room = Player.current_room.s_to
#             else:
#                 print("You can't go this way.")
#         elif cmd == "e":
#             if Player.current_room.e_to is not None:
#                 Player.current_room = Player.current_room.e_to
#             else:
#                 print("You can't go this way.")
#         elif cmd == "w":
#             if Player.current_room.w_to is not None:
#                 Player.current_room = Player.current_room.w_to
#             else:
#                 print("You can't go this way.")
#     elif cmd == "q":
#         print("Closing Game")
#         exit()
#     elif cmd == "l":
#         if len(Player.current_room.items) != 0:
#             for i in range(len(Player.current_room.items)):
#                 print(f"You look around and you find a {Player.current_room.items[i].name}")
#         print("What would you like to do?")
#     else:
#         print("That is not a valid command.")