# -*- coding: utf-8 -*-

"""file module."""

import os


class File:
    def __init__(self, path):
        # check if file exists before it is being accessed
        if os.path.isfile(path):
            self.path = path
        else:
            raise ValueError
        self.name = None
        self.extension = None
        self.signature = None

    def populate(self):
        self.name = self._populate_name()
        self.extension = self._populate_extension()
        self.signature = self._populate_signature()

    def _populate_name(self):
        name_with_ext = os.path.basename(self.path)
        name = os.path.splitext(name_with_ext)[0]
        return name

    def _populate_signature(self):
        # ToDo: Need to refactor this method as the signature is being
        # populated twice - once in File.__init__ and once here
        return 'signature'

    def _populate_extension(self):
        name_with_ext = os.path.basename(self.path)
        # we use the second [] to remove the '.' from ext
        ext = os.path.splitext(name_with_ext)[1][1:]
        return ext
