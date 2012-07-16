"""init.d script generator
"""

import string

_template = """
#!/bin/sh -e

# [runlevels] [start order] [stop order]
# chkconfig: 2345 80 20
# description: $app_cap

# Application name
APP="$app_cap"
# User to run as
USER="$user"
# Application directory
APP_DIR="$app_dir"
# Start/stop scripts, relative to APP_DIR
START_SH="bin/startup.sh"
STOP_SH="bin/shutdown.sh"

case "$$1" in
    start)
        echo "Starting $$APP"
        /bin/su -m $$USER -c "$$APP_DIR/$$START_SH &> /dev/null"
        ;;
    stop)
        echo "Stopping $$APP"
        /bin/su -m $$USER -c "$$APP_DIR/$$STOP_SH &> /dev/null"
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

import config

def generate(app):
    """Generate and return an init.d script for the given app.
    """
    conf = config.Config()
    print(conf.config.items(app))
    mapping = {
        'app': app,
        'app_cap': app.capitalize(),
        'user': app,
        'app_dir': conf.property(app, 'install'),
    }
    return template.substitute(mapping)

