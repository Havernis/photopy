#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `scan` module."""


import pytest
from photopy.scan import Scan
from photopy.photo import Photo
from photopy.photo import File
from unittest.mock import patch


@pytest.fixture
def s():
    return Scan('path/to/root/folder', 'path/to/db', [])


def test_init(s):
    assert isinstance(s, Scan)
    assert s.root_path == 'path/to/root/folder'
    assert s.db_path == 'path/to/db'
    assert isinstance(s.db_records, list)


def test_scan(s):
    with patch('os.walk') as walk_patch:
        walk_patch.return_value = [('/foo', (), ('photo.jpeg', 'file.txt'))]
        with patch('os.path.isfile') as isfile_mock:  # File init checks if file exists or not
            isfile_mock.return_value = True
            list_of_files = s.scan('/root_path')
            assert isinstance(list_of_files, list)
            assert isinstance(list_of_files[0], Photo)
            # assert isinstance(list_of_files[1], File)
            # asset size of list_of_files