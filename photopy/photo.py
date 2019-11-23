# -*- coding: utf-8 -*-

"""photo module."""

from photopy.file import File


class Photo(File):
    def __init__(self, path):
        File.__init__(self, path)
        self.signature = self._populate_signature()
        self.exif_data = self._populate_exif_data()

    def _populate_exif_data(self):
        return {}

    def _populate_signature(self):
        return 'photo_signature'
