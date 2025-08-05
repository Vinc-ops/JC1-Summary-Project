#Global Variables
room_types = ['treasure', 'battle']

class Game:
    """
    Class constructor for Game
    """
    def __init__(self, intro, outro, maze):
        pass

#List of things we need to do
#Create maze
class Maze:
    """
    Class constructor for Maze
    """
    def __init__(self, rooms: dict['Room'], starting_room):
        """
        Takes in a dict of Room objects and a starting room.
        Initializes str_chain, which will hold a chain of selected rooms for the maze (specifically, every second room from the list — explained below).
        """
        self.rooms = rooms
        self.starting_room = starting_room
        self.str_chain = []

    def generate_maze(self):
        """
        Function to generate the layout of rooms
        """
       
        strt_line = [i for i in range(len(self.rooms)) if i % 3 == 0]
        
        for i, id in enumerate(strt_line):
            current = self.rooms[id]

            # Connect vert
            if i + 1 < len(strt_line):
                down_room = self.rooms[strt_line[i + 1]]
                current.connection(down_room, 'down')
                down_room.connection(current, 'top')

            # Connect left
            if id - 1 >= 0:
                left_room = self.rooms[id - 1]
                current.connection(left_room, 'left')
                left_room.connection(current, 'right')

            # Connect right
            if id + 1 < len(self.rooms):
                right_room = self.rooms[id + 1]
                current.connection(right_room, 'right')
                right_room.connection(current, 'left')
                
            
    def draw_rooms(self):
        """
        Method to print out the room in the format of a mini map
        Then connects these rooms
        Each room (except the last) connects to the one above it ('top')
        Each room (except the first) connects to the one below it ('down')
        """
        for room in self.rooms:
            print(f'Room {room.id} connections:')
            for direction, connected_room in room.connects.items():
                if connected_room:
                    print(f'{direction} Room {connected_room.id}')
            print()

#Create Room

class Room:
    """
    Class construtor for Room
    For each room in the str_chain, it:

    Prints the room's .connects attribute (presumably a dictionary or list of connected rooms by direction)

    Then prints out the IDs of connected rooms, assuming each room has an id attribute.
    """
    def __init__(self, id: int):
        self.id = id
        self.connects = {'top': None, 'left': None, 'right': None, 'down': None}

    def connection(self, room, direction):
        if direction in self.connects:
            self.connects[direction] = room


class Character:
    pass


list_of_rooms = []
for i in range(20):
    room =  Room(i)
    list_of_rooms.append(room)
maze = Maze(list_of_rooms, list_of_rooms[0])
maze.generate_maze()
maze.draw_rooms()
#Objects



