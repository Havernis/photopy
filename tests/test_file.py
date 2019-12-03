#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `file` module
    class File:
            name
            path
            extension
            signature
"""
import pytest
from photopy.file import File
from unittest.mock import patch


@pytest.fixture
@patch('os.path.isfile')
def f(isfile_mock):
    isfile_mock.return_value = True
    f = File('/path/to/file_name.txt')
    return f


def test_init(f):
    assert isinstance(f, File)
    assert f.path == '/path/to/file_name.txt'


def test_init_with_no_args():
    with pytest.raises(Exception):
        assert File()


def test_init_with_invalid_path():
    with pytest.raises(Exception):
        assert File('/path/to/file_name.txt')


# This test is used only for 100% coverage as both
# _populate methods are covered in other tests
def test_populate(f):
    f.populate()
    assert f.name == 'file_name'
    assert f.signature == 'signature'
    assert f.extension == 'txt'


def test_populate_name(f):
    assert f._populate_name() == 'file_name'


def test_populate_signature(f):
    assert f._populate_signature() == 'signature'


def test_populate_extension(f):
    assert f._populate_extension() == 'txt'
