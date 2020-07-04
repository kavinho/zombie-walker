import unittest
from challenge.zombie_land import Zombie

class TestZombie(unittest.TestCase):

    def test_zombie_1x1_false_creature(self):
        # prepare
        zombie = Zombie('R', (0,0), 1)

        # action
        new_z = zombie.travel([(2,2)])

        # assert
        self.assertEqual([], new_z)
        self.assertEqual(zombie.current_location, (0, 0))

    def test_zombie_2x2_meet_creature(self):
        # prepare
        zombie = Zombie('R', (0,0), 2)

        # action
        new_z = zombie.travel([(1,0)])

        # assert
        self.assertEqual([(1,0)], new_z)
        self.assertEqual(zombie.current_location, (1, 0))

    def test_zombie_3x3_meet_creature(self):
        # prepare
        zombie = Zombie('RD', (0,0), 3)

        # action
        new_z = zombie.travel([(1,0), (1, 1), (2, 1)])

        # assert
        self.assertEqual([(1,0),(1,1)], new_z)
        self.assertEqual(zombie.current_location, (1, 1))

    def test_zombie_3x3_travel_edge(self):
        # prepare
        zombie = Zombie('RD', (0,0), 3)

        # action
        new_z = zombie.travel([(1,0), (1, 1), (2, 1)])

        # assert
        self.assertEqual([(1,0),(1,1)], new_z)
        self.assertEqual(zombie.current_location, (1, 1))

    def test_zombie_3x3_meet_creature(self):
        # prepare
        zombie = Zombie('RD', (0,0), 3)

        # action
        new_z = zombie.travel([(1,0), (1, 1), (2, 1)])

        # assert
        self.assertEqual([(1,0),(1,1)], new_z)
        self.assertEqual(zombie.current_location, (1, 1))
