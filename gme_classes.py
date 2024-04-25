# game_classes.py

import random


"""
create a room class that will take in 4 arguments including name, description, and challenges as well as a boolean representing
whether or not the room has been beaten and a dictionary called connections which will hold the rooms connected to current room
"""

class Room:
    """
    Representation of a game room that contains challenges the player will need to solve

    Attributes:
        name (str): name of room
        description (str): brief description of room
        challenges(list): A list of dictionaries containing questions for each room
        beaten (bool): Variable indicating whether room has been beaten or not
        connections (dict): dictionary mapping directions to connect rooms

    """

    def __init__(self, name, description, challenges):
        self.name = name
        self.description = description
        self.challenges = challenges
        self.beaten = False
        self.connections = {}

    def connect_room(self, room, direction):
        """
        Connects this room to another room in specified direction

        Args: 
            room (Room): Room to connect to
            direction (str): The direction in which to connect the room
        """
        self.connections[direction] = room.name

    def play_game(self, inventory):
        """
        Conducts a challenge in the room. If room has not been beaten, player is presented with a challenge and their answer is checked.

        Args:
            inventory (list): List where names of beaten rooms are stored
        
        Returns:
            str: A message indicating  the result of the game attempt.
        """
        if self.beaten:
            return "You have already beaten this room."
        
        challenge = random.choice(self.challenges)
        print(challenge['question'])
        print('Your answer: ')
        user_answer = input().strip().lower()
        
        if user_answer == challenge['answer'].lower():
            self.beaten = True
            inventory.append(self.name)
            return f"Correct! You have beaten the {self.name} challenge!"
        else:
            return "Incorrect! Try again."

    def __str__(self):
        """
        Provides a string representation of the room
        """
        return self.name



class AdventureMap:
    """
    Manages all the room within the game, allows for navigation and management of connections between them

    Attributes:
        rooms (dict): A dictionary of room names to Room instances
    """

    def __init__(self):
        self.rooms = {}
    
    def add_room(self, room):
        """
        Adds a room to the map.

        Args:
            room (Room): The room to add
        """
        self.rooms[room.name.lower()] = room
    
    def get_room(self, room_name):
        """
        Retrieves a room by its name.

        Args:
            room_name (str): Name of the room to retrieve
        
        Returns:
            Room: The room corresponding to the given name.

        Raises:
            ValueError: If the room is not found
        """
        room = self.rooms.get(room_name.lower())
        if room:
            return room 
        else:
            raise ValueError(f"Room not found: {room_name}")
    
    def connect_rooms(self, room1_name, room2_name, direction):
        """
        Connects two rooms in a specified direction.

        Args:
            room1_name (str): The name of the first room.
            room2_name (str): The name of the second room to connect to the first.
            direction (str): the direction to establish the connection in.
        """

        room1 = self.get_room(room1_name)
        room2 = self.get_room(room2_name)
        room1.connect_room(room2, direction)



class Character:
    """
    Represents a character tha a player can choose

    Attributes:
        name (str): The characters name
        description (str): A brief desription of the characters attributes
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        """
        Returns a string representation of the character, including their description.
        """
        return f"{self.name}, a {self.description}."



class Player:
    """
    Represents the player in the game, managing their chosen character and their progress

    Attributes:
        character (Character): The player's chosen character.
        Inventory (list): A list of items or achievements collected by the player
        completed_rooms (set): A set of rooms that have been completed
    """
    def __init__(self, character=None):
        self.character = character
        self.inventory = []
        self.completed_rooms = set()  # Tracks completed or skipped rooms

    def choose_character(self, available_characters):

        """
        Allows the player to choose a character from a list of available characters.

        Args: 
            available_characters (list): A list of Character instances available for selection
        
        Raises:
            ValueError: If the player's choice is out of the range
        """

        print("Available characters:")
        for index, character in enumerate(available_characters, start=1):
            print(f"{index}. {character}")
        while True:
            try:
                print("Choose your character (1-3):")
                choice = int(input())
                if 1 <= choice <= len(available_characters):
                    self.character = available_characters[choice - 1]
                    print(f"You have chosen {self.character.name}.")
                    break
                else:
                    raise ValueError("Please choose a valid number between 1 and 3.")
            except ValueError as e:
                print(e)

    


