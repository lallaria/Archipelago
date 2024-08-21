import os
import sys

def setup_lib_path():
    """ensure lib folder is part of the sys.path to load dependencies."""
    base_path = os.path.dirname(__file__)
    lib_path = os.path.join(base_path, "lib")
  
    #print("Using local lib folder")
    if lib_path not in sys.path:
        sys.path.append(lib_path)
    #print(f"lib folder added to path: {lib_path}")
    return lib_path
