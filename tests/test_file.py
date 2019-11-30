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
    f = File('/path/to/file')
    return f


def test_init(f):
    assert isinstance(f, File)
    assert f.path == '/path/to/file'


def test_init_with_no_args():
    with pytest.raises(Exception):
        assert File()


def test_init_with_invalid_path():
    with pytest.raises(Exception):
        assert File('/path/to/file')


def test_populate(f):
    f.populate()
    assert f.name == 'name'
    assert f.signature == 'signature'
    assert f.extension == 'ext'
