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
def file_fixture(isfile_mock):
    isfile_mock.return_value = True
    return File('/path/to/file_name.txt')


def test_init(file_fixture):
    assert isinstance(file_fixture, File)
    assert file_fixture.path == '/path/to/file_name.txt'


def test_init_with_no_args():
    with pytest.raises(Exception):
        assert File()


@patch('os.path.isfile')
def test_init_with_invalid_path(isfile_mock):
    isfile_mock.return_value = False
    with pytest.raises(Exception):
        assert File('/path/to/file_name.txt')


@pytest.mark.skip(reason="To be fixed")
# This test is used only for 100% coverage as both
# _populate methods are covered in other tests
def test_populate(file_fixture):
    file_fixture.populate()
    assert file_fixture.name == 'file_name'
    assert file_fixture.signature == 'signature'
    assert file_fixture.extension == 'txt'


@pytest.mark.skip(reason="To be fixed, name was removed!")
def test_populate_name(file_fixture):
    assert file_fixture._populate_name() == 'file_name'


@pytest.mark.skip(reason="To be fixed")
def test_populate_signature(file_fixture):
    assert file_fixture._populate_signature() == 'signature'


@pytest.mark.skip(reason="To be fixed")
def test_populate_extension(file_fixture):
    assert file_fixture._populate_extension() == 'txt'
