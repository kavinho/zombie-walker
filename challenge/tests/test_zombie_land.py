import unittest
from challenge.zombie_land import ZombieLand
from challenge.config import Config

class TestZombieLand(unittest.TestCase):

    def test_1x1_grid_no_creature_travel_edge(self):
        # assert edge traveling
        config = {
            'size': 1,
            'zombie_start': (0,0),
            'creatures': [],
            'moves': 'DD',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score,0)
        self.assertEqual(positions,[(0,0)])

    def test_1x1_grid_no_creature(self):
        # assert edge traveling
        config = {
            'size': 2,
            'zombie_start': (0,0),
            'creatures': [],
            'moves': 'RR',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score,0)
        self.assertEqual(positions,[(0,0)])

    def test_simple_2x2_grid_no_creature(self):
        # assert no creatures
        config = {
            'size': 2,
            'zombie_start': (0,0),
            'creatures': [],
            'moves': 'D',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score,0)
        self.assertEqual(positions,[(0,1)])

    def test_simple_2x2_grid_zombie_creature (self):
        # assert not meeting creatures
        config = {
            'size': 2,
            'zombie_start': (0,0),
            'creatures': [(0,0)],
            'moves': 'D',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score,1)
        self.assertEqual(positions,[(0,1)])

    def test_simple_2x2_grid_1_creature_wont_meet(self):
        # assert not meeting creatures
        config = {
            'size': 2,
            'zombie_start': (0,0),
            'creatures': [(1,1)],
            'moves': 'D',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score,0)
        self.assertEqual(positions,[(0,1)])

    def test_simple_2x2_grid_1_creature_will_meet(self):
        # assert simple move and meeting creature
        config = {
            'size': 2,
            'zombie_start': (0, 0),
            'creatures': [(1, 0)],
            'moves': 'R',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score, 1)
        self.assertEqual(positions,[(1,0),(0,0)])

    def test_simple_3x3_grid_2_creatures_in_same_cell(self):
        # assert cascade infection
        config = {
            'size': 3,
            'zombie_start': (0, 0),
            'creatures': [(1, 1), (1,1),(1,0)],
            'moves': 'RD',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score,3)
        self.assertEqual(positions,[(1, 1), (2, 1), (2, 2)])

    def test_simple_3x3_grid_2_creatures_cascade(self):
        # assert cascade infection
        config = {
            'size': 3,
            'zombie_start': (0, 0),
            'creatures': [(1, 1), (2,1)],
            'moves': 'RD',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score,2)
        self.assertEqual(positions,[(0, 2), (1, 1), (2, 2)])

    def test_simple_3x3_grid_2_creatures_cascade_multi_move(self):
        # assert multi-move and cascade effect
        config = {
            'size': 3,
            'zombie_start': (0, 0),
            'creatures': [(1, 1), (2,1)],
            'moves': 'RDLU',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score,2)
        self.assertEqual(positions,[(1, 1), (2, 1), (0, 0)])

    def test_simple_3x3_grid_3_creatures_same_cell(self):

        config = {
            'size': 3,
            'zombie_start': (0, 0),
            'creatures': [(1, 0),(1, 0), (2,1)],
            'moves': 'RD',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score,3)
        self.assertEqual(positions,[(1, 1), (2, 1), (0, 2)] )

    def test_simple_5x5_grid_complex_moves(self):

        config = {
            'size': 10,
            'zombie_start': (0,4),
            'creatures': [(9,4)],
            'moves': 'LLUUUUU',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score,1)
        self.assertEqual(positions,[(7, 9), (8, 9)])

    def test_big_grid(self):
        # lets go crazy
        config = {
            'size': 500000,
            'zombie_start': (200000, 200001),
            'creatures': [(200000,200000)],
            'moves': 'UDUD',
        }

        z_config = Config(config)
        zombie_land = ZombieLand(z_config)
        score, positions = zombie_land.release_the_zombie()
        self.assertEqual(score,1)
        self.assertEqual(positions,[(200000, 200000), (200000, 200001)])
