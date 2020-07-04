import operator
from challenge.config import DIRECTIONS_MAP

class Zombie(object):
    """
    This class represent a zombie, which is capable of traveling,
    and infecting creatures it encounters on its way.
    traveling is realized bu changing current_location.
    A zombie cannot breach a predefined boundary.
    """

    """
    maps movement verbs to 2D changes 
    """
    directions_map = DIRECTIONS_MAP

    def __init__(self, moves, start_location,boundary):
        """
        :param (string) moves: a string of direction letters, that zombie follows
        :param (tuple) start_location: starting 2D location of a zombie
        :param (int) boundary limits of zombie's world
        """
        self.moves = moves
        self.start_location = start_location
        self.current_location = start_location
        self.boundary = boundary

    def _update_position(self, direction):
        """
        Updates current location give a direction
        :param (string) direction: a character indicating the direction if movement
        :return: None
        """

        calculated_position = tuple(map(operator.add, self.current_location, self.directions_map.get(direction,(0,0))))

        # fix edge traveling
        x = calculated_position[0]
        if calculated_position[0] >= self.boundary:
            x = 0
        if calculated_position[0] == -1:
            x = self.boundary - 1

        y = calculated_position[1]
        if calculated_position[1] >= self.boundary:
            y = 0
        if calculated_position[1] == -1:
            y = self.boundary - 1


        # trigger IndexError if crossing boundaries
        if x < self.boundary and y < self.boundary:

            self.current_location = (x,y)
        else:
            raise IndexError('{} out of range'.format(calculated_position))

    def _detect_and_infect(self, creature_locations):
        """
        A zombie will infect creatures it meets.
        :param (list) creature_locations: the location of creatures, a zombie might encounter
        :return: (list) of infected creatures, by current location
        """
        creature_count = 0

        try:
            while True:
                detected_index = creature_locations.index(self.current_location)
                del creature_locations[detected_index]
                creature_count+=1
        except ValueError:
            pass
        finally:
            return [self.current_location for _ in range(creature_count)]

    def travel(self, creature_locations):
        """
        Move zombie in his world. to possibly infect creatures he meets
        :param (list) creature_locations:  list of creature locations a zombie may meet.
        :return: (list) A list of infected creatures, by zombie's moves
        """


        new_zombie_locations = []
        try:
            """
            follow the moves. * is to check for starting location, and infect existing creatures.
            """

            for move in '*' + self.moves:
                self._update_position(move)
                just_added_zombie_locations = self._detect_and_infect( creature_locations)
                new_zombie_locations.extend(just_added_zombie_locations)

            return new_zombie_locations
        except IndexError:
            # This means moves exceed grids limit, so that's as far as a zombie can go.
            return new_zombie_locations


class ZombieLand(object):
    """
    This is where Zombies exist, and make their moves.
    """

    def __init__(self, config):

        self.config = config


    def release_the_zombie(self):
        """
        Trigger the zombie adventure, and infect.
        :return: (int,list) The number of new zombies, and a list of their locations.
        """

        new_zombies = [self.config.zombie_start]
        zombies_final_positions = []
        creature_locations = self.config.creatures
        score = 0
        while new_zombies:

            zombie = Zombie(self.config.moves, new_zombies.pop(0),self.config.size)
            interim_new_zombies = zombie.travel(creature_locations)
            score += len(interim_new_zombies)
            zombies_final_positions.append(zombie.current_location)
            new_zombies.extend(interim_new_zombies)

        return score, list(set(zombies_final_positions))
