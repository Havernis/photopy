# -*- coding: utf-8 -*-

"""file module."""

import os


class File:
    def __init__(self, path):
        # check if file exists
        if os.path.isfile(path):
            self.path = path
        else:
            raise ValueError
        self.name = self._populate_name()
        self.extension = self._populate_extension()
        self.signature = self._populate_signature()

    def _populate_name(self):
        return 'name'

    def _populate_signature(self):
        # ToDo: Need to refactor this method as the signature is being
        # populated twice - once in File.__init__ and once here
        return 'signature'

    def _populate_extension(self):
        return 'ext'
