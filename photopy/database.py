# -*- coding: utf-8 -*-

"""database module."""

# import os


class Database:
    def __init__(self, path):
        self.path = path

    def get_sorted_records(self):
        return ['test_record_1', 'test_record_2']

    def insert_records(self, list_of_records):
        return True

    def delete_records(self, list_of_records):
        return True
