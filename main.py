"""
Author: Kevin Mastracchio
Class: CPSC
Assignment: RPG Game
Date: April 25, 2024

Code Description: I am writing code that will create an RPG game called "The Fun House" that takes place in a house.
In this house there are three rooms that a user can enter. Upon entering the rooms, the user is presented with a challenge specific to that room.
The user can continue trying to pass these rooms, and once he does he has beaten the game.
Upon beating the game the user can decide to quit out of the game, otherwise he can roam around the house until he'd like to quit.

(https://github.com/Kevm112/Rpg-Game.git) - Link of Github Repository

(https://github.com/Kevm112) - Link of Github Dashboard

"""



from gme_classes import Room, AdventureMap, Character, Player


def setup_game(characters):
    #intialize the game map to organize rooms
    game_map = AdventureMap()

    # Create room instances with descriptions and challenges
    outside = Room("Outside", "You are outside the house. Enter the house or quit.", [])
    entrance = Room("Entrance", "You are in the lobby. Choose a room or go back outside.", [])
    riddle_room = Room("Riddle Room", "Solve the riddle to proceed.", [
        {'question': "What has keys but can’t open locks?", 'answer': "piano"},
        {'question': "What has words, but never speaks?", 'answer': "book"},
        {'question': "What gets wetter as it dries?", 'answer': "towel"}
    ])
    trivia_room = Room("Trivia Room", "Test your knowledge with trivia.", [
        {'question': "What year did the Titanic sink?", 'answer': "1912"},
        {'question': "What planet is known as the red planet?", 'answer': "mars"},
        {'question': "Who wrote 'Hamlet'?", 'answer': "shakespeare"}
    ])
    unscramble_room = Room("Unscramble Room", "Unscramble the words to win.", [
        {'question': "Scrambled word: 'noypth' (Hint: Programming Language)", 'answer': "python"},
        {'question': "Scrambled word: 'ajav' (Hint: Programming Language)", 'answer': "java"},
        {'question': "Scrambled word: 'pacsr' (Hint: Garbage Collection)", 'answer': "scrap"}
    ])

    # Add rooms to game map
    game_map.add_room(outside)
    game_map.add_room(entrance)
    game_map.add_room(riddle_room)
    game_map.add_room(trivia_room)
    game_map.add_room(unscramble_room)

    # Define connections between rooms to navigate
    game_map.connect_rooms("outside", "entrance", "enter")
    game_map.connect_rooms("entrance", "riddle room", "1")
    game_map.connect_rooms("entrance", "trivia room", "2")
    game_map.connect_rooms("entrance", "unscramble room", "3")
    game_map.connect_rooms("entrance", "outside", "exit")

    # Initialize a player and assign a character
    player = Player(None)
    player.choose_character(characters)

    # Return Initalized game components
    return game_map, outside, player



def main():
    # Define Available characters
    characters = [
        Character("Wizard", "A wise and mystical old man"),
        Character("Warrior", "A strong and brave soldier"),
        Character("Archer", "A swift and silent Archer")
    ]

    # Welcome message and prompt to continue
    print('Welcome to the Fun House. Collect all the necessary resources to complete the game. Press any key to continue:')
    input()
    game_map, current_room, player = setup_game(characters)

    # Initialize game completion tracking variables
    game_completed = False  
    total_rooms = 3  
    beaten_rooms = 0

    # Game loop to keep game running
    while True:
        print(current_room.description)
        if current_room.name == "Outside":
            # Allow player to enter house again or quit
            print("Type 'enter' to enter the house or 'quit' to quit the game: ")
            action = input().lower().strip()
            if action == 'quit':
                print("Thanks for playing!")
                break
            elif action == 'enter':
                current_room = game_map.get_room("entrance")
        elif current_room.name == "Entrance":
            # Show available rooms or the option to exit
            for direction, room_name in current_room.connections.items():
                room_instance = game_map.get_room(room_name)
                if room_instance.beaten:
                    status = " (already beaten)"
                else:
                    status = ""
                print(f"Type '{direction}' to enter {room_name}{status}.")
            print('Choose a direction: ')
            action = input().lower().strip()
            if action == 'exit':
                current_room = game_map.get_room("outside")
            else:
                next_room_name = current_room.connections.get(action)
                if next_room_name:
                    current_room = game_map.get_room(next_room_name)
                    if current_room.beaten:
                        print("You have already beaten this room.")
                    else:
                        result = current_room.play_game(player.inventory)
                        print(result)
                        if "Correct!" in result:
                            beaten_rooms += 1
                    print("Press 'b' to return to the lobby: ")
                    back_to_lobby = input().strip().lower()
                    if back_to_lobby.lower() == 'b':
                        current_room = game_map.get_room("entrance")
                        if beaten_rooms == total_rooms and not game_completed:
                            print("Congratulations! You have beaten all the rooms and completed the game! Feel free to explore more or exit by going outside.")
                            game_completed = True

if __name__ == "__main__":
    main()
