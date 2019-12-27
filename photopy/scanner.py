# -*- coding: utf-8 -*-

"""scanner module."""

import os
from file import *
# from photo import *


# EXT_PHOTOS = ('jpeg', 'exif', 'tiff', 'tif', 'gif', 'bmp', 'png', 'svg', 'jpg', 'jif', 'jfif', 'jp2', 'jpx', 'j2k', 'j2c', 'pcd')
# Need also to add this statement: if file_name.lower().endswith(EXT_PHOTOS):


class Scanner:
    def __init__(self, root_path):
        if os.path.isdir(root_path):
            self.root_path = root_path
        else:
            print(f"Exception was raised in Scanner.init({root_path})")
            raise Exception

    def scan(self):
        list_of_files = []
        for root, dirs, files in os.walk(self.root_path):
            for file in files:
                f = File(os.path.join(root, file))
                list_of_files.append(f)
            print('#', flush=True, end='')
        print()
        return list_of_files
