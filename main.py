import pygame
import os
import time
import random
from pathlib import Path

from tools.asset_library import AssetsLibrary

class Image:
    def __init__(self, image_file_path: Path):
        self.data = pygame.image.load(str(image_file_path))


def main():
    assets_library = AssetsLibrary((Path(__file__).parent / "Assets"))
    
    img_path = assets_library.assets.ships.red
    
    img = Image(img_path)
    
    print(img)
    

if __name__ == "__main__":
    main()