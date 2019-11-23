# -*- coding: utf-8 -*-

"""scan module."""

import os
# from photopy.file import File
from photopy.photo import Photo


EXT_PHOTOS = ('jpeg', 'exif', 'tiff', 'tif', 'gif', 'bmp', 'png', 'svg', 'jpg', 'jif', 'jfif', 'jp2', 'jpx', 'j2k', 'j2c', 'pcd', 'pdf')


class Scan:
    def __init__(self, root_path, db_path, db_records):
        self.root_path = root_path
        self.db_path = db_path
        self.db_records = db_records

    def scan(self, root_path):
        list_of_files = []
        for root, dirs, files_names in os.walk(root_path):
            for file_name in files_names:
                if file_name.endswith(EXT_PHOTOS):
                    f = Photo(os.path.join(root, file_name))
                # else:
                    # f = File(os.path.join(root, file))
                    list_of_files.append(f)  # Need to be less intented once I choose to add File functionality
        return list_of_files
