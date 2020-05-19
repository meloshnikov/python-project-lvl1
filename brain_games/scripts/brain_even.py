#!/usr/bin/python3
from brain_games.engine.flow import game_launch
from brain_games.games.even import even


def main():
    game_launch(even)


if __name__ == '__main__':
    main()
