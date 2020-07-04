import json
from challenge.zombie_exceptions import IncorrectConfig

DIRECTIONS_MAP = {'U': (0, -1),
                  'D': (0, 1),
                  'L': (-1, 0),
                  'R': (1, 0),
                  }


class Config(object):

    def __init__(self, config_dict):
        """
        :param (dict) config_dict: contains configuration data to build Zombieland.
        Example:
            {
                'size': 4,
                'zombie_start': (2, 1),
                'creatures': [(0, 1),(1, 2),(3, 1)],
                'moves': 'DLUURR',
            }

        """
        self.config = config_dict.copy()
        self.validate()
        self.config['zombie_start'] = tuple(self.config['zombie_start'])
        for index, loc in enumerate(self.config['creatures']):
            if isinstance(loc,list):
                self.config['creatures'][index] = tuple(loc)


    @classmethod
    def load_from_file(cls,file_name):
        with open(file_name) as f:
            data = json.load(f)
        return cls(data)

    @staticmethod
    def _validate_int_tuple(the_tuple, tuple_name):

        if not the_tuple:
            raise IncorrectConfig(tuple_name,'value not defined')

        elif not type(the_tuple) in [tuple,list]:
            raise IncorrectConfig(tuple_name,'value must be a tuple')

        elif not len(the_tuple)==2:
            raise IncorrectConfig(tuple_name, 'value must be a tuple of 2 items')

        elif not (isinstance(the_tuple[0], int) and isinstance(the_tuple[1], int)):
            raise IncorrectConfig(tuple_name, 'value must be a tuple of 2 integers')

    def validate(self):
        # location are with in grid ?

        if not self.size:
            raise IncorrectConfig('size','size not defined')
        elif not isinstance(self.size, int):
            raise IncorrectConfig('size','size does not have correct value')

        self._validate_int_tuple(self.zombie_start,'zombie_start')

        for creature_loc in self.creatures:
            self._validate_int_tuple(creature_loc,'creatures')

        if not self.moves:
            raise IncorrectConfig('moves','moves not defined')
        elif not isinstance(self.moves, str):
            raise IncorrectConfig('moves', 'moves must be string')
        else:
            invalids=''
            for mv in self.moves:
                if mv not in DIRECTIONS_MAP.keys():
                    invalids+=mv
            if invalids !='':
                raise IncorrectConfig('moves', 'invalid moves {}'.format(invalids))

    @property
    def size(self):
        return self.config.get('size')

    @property
    def zombie_start(self):
        return self.config.get('zombie_start')

    @property
    def creatures(self):
        return self.config.get('creatures')

    @property
    def moves(self):
        return self.config.get('moves')
