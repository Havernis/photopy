#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `scanner` module."""


import pytest
from photopy.scanner import Scanner
from unittest.mock import patch


@pytest.fixture
@patch('os.path.isdir')
def scanner_fixture(mock_isdir):
    mock_isdir.return_value = True
    return Scanner('path/to/root/folder')


def test_init(scanner_fixture):
    assert isinstance(scanner_fixture, Scanner)
    assert scanner_fixture.root_path == 'path/to/root/folder'


def test_init_no_path():
    with pytest.raises(Exception):
        Scanner()


@patch('os.path.isdir')
def test_init_invalid_path(mock_isdir):
    mock_isdir.return_value = False
    with pytest.raises(Exception):
        Scanner('path/to/root/folder/which/does/not/exists')


@patch('photopy.photo.Photo.__init__')
@patch('os.path.isfile')
@patch('os.walk')
def test_scan(walk_patch, isfile_mock, photo_mock, scanner_fixture):
    walk_patch.return_value = [('/foo', (), ('photo.jpeg', 'file.txt'))]
    isfile_mock.return_value = True
    photo_mock.return_value = None
    list_of_files = scanner_fixture.scan()
    assert isinstance(list_of_files, list)
    assert isinstance(list_of_files[0], object)
    assert len(list_of_files) == 2
