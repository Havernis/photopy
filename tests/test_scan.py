#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `scan` module."""


import pytest
from photopy.scan import Scan
from unittest.mock import patch
# from photopy.photo import Photo
# from photopy.photo import File


@pytest.fixture
def s():
    return Scan('path/to/root/folder', 'path/to/db', [])


def test_init(s):
    assert isinstance(s, Scan)
    assert s.root_path == 'path/to/root/folder'
    assert s.db_path == 'path/to/db'
    assert isinstance(s.db_records, list)


@patch('photopy.photo.Photo.__init__')
@patch('os.path.isfile')
@patch('os.walk')
def test_scan(walk_patch, isfile_mock, photo_mock, s):
    walk_patch.return_value = [('/foo', (), ('photo.jpeg', 'file.txt'))]
    isfile_mock.return_value = True
    photo_mock.return_value = None
    list_of_files = s.scan('/root_path')
    assert isinstance(list_of_files, list)
    assert isinstance(list_of_files[0], object)
    # assert isinstance(list_of_files[1], File)
    # asset size of list_of_files
