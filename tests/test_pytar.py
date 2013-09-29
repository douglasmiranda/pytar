#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pytar
----------------------------------

Tests for `pytar` module.
"""

import unittest
import os

from pytar import pytar

from utils import abspath, CURRENT_DIR


def clean_extracted_files():
    os.remove(abspath('tarfiles/hi.txt'))
    os.remove(abspath('tarfiles/tar.png'))


class TestPytar(unittest.TestCase):
    def test_should_extract_a_normal_tar_file(self):
        tar_file = abspath('tarfiles/files.tar')
        result = pytar.pytar_extract(tar_file)
        self.assertEqual('success', result['status'])
        self.addCleanup(clean_extracted_files)

    def test_should_not_extract_a_corrupted_tar_file(self):
        tar_file = abspath('tarfiles/corrupted-tar-file.tar')
        result = pytar.pytar_extract(tar_file)
        self.assertEqual('fail', result['status'])

    def test_should_not_extract_a_directory(self):
        result = pytar.pytar_extract(CURRENT_DIR)
        self.assertEqual('fail', result['status'])

    def test_should_not_extract_an_inexistent_path(self):
        inexistent_tar_file = abspath('tarfiles/inexistent-tar-file.tar')
        result = pytar.pytar_extract(inexistent_tar_file)
        self.assertEqual('fail', result['status'])


if __name__ == '__main__':
    unittest.main()
