#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `database` module."""

from photopy.database import Database


def test_init():
    d = Database('path/to/database')
    assert d.db_path == 'path/to/database'
