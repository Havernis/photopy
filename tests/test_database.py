#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `database` module."""

import pytest
from unittest.mock import patch
from photopy.database import Database
from unittest.mock import Mock
from sqlite3 import OperationalError


@pytest.fixture
def database_fixture():
    return Database('/path/to/database')


def test_init(database_fixture):
    assert database_fixture.path == '/path/to/database'


def test_init_no_path():
    with pytest.raises(Exception):
        Database()


@patch('sqlite3.connect')
def test_connect(connect_mock, database_fixture):
    connect_mock.return_value = Mock()
    database_fixture.connect()
    assert isinstance(database_fixture.connection, Mock)


@patch('sqlite3.connect')
def test_unable_to_connect(connect_mock, database_fixture):
    with pytest.raises(Exception):
        connect_mock.side_effect = OperationalError
        database_fixture.connect()


def test_cursor(database_fixture):
    database_fixture.connection = Mock()
    database_fixture.cursor()
    assert isinstance(database_fixture.cursor, Mock)


def test_cursor_no_connection(database_fixture):
    with pytest.raises(Exception):
        # database_fixture.connection = None
        database_fixture.cursor()


def test_cursor_unable_to_cursor(database_fixture):
    with pytest.raises(Exception):
        connection_mock = Mock()
        connection_mock.cursor.side_effect = OperationalError
        database_fixture.connection = connection_mock
        database_fixture.cursor()


def test_close_connection(database_fixture):
    database_fixture.connection = Mock()
    database_fixture.close_connection()


def test_unable_to_close_connection(database_fixture):
    with pytest.raises(Exception):
        connection_mock = Mock()
        connection_mock.close.side_effect = OperationalError
        database_fixture.connection = connection_mock
        database_fixture.close_connection()


def test_close_cursor(database_fixture):
    database_fixture.cursor = Mock()
    database_fixture.close_cursor()


def test_unable_to_close_cursor(database_fixture):
    with pytest.raises(Exception):
        database_fixture.cursor = Mock()
        database_fixture.cursor.close.side_effect = OperationalError
        database_fixture.close_cursor()


def test_table_exists_true(database_fixture):
    database_fixture.cursor = Mock()
    database_fixture.cursor.fetchall.return_value = ['photos']
    assert database_fixture.table_exists() is True


def test_table_exists_false(database_fixture):
    database_fixture.cursor = Mock()
    database_fixture.cursor.fetchall.return_value = ['something', 'else']
    assert database_fixture.table_exists() is False


def test_create_table(database_fixture):
    database_fixture.cursor = Mock()
    database_fixture.create_table()


def test_unable_to_create_table(database_fixture):
    with pytest.raises(Exception):
        database_fixture.cursor = Mock()
        database_fixture.cursor.execute.side_effect = OperationalError
        database_fixture.create_table()


def test_create_records(database_fixture):
    list_of_records = [['file_name', 'path_to_file', 'signature', 'exif_data']]
    database_fixture.cursor = Mock()
    database_fixture.create_records(list_of_records)


# ToDo:
# 1. test create_records raise error
# 2. test read_records + raise error
