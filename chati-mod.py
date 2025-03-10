import os
import zipfile
import shutil
import compileall
from worlds.chatipelago import ItemName, Regions

chatifolder = os.path.join(os.curdir, 'worlds', 'chatipelago')
custom_name = ""
shutil.copy(chatifolder)

def copy_item_names(item_names: dict):
    with open(os.path.join(chatifolder, 'ItemName.py'), 'w', encoding='UTF-8') as inpy:
        for var, name in item_names.items():
            inpy.write(f"{var} = '{name}'\n")

def copy_loc_names(loc_names: dict):
    ## recreate the whole stupid file
    region_header = f"""from typing import NamedTuple, Optional

from BaseClasses import Location, Region

class ChatipelagoLoc(Location):
    game: str = "Chatipelago{custom_name}"

class ChatipelagoLocationData(NamedTuple):
    region: str
    address: Optional[int] = None

class ChatipelagoRegionData(NamedTuple):
    connecting_regions: list[str] = []

    """
    region_footer = """

    """


def recompile_apworld(mod_name: str):
    world_directory = os.path.join(f'{self.libfolder}/worlds/chatipelago')
    # this method creates an apworld that cannot be moved to a different OS or minor python version,
    # which should be ok
    with zipfile.ZipFile(f"chatipelago{custom_name}.apworld", "x", zipfile.ZIP_DEFLATED,
                            compresslevel=9) as zf:
        for path in world_directory.rglob("*.*"):
            relative_path = os.path.join(*path.parts[path.parts.index("worlds")+1:])
            zf.write(path, relative_path)
    shutil.rmtree(world_directory)
shutil.copyfile("meta.yaml", self.buildfolder / "Players" / "Templates" / "meta.yaml")

def send_yaml(player_name: str, formatted_options: dict) -> Response:
    response = Response(yaml.dump(formatted_options, sort_keys=False))
    response.headers["Content-Type"] = "text/yaml"
    response.headers["Content-Disposition"] = f"attachment; filename={player_name}.yaml"
    return response