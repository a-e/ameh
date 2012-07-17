import os
from ConfigParser import ConfigParser
from exceptions import MissingConfig, UnknownApplication

class Config:
    def __init__(self, filename='/etc/ameh.ini'):
        if not os.path.isfile(filename):
            raise MissingConfig("Config file not found: '%s'" % filename)

        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename)

    def apps(self):
        """Return a list of app names defined in the configuration.
        """
        return self.config.sections()

    def check_app(self, app):
        """Raise UnknownApplication if the given app is not configured.
        """
        if app in self.apps():
            return True
        else:
            raise UnknownApplication(
                "Application '%s' not defined in '%s'" % (app, self.filename))

    def property(self, app, prop):
        """Return the given property configured for an application.
        """
        self.check_app(app)
        return self.config.get(app, prop)

    def defaults(self, app):
        """Return all default properties for a given application.
        """
        return {
            'app': app,
            'user': app,
            'install': '/opt/atlassian/%s' % app,
            'home': '/var/atlassian/application-data/%s-home' % app,
        }

    def properties_dict(self, app):
        """Return a dict of all properties for the given application,
        including all default properties.
        """
        self.check_app(app)
        props = self.defaults(app)
        props.update(dict(self.config.items(app)))
        return props

    def properties_string(self, app):
        """Return a string of all properties for the given application,
        including all default properties.
        """
        props = self.properties_dict(app)
        prop_lines = [
            "%s %s: %s" % (app, prop, value)
            for (prop, value) in props.items()
        ]
        return '\n'.join(prop_lines)

