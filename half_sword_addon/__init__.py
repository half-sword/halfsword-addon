bl_info = {
    "name": "HalfSword",
    "description": "halfsword tools",
    "author": "Hannes Delbeke",
    "wiki_url": "",
    "doc_url": "",
    "tracker_url": "https://github.com/half-sword/halfsword/issues",
    "version": (0, 3, 0),
    "blender": (2, 91, 0),
    "location": "",
    "support": "COMMUNITY",
    "category": "Interface",
}


import bpy
import os
import platform
import subprocess
import webbrowser
from pathlib import Path
import unimenu


menu_nodes = []


def setup():
    # register config paths
    addon_folder = Path(__file__).parent
    os.environ["UNIMENU_CONFIG_PATH"] = str(addon_folder / "configs" / "menu")
    os.environ["BUTTONIZER_CONFIG_DIRS"] = str(addon_folder / "configs" / "buttonizer")

    # create menu
    global menu_nodes
    menu_nodes = unimenu.setup_all_configs()


def teardown():
    # Teardown the menu if unimenu is installed.
    global menu_nodes
    for node in menu_nodes:
        node.teardown()


def register():
    # runs when addon is enabled, also on startup if enabled 
    setup()


def unregister():
    teardown()
