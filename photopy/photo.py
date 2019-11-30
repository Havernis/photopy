# -*- coding: utf-8 -*-

"""photo module."""

import sys
from photopy.file import File
from PIL import Image
from PIL.ExifTags import TAGS
import imagehash


class Photo(File):
    def __init__(self, path):
        File.__init__(self, path)
        self.signature = None
        self.exif_data = None

    def populate(self):
        self.signature = self._populate_signature()
        self.exif_data = self._populate_exif_data()

    def _populate_exif_data(self):
        exif = []
        img = Image.open(self.path)
        raw_exif_data = img._getexif()
        if raw_exif_data is None:
            return exif
        try:
            for tag, value in raw_exif_data.items():
                exif.append((TAGS.get(tag, tag), value))
        except Exception as e:
            raise e
        return exif

    def _populate_signature(self):
        img = Image.open(self.path)
        img_hash = str(imagehash.phash(img))
        return img_hash
