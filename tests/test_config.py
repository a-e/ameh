import os
import unittest
import libameh
from . import data_dir

class TestConfig (unittest.TestCase):
    def setUp(self):
        self.ini_file = os.path.join(data_dir, 'test.ini')
        self.config = libameh.config.Config(self.ini_file)

    def test_init(self):
        conf = libameh.config.Config(self.ini_file)
        self.assertEqual(conf.filename, self.ini_file)

    def test_init_missing_config(self):
        self.assertRaises(libameh.exceptions.MissingConfig,
                          libameh.config.Config, 'bogus.ini')

    def test_apps(self):
        self.assertEqual(self.config.apps(), ['jira', 'confluence'])

    def test_check_app(self):
        self.assertTrue(self.config.check_app('jira'))
        self.assertTrue(self.config.check_app('confluence'))

    def test_check_app_unknown_app(self):
        self.assertRaises(libameh.exceptions.UnknownApplication,
                          self.config.check_app, 'bogus')

    def test_properties_string(self):
        props = self.config.properties_string('jira')
        self.assertIn('jira home', props)
        self.assertIn('jira install', props)

    def test_properties_string_unknown_app(self):
        self.assertRaises(libameh.exceptions.UnknownApplication,
                          self.config.properties_string, 'bogus')

    def test_property(self):
        self.assertEqual(self.config.property('jira', 'install'),
                         '/opt/atlassian/jira')

    def test_property_unknown_app(self):
        self.assertRaises(libameh.exceptions.UnknownApplication,
                          self.config.property, 'bogus', 'install')

    def test_defaults(self):
        self.assertEqual(self.config.defaults('jira'), {
            'app': 'jira',
            'user': 'jira',
            'install': '/opt/atlassian/jira',
            'home': '/var/atlassian/application-data/jira-home',
        })

    def test_properties_dict(self):
        props = self.config.properties_dict('jira')
        self.assertIn('home', props)
        self.assertIn('install', props)

    def test_properties_dict_unknown_app(self):
        self.assertRaises(libameh.exceptions.UnknownApplication,
                          self.config.properties_dict, 'bogus')

