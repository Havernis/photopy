# -*- coding: utf-8 -*-

"""file module."""

import os
import hashlib

BUF_SIZE = 65536  # 64K chunk


class File:
    def __init__(self, path):
        if os.path.isfile(path):
            self.path = path
        else:
            print(f"Exception was raised in File.init({path})")
            raise Exception

    def _populate_name(self):
        name_with_ext = os.path.basename(self.path)
        name = os.path.splitext(name_with_ext)[0]
        return name

    def _populate_hash(self):
        md5 = hashlib.md5()
        with open(self.path, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
        f.close()
        return md5.hexdigest()

    def _populate(self):
        self.name = self._populate_name()
        self.hash = self._populate_hash()

    def get_file_details(self):
        self._populate()
        return (self.path, self.name, self.hash)
