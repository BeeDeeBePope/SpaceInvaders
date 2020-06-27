"""The main module of Space Invaders game
"""
import os
import time
import random
from pathlib import Path

import pygame

from tools.asset_library import AssetsLibrary


class InputsTemp:
    """Temporary class for inputs.
    """
    def __init__(self):
        self.width_height = (750, 750)


def setup_display(width_height: tuple, caption: str="Space Invaders"):
    """Display setup function

    Args:
        width_height (tuple): tuple with window size (width, height)
        caption (str, optional): The caption on window ribon. Defaults to "Space Invaders".
    """
    pygame.display.set_mode(width_height)
    pygame.display.set_caption(caption)


def main():
    """Main function of Space Invaders game
    """
    inputs = InputsTemp()

    assets_library = AssetsLibrary((Path(__file__).parent / "Assets"))

    # todo: create display class to wrap display from pygame
    setup_display(inputs.width_height)

    img = assets_library.assets.ships.red

    run = True
    FPS = 60
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    print("Game ended")


if __name__ == "__main__":
    main()
