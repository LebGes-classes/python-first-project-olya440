from game import (
    Game,
)
import os

if __name__ == "__main__":
    game = Game(40, 20)
    game.execute()
    os.system('cls' if os.name == 'nt' else 'clear')