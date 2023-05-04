import os

def get_local_assets_path(fileName: str):
    return os.path.join(os.path.dirname(__file__), "assets", fileName)