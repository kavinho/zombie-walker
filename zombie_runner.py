import sys, getopt
from challenge.zombie_land import ZombieLand
from challenge.zombie_exceptions import IncorrectConfig
from challenge.config import Config

def main(argv):

    try:
        opts, _ = getopt.getopt(argv, "f:")
    except getopt.GetoptError:
        print('zombie_runner.py -i <name.json>')
        print('or no arguments to use input.json file name')
        print('zombie_runner.py ')
        sys.exit(2)

    input_file = opts[0][1] if len(opts) else 'input.json'

    try:
        z_config = Config.load_from_file(input_file)
    except IncorrectConfig as ice:
        print('Incorrect configuration detected.' , ice)
        exit(2)
    except Exception as e:
        print('encountered and error while loading/analysing config.' , e)
        exit(2)

    zombie_land = ZombieLand(z_config)
    score, positions = zombie_land.release_the_zombie()

    print('zombies score:', score)
    print('zombies positions:\n', positions)


if __name__ == "__main__":
    main(sys.argv[1:])
