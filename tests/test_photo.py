#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `photo` module."""

import pytest
from photopy.photo import Photo
from unittest.mock import patch
from unittest import mock


@pytest.fixture
@patch('os.path.isfile')
def p(isfile_mock):
    isfile_mock.return_value = True
    p = Photo('/path/to/photo')
    return p


def test_init(p):
    assert isinstance(p, Photo)
    assert p.path == '/path/to/photo'


@patch('PIL.Image.open')
def test_populate_exif_data_none(open_mock, p):
    m = mock.Mock()
    m._getexif.return_value = None
    open_mock.return_value = m
    assert p._populate_exif_data() == []


@patch('PIL.Image.open')
def test_populate_exif_data_try(open_mock, p):
    m = mock.Mock()
    m._getexif.return_value = {'key_A': 'val_A', 'key_B': 'val_B'}
    open_mock.return_value = m
    assert p._populate_exif_data() == [('key_A', 'val_A'), ('key_B', 'val_B')]
