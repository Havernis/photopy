#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `database` module."""

import pytest
# from unittest.mock import patch
from photopy.database import Database


@pytest.fixture
def database_fixture():
    return Database('/path/to/database')


def test_init(database_fixture):
    assert database_fixture.path == '/path/to/database'


def test_init_no_path():
    with pytest.raises(Exception):
        Database()


def test_get_sorted_records(database_fixture):
    assert database_fixture.get_sorted_records() == ['test_record_1', 'test_record_2']


def test_insert_records(database_fixture):
    list_of_records = ['test_record_1', 'test_record_2']
    assert database_fixture.insert_records(list_of_records) is True


def test_delete_records(database_fixture):
    list_of_records = ['test_record_1', 'test_record_2']
    assert database_fixture.delete_records(list_of_records) is True
