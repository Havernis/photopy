# -*- coding: utf-8 -*-

"""photo module."""

import os
from photopy.file import *
from PIL import Image
from PIL.ExifTags import TAGS
import imagehash


class Photo(File):
    def __init__(self, path):
        super().__init__(path)
        # self.exif_data = None

    # def _populate_exif_data(self):
    #     exif = []
    #     img = Image.open(self.path)
    #     raw_exif_data = img._getexif()
    #     if raw_exif_data is None:
    #         return exif
    #     try:
    #         for tag, value in raw_exif_data.items():
    #             if TAGS.get(tag, tag) in ['Manufacturer', 'Make', 'Model']:
    #                 exif.append((TAGS.get(tag, tag), value))
    #     except:
    #         raise Exception
    #     return exif

    def _populate_size(self):
        return os.path.getsize(self.path)

    def _populate_hash(self):
        img = Image.open(self.path)
        img_hash = str(imagehash.phash(img))
        return img_hash

    def _populate(self):
        self.size = self._populate_size()
        self.hash = self._populate_hash()
        # self.exif_data = self._populate_exif_data()

    def get_file_details(self):
        self._populate()
        return (self.path, self.size, self.hash)
