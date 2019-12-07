#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `photo` module."""

import pytest
from unittest import mock
from photopy.photo import Photo
from unittest.mock import patch


@pytest.fixture
@patch('os.path.isfile')
def p(isfile_mock):
    isfile_mock.return_value = True
    return Photo('/path/to/photo')


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


@patch('PIL.Image.open')
def test_populate_exif_data_exception(open_mock, p):
    m = mock.Mock()
    m._getexif.return_value = ''
    open_mock.return_value = m
    with pytest.raises(Exception):
        assert p._populate_exif_data() == []


@patch('imagehash.phash')
@patch('PIL.Image.open')
def test_populate_signature(open_mock, phash_mock, p):
    m = mock.Mock()
    m._getexif.return_value = ''
    open_mock.return_value = m
    phash_mock.return_value = 'image_hash'
    assert p._populate_signature() == 'image_hash'


# This test is used only for 100% coverage as both
# _populate methods are covered in other tests
@patch('photopy.photo.Photo._populate_exif_data')
@patch('photopy.photo.Photo._populate_signature')
def test_populate(popsig_mock, popexif_mock, p):
    popsig_mock.return_value = 'signature_populated'
    popexif_mock.return_value = 'exif_populated'
    p.populate()
    assert p.signature == 'signature_populated'
    assert p.exif_data == 'exif_populated'
