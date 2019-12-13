# -*- coding: utf-8 -*-

"""scanner module."""

import os
from photopy.file import File
from photopy.photo import Photo


EXT_PHOTOS = ('jpeg', 'exif', 'tiff', 'tif', 'gif', 'bmp', 'png', 'svg', 'jpg', 'jif', 'jfif', 'jp2', 'jpx', 'j2k', 'j2c', 'pcd', 'pdf')


class Scanner:
    def __init__(self, root_path):
        if os.path.isdir(root_path):
            self.root_path = root_path
        else:
            raise Exception

    def scan(self):
        list_of_files = []
        for root, dirs, files_names in os.walk(self.root_path):
            for file_name in files_names:
                if file_name.endswith(EXT_PHOTOS):
                    f = Photo(os.path.join(root, file_name))
                else:
                    f = File(os.path.join(root, file_name))
                list_of_files.append(f)
        return list_of_files
