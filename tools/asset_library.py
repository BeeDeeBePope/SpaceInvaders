"""Module with AssetLibrary implementaation
"""

from pathlib import Path

from .pygame_wrappers import Image


class AssetsNamespace:
    """A class to add attributees to  dynamically.
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        #todo: figure out how to use repr here so that all assets can be displayed like a tree
        return f"{self.name}<AssetsNamespace>: {', '.join([a for a in self.__dir__() if not str(a).startswith('_')])}"

class AssetsLibrary:
    """ Asset files reader.

    A class which dynamically interprets Assets folder to add attributes for accessing pygame assets.
    """
    def _get_assets_from_folder(self, folder: Path, current_attribute: AssetsNamespace) -> list:
        out_folders = []
        assets_folder_contents = folder.iterdir()

        for asset in assets_folder_contents:
            if asset.is_dir() and next(asset.iterdir(), None):
                setattr(current_attribute, asset.name, AssetsNamespace(asset.name))
                out_folders.append((asset, getattr(current_attribute, asset.name)))
            else:
                file_name_info = str(asset.name).split('.')
                value = asset.resolve()
                if file_name_info[1] in Image.EXTENSIONS:
                    value = Image(asset.resolve())

                setattr(current_attribute, file_name_info[0], value)

        return out_folders

    __get_assets_from_folder = _get_assets_from_folder

    def __init__(self, assets_folder: Path):
        self.assets_folder = assets_folder
        self.assets = AssetsNamespace("assets")

        folders = [(assets_folder, getattr(self, "assets"))]
        while folders:
            current_folder = folders.pop()
            out = self.__get_assets_from_folder(current_folder[0], current_folder[1])
            folders.extend(out)
