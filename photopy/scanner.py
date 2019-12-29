# -*- coding: utf-8 -*-

"""scanner module."""

import os
from photopy.file import *
# from photo import *


# EXT_PHOTOS = ('jpeg', 'exif', 'tiff', 'tif', 'gif', 'bmp', 'png', 'svg', 'jpg', 'jif', 'jfif', 'jp2', 'jpx', 'j2k', 'j2c', 'pcd')
# Need also to add this statement: if file_name.lower().endswith(EXT_PHOTOS):


class Scanner:
    def __init__(self, root_path):
        if os.path.isdir(root_path):
            self.root_path = root_path
        else:
            print(f"\nException was raised in Scanner.init({root_path})")
            raise Exception

    def scan(self):
        list_of_files = []
        for root, dirs, files in os.walk(self.root_path):
            for file in files:
                try:
                    f = File(os.path.join(root, file))
                    list_of_files.append(f)
                except:  # Any exception at the moment.
                    continue
            print('#', flush=True, end='')
        print()
        return list_of_files

    def scan_for_duplicates(self, list_of_ordered_records):
        duplicates_list = []
        clean_list = [[None, None, None], ]
        count_duplicates = 0
        for record in list_of_ordered_records:
            if record[2] == clean_list[-1][2]:
                duplicates_list.append(record[0])  # append only file_path
                count_duplicates += 1
            else:
                clean_list.append(record)
        print(f"Found total {count_duplicates} duplicates")
        return duplicates_list

    def scan_for_simillar(self):
        # To be implemented in the future. Need to change the hashing algorythm
        pass
