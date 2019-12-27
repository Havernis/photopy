# -*- coding: utf-8 -*-

"""database module."""

import sqlite3

TABLE_NAME_FILES = 'files'
SQL_TABLE_EXISTS_FILES = f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME_FILES}';"""
SQL_TABLE_CREATE_FILES = f"""CREATE TABLE {TABLE_NAME_FILES}(path TEXT NOT NULL PRIMARY KEY, filename TEXT, hash TEXT);"""
SQL_INSERT_RECORDS_FILES = f"""INSERT INTO {TABLE_NAME_FILES} (path, filename, hash) VALUES(?,?,?);"""
SQL_SELECT_RECORDS_FILES = f"""SELECT * FROM {TABLE_NAME_FILES} ORDER BY hash"""

# TABLE_NAME_PHOTOS = 'photos'
# SQL_TABLE_EXISTS_PHOTOS = f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME_PHOTOS}';"""
# SQL_TABLE_CREATE_PHOTOS = f"""CREATE TABLE {TABLE_NAME_PHOTOS}(id INTEGER NOT NULL PRIMARY KEY, filename TEXT, path TEXT, hash TEXT, exifdata TEXT);"""
# SQL_INSERT_RECORDS_PHOTOS = f"""INSERT INTO {TABLE_NAME_PHOTOS} (filename, path, hash, exifdata) VALUES(?,?,?,?);"""
# SQL_SELECT_RECORDS_PHOTOS = f"""SELECT * FROM {TABLE_NAME_PHOTOS} ORDER BY hash, exifdata"""


class Database:
    def __init__(self, path):
        self.path = path

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.path)
        except sqlite3.OperationalError as error:
            raise error

    def close_connection(self):
        try:
            self.connection.commit()
            self.connection.close()
        except sqlite3.OperationalError as error:
            raise error

    def cursor(self):
        try:
            self.cursor = self.connection.cursor()
        except sqlite3.OperationalError as error:
            raise error

    def close_cursor(self):
        try:
            self.cursor.close()
        except sqlite3.OperationalError as error:
            raise error

    def table_exists(self):
        self.cursor.execute(SQL_TABLE_EXISTS_FILES)
        if len(self.cursor.fetchall()) == 1:
            return True
        return False

    def create_table(self):
        try:
            self.cursor.execute(SQL_TABLE_CREATE_FILES)
        except sqlite3.OperationalError as error:
            raise error

    def insert_records(self, records_list):
        try:
            # for record in records_list:
            self.cursor.executemany(SQL_INSERT_RECORDS_FILES, records_list)
        except sqlite3.OperationalError as error:
            raise error

    def read_records(self):
        try:
            self.cursor.execute(SQL_SELECT_RECORDS_FILES)
        except sqlite3.OperationalError as error:
            raise error
        return self.cursor.fetchall()


# ToDo CRUD:
# 5. update records
# 6. delete records
