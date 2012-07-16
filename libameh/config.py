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
        if app not in self.apps():
            raise UnknownApplication(
                "Application '%s' not defined in '%s'" % (app, self.filename))

    def show_app(self, app):
        """Print out properties for the given application.
        """
        if app == 'all':
            show_apps = self.apps()
        else:
            self.check_app(app)
            show_apps = [app]

        for app in show_apps:
            for prop, value in self.config.items(app):
                print("%s %s: %s" % (app, prop, value))

    def show_prop(self, app, prop):
        """Print out the value of a single property for the given application.
        """
        self.check_app(app)
        print(self.config.get(app, prop))


    def property(self, app, prop):
        """Return the given property configured for an application.
        """
        self.check_app(app)
        return self.config.get(app, prop)

