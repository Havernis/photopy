#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `scan` module."""


import pytest
from photopy.scan import Scan


@pytest.fixture
def s():
    return Scan('path/to/album', 'path/to/db', {})


def test_init(s):
    assert isinstance(s, Scan)
    assert s.album_path == 'path/to/album'
    assert s.db_path == 'path/to/db'
    assert s.db_records == {}


def test_scan(s):
    dictionary = s.scan()
    assert isinstance(dictionary, dict)
