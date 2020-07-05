"""Module with wprapper classes for pygame
"""
from pathlib import Path
import pygame

class Image:
    """Wrapper class for pygame's image.
    """

    # File extensions retrieved from  pygame documentation: https://www.pygame.org/docs/ref/image.html
    EXTENSIONS = ["jpg", "png", "gif", "bmp", "pcx", "tga", "tif", "lbm", "pbm", "pgm", "ppm", "xpm"]

    def __init__(self, image_file_path: Path):
        self.data = pygame.image.load(str(image_file_path))

    def get_image(self, scale):
        out = self.data

        out = pygame.transform.scale(out, scale)
        return out
