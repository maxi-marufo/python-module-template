from __future__ import print_function

# Python dependencies:
from builtins import str
from builtins import object
import os
import logging
import inspect

# PIP dependencies:
import pbr.version
from nose.plugins.attrib import attr

from src.module import module


FORMAT = '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s'
logging.basicConfig(format=FORMAT, level = logging.INFO)

class testModule(object):

    # Directorio a lee/escribir para test
    dir_path = os.path.dirname(os.path.realpath(__file__))
    version = pbr.version.VersionInfo("module").version_string()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def aux_function(self):
        return

    @attr(attr='1')
    @attr('tag_a')
    def test_a(self):
        module.someMethod()
        pass

    @attr(attr='2')
    @attr('tag_b')
    def test_b(self):
        module.otherMethod()
        pass
