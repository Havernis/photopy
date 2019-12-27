# -*- coding: utf-8 -*-

"""photo module."""

from file import *
from PIL import Image
from PIL.ExifTags import TAGS
import imagehash


class Photo(File):
    def __init__(self, path):
        File.__init__(self, path)
        self.hash = None
        self.exif_data = None

    def photo_details(self):
        self.populate()
        return (self.name, self.path, self.hash, str(self.exif_data))

    def populate(self):
        self.name = self._populate_name()
        self.hash = self._populate_hash()
        self.exif_data = self._populate_exif_data()

    def _populate_exif_data(self):
        exif = []
        img = Image.open(self.path)
        raw_exif_data = img._getexif()
        if raw_exif_data is None:
            return exif
        try:
            for tag, value in raw_exif_data.items():
                if TAGS.get(tag, tag) in ['Manufacturer', 'Make', 'Model']:
                    exif.append((TAGS.get(tag, tag), value))
        except:
            raise Exception
        return exif

    def _populate_hash(self):
        img = Image.open(self.path)
        img_hash = str(imagehash.phash(img))
        return img_hash
