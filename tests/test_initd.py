import os
import unittest
import libameh
from . import data_dir

class TestInitd (unittest.TestCase):
    def setUp(self):
        self.ini_file = os.path.join(data_dir, 'complete.ini')
        self.config = libameh.config.Config(self.ini_file)

    def test_generate(self):
        complete_ini = os.path.join(data_dir, 'complete.ini')
        config = libameh.config.Config(complete_ini)
        result = libameh.initd.generate('jira', config)
        for prop in ['start', 'stop']:
            self.assertIn(config.property('jira', prop), result)

    def test_generate_unknown_property(self):
        incomplete_ini = os.path.join(data_dir, 'incomplete.ini')
        config = libameh.config.Config(incomplete_ini)
        self.assertRaises(libameh.exceptions.UnknownProperty,
                          libameh.initd.generate, 'jira', config)

