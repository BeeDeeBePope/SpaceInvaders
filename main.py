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
    window = pygame.display.set_mode(width_height)
    pygame.display.set_caption(caption)

    return window


def initialize():
    pygame.font.init()


class Ship:
    def __init__(self, x, y, image, laser, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health
        self.image = image
        self.laser = laser
        self.lasers = []
        self.cool_down_counter = 0

        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        # color = (255, 0, 0)
        # rect = (self.x, self.y, 50, 50)
        # pygame.draw.rect(window, color, rect)

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()


class Player(Ship):
    def __init__(self, x, y, image, laser, health=100):
        super().__init__(x, y, image, laser, health=health)


class Enemy(Ship):
    def __init__(self, x, y, image, laser, health=100):
        super().__init__(x, y, image, laser, health=health)


def main():
    """Main function of Space Invaders game
    """
    initialize()
    inputs = InputsTemp()

    ui_font = pygame.font.SysFont("Comic Sans MS", 50)

    assets_library = AssetsLibrary((Path(__file__).parent / "Assets"))

    # todo: create display class to wrap display from pygame
    window = setup_display(inputs.width_height)

    background_img = assets_library.assets.bg_black

    run = True
    FPS = 60
    lives = 5
    level = 1
    player_vel = 5
    clock = pygame.time.Clock()

    ui_margin = {
        "left": 10,
        "right": 10,
        "top": 10,
        "bottom": 10,
    }

    player = Player(300, 300, assets_library.assets.ships.yellow.data, assets_library.assets.projectiles.laser_yellow.data)

    def redraw_window():
        window.blit(background_img.get_image(inputs.width_height), (0, 0))

        lives_label = ui_font.render(f"lives: {lives}", 1, (255, 255, 255))
        level_label = ui_font.render(f"level: {level}", 1, (255, 255, 255))

        window.blit(lives_label, (ui_margin["left"], ui_margin["top"]))
        window.blit(level_label, (inputs.width_height[0] - level_label.get_width() - ui_margin["right"], ui_margin["top"]))

        player.draw(window)

        pygame.display.update()

    while run:
        clock.tick(FPS)

        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel

        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < inputs.width_height[0]:
            player.x += player_vel

        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel

        if keys[pygame.K_s] and player.y + player_vel + player.get_width() < inputs.width_height[1]:
            player.y += player_vel

        if keys[pygame.K_ESCAPE]:
            run = False

    print("Game ended")


if __name__ == "__main__":
    main()
