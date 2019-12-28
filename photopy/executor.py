# -*- coding: utf-8 -*-

"""executor module."""

import os
import shutil
from random import randint

class Executor:
    def __init__(self):
        pass

    def execute(self, files_list, duplicated_folder_path, action='move'):
        self.files_list = files_list
        self.duplicated_folder_path = duplicated_folder_path
        self.action = action

        if self.action == 'delete':
            return self._delete()
        else:  # everything else to cover even a typo and avoid deletion
            return self._move()

    def _move(self):
        self._create_dir_for_duplicates()
        for file in self.files_list:
            filename = os.path.basename(file)
            if not os.path.isfile(os.path.join(self.duplicated_folder_path, filename)):
                shutil.move(file, self.duplicated_folder_path)
            else:  # file with the same name already exists in dest folder..
                name_and_extention = os.path.splitext(filename)
                random_int = str(randint(0, 10000))
                new_filename = name_and_extention[0] + '_' + random_int + name_and_extention[1]
                print(os.path.join(self.duplicated_folder_path, new_filename))
                shutil.move(file, os.path.join(self.duplicated_folder_path, new_filename))

    def _delete(self):
        return True

    def _create_dir_for_duplicates(self):
        if os.path.isdir(self.duplicated_folder_path):
            print(f"Duplicated folder found in {self.duplicated_folder_path} path, writting into it")
            return
        os.mkdir(self.duplicated_folder_path)
        return
