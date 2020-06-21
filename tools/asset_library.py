from pathlib import Path


class AssetsNamespace:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        #todo: figure out how to use repr here so that all assets can be displayed like a tree
        return f"{self.name}<AssetsNamespace>: {', '.join([a for a in self.__dir__() if not str(a).startswith('_')])}"
    
class AssetsLibrary:
    def get_assets_from_folder(self, folder: Path, current_attribute: AssetsNamespace) -> list:
            out_folders = []
            assets_folder_contents = folder.iterdir()

            for asset in assets_folder_contents:
                if asset.is_dir() and next(asset.iterdir(), None):
                    setattr(current_attribute, asset.name, AssetsNamespace(asset.name))
                    out_folders.append((asset, getattr(current_attribute, asset.name)))
                else:
                    setattr(current_attribute, str(asset.name).split('.')[0], asset.resolve())
                    
            return out_folders


    def __init__(self, assets_folder: Path):
        self.assets_folder = assets_folder
        self.assets = AssetsNamespace("assets")

        folders = [(assets_folder, getattr(self, "assets"))]
        while folders:
            current_folder = folders.pop()
            out = self.get_assets_from_folder(current_folder[0], current_folder[1])
            folders.extend(out)