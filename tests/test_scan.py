#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `scan` module."""


import pytest
from photopy.scan import Scan
from unittest.mock import patch
# from photopy.photo import Photo
# from photopy.photo import File


@pytest.fixture
@patch('os.path.isdir')
def scan_fixture(mock_isdir):
    mock_isdir.return_value = True
    return Scan('path/to/root/folder')


def test_init(scan_fixture):
    assert isinstance(scan_fixture, Scan)
    assert scan_fixture.root_path == 'path/to/root/folder'


def test_init_no_path():
    with pytest.raises(Exception):
        Scan()


@patch('os.path.isdir')
def test_init_invalid_path(mock_isdir):
    mock_isdir.return_value = False
    with pytest.raises(Exception):
        Scan('path/to/root/folder/which/does/not/exists')


@patch('photopy.photo.Photo.__init__')
@patch('os.path.isfile')
@patch('os.walk')
def test_scan(walk_patch, isfile_mock, photo_mock, scan_fixture):
    walk_patch.return_value = [('/foo', (), ('photo.jpeg', 'file.txt'))]
    isfile_mock.return_value = True
    photo_mock.return_value = None
    list_of_files = scan_fixture.scan()
    assert isinstance(list_of_files, list)
    assert isinstance(list_of_files[0], object)
    assert len(list_of_files) == 2
