from DND_Game.actors import Creature

def main():
    print_header()
    game_loop()

def print_header():
    print('-------------------------')
    print('      WIZARD GAME        ')
    print('-------------------------')
    print()

def game_loop():
    creatures = [
        Creature('Toad', 1),
        Creature('Bat', 5),
        Creature('Tiger', 12),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]

    print(creatures)

    hero = None # TODO: Create out hero

    while True:

        #Randomly choose a creature
        active_creature = None
        print('A [] of level [] has appeared from a dark and foggy forest...'.format(...))

if __name__ == '__main__':
    main()

