#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `photo` module."""

from photopy.photo import Photo
from unittest.mock import patch


def test_init():
    with patch('os.path.isfile') as isfile_mock:
        isfile_mock.return_value = True
        p = Photo('/path/to/photo')
        assert p.extension == 'ext'
        assert p.signature == 'photo_signature'
        assert p.exif_data == 'photo_exif_data'
