# -*- coding: utf-8 -*-

"""file module."""

import os


class File:
    def __init__(self, path):
        # check if file exists before it being accessed
        if os.path.isfile(path):
            self.path = path
        else:
            raise ValueError
        self.name = None
        self.extension = None
        self.signature = None

    def populate(self):
        self._populate_name()
        self._populate_extension()
        self._populate_signature()

    def _populate_name(self):
        self.name = 'name'

    def _populate_signature(self):
        # ToDo: Need to refactor this method as the signature is being
        # populated twice - once in File.__init__ and once here
        self.signature = 'signature'

    def _populate_extension(self):
        self.extension = 'ext'
