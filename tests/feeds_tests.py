"""
Unit tests for feeds reading and parsing.
"""

import logging
import os
import sys

from unittest.mock import patch

from trafilatura import cli, feeds


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
RESOURCES_DIR = os.path.join(TEST_DIR, 'resources')



def test_atom_extraction():
    '''Test link extraction from an Atom feed'''
    filepath = os.path.join(RESOURCES_DIR, 'feed1.atom')
    with open(filepath) as f:
        teststring = f.read()
    assert len(feeds.extract_links(teststring)) > 0


def test_rss_extraction():
    '''Test link extraction from a RSS feed'''
    filepath = os.path.join(RESOURCES_DIR, 'feed2.rss')
    with open(filepath) as f:
        teststring = f.read()
    assert len(feeds.extract_links(teststring)) > 0


def test_feeds_helpers():
    '''Test helper functions for feed extraction'''
    assert feeds.validate_url('http://example.org/article1/') is True
    assert feeds.validate_url('') is False
    assert feeds.validate_url('http://example.org/') is False


def test_cli_behavior():
    '''Test command-line interface with respect to feeds'''
    testargs = ['', '--list', '--feed', 'https://httpbin.org/xml']
    with patch.object(sys, 'argv', testargs):
        assert cli.main() is None


if __name__ == '__main__':
   test_atom_extraction()
   test_rss_extraction()
   test_feeds_helpers()
   test_cli_behavior()