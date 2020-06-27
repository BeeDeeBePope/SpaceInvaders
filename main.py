"""The main module of Space Invaders game
"""
import os
import time
import random
from pathlib import Path

from tools.asset_library import AssetsLibrary


def main():
    """Main function of Space Invaders game
    """
    assets_library = AssetsLibrary((Path(__file__).parent / "Assets"))

    img = assets_library.assets.ships.red

    print(img)


if __name__ == "__main__":
    main()
