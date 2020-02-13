from room import Room
from player import Player
from item import Item

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
room['outside'].items += [Item("Key", "Maybe it opens something inside")]
room['narrow'].items += [Item("Gold Coin", "Easy to miss a first, a small gold coin. Maybe theres more to be found")]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

Player = Player(input("What is your players name? "), room['outside'])
print("test", len(Player.current_room.items))
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

while True:
    print(Player.current_room, Player.current_room.items)
    cmd = input("~~~> ")
    if cmd in ["n", "s", "e", "w"]:
        current_room = Player.current_room
        next_room = getattr(current_room, f"{cmd}_to")
        if next_room is not None:
            Player.current_room = next_room
        else:
            print("You can't move that way.")
    elif cmd == "q":
        print("Exiting Game")
        exit()
    else:
        print("Invalid command. Please try again.")