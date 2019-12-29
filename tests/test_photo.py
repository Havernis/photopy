#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `photo` module."""

import pytest
from unittest import mock
from photopy.photo import Photo
from unittest.mock import patch


@pytest.fixture
@patch('os.path.isfile')
def photo_fixture(isfile_mock):
    isfile_mock.return_value = True
    return Photo('/path/to/photo')


def test_init(photo_fixture):
    assert isinstance(photo_fixture, Photo)
    assert photo_fixture.path == '/path/to/photo'


@patch('PIL.Image.open')
def test_populate_exif_data_none(open_mock, photo_fixture):
    m = mock.Mock()
    m._getexif.return_value = None
    open_mock.return_value = m
    assert photo_fixture._populate_exif_data() == []


@pytest.mark.skip(reason="To be fixed")
@patch('PIL.Image.open')
def test_populate_exif_data_try(open_mock, photo_fixture):
    m = mock.Mock()
    m._getexif.return_value = {'key_A': 'val_A', 'key_B': 'val_B'}
    open_mock.return_value = m
    assert photo_fixture._populate_exif_data() == [('key_A', 'val_A'), ('key_B', 'val_B')]


@patch('PIL.Image.open')
def test_populate_exif_data_exception(open_mock, photo_fixture):
    m = mock.Mock()
    m._getexif.return_value = ''
    open_mock.return_value = m
    with pytest.raises(Exception):
        assert photo_fixture._populate_exif_data() == []


@pytest.mark.skip(reason="To be fixed")
@patch('imagehash.phash')
@patch('PIL.Image.open')
def test_populate_signature(open_mock, phash_mock, photo_fixture):
    m = mock.Mock()
    m._getexif.return_value = ''
    open_mock.return_value = m
    phash_mock.return_value = 'image_hash'
    assert photo_fixture._populate_signature() == 'image_hash'


@pytest.mark.skip(reason="To be fixed")
# This test is used only for 100% coverage as both
# _populate methods are covered in other tests
@patch('photopy.photo.Photo._populate_exif_data')
@patch('photopy.photo.Photo._populate_signature')
def test_populate(popsig_mock, popexif_mock, photo_fixture):
    popsig_mock.return_value = 'signature_populated'
    popexif_mock.return_value = 'exif_populated'
    photo_fixture.populate()
    assert photo_fixture.signature == 'signature_populated'
    assert photo_fixture.exif_data == 'exif_populated'
