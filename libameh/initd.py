"""init.d script generator
"""

import string
from exceptions import UnknownProperty

# This template can include any ``$property`` defined in ameh.ini
_template = """#!/bin/sh -e
# /etc/init.d/$app

# [runlevels] [start order] [stop order]
# chkconfig: 2345 80 20
# description: $app

APP="$app"
USER="$user"
START="$start"
STOP="$stop"

case "$$1" in
    start)
        echo "Starting $$APP"
        /bin/su -m $$USER -c "$$START &> /dev/null"
        ;;
    stop)
        echo "Stopping $$APP"
        /bin/su -m $$USER -c "$$STOP &> /dev/null"
        ;;
    restart)
        $$0 stop
        sleep 5
        $$0 start
        ;;
    *)
        echo "Usage: $$0 {start|restart|stop}"
        exit 1
        ;;
esac
"""
template = string.Template(_template)

def generate(app, config):
    """Generate and return an init.d script for the given app.
    """
    props = config.properties_dict(app)

    try:
        script = template.substitute(props)
    except KeyError, prop:
        raise UnknownProperty(
            "Missing %s property for application '%s'" % (prop, app))
    else:
        return script

