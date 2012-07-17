Usage
=====

The main way to use ameh is through the command-line script ``ameh``, which
includes several subcommands for doing various tasks. Run ``ameh`` with no
arguments to get help, or ``ameh <command>`` with no arguments to get help on a
particular command.


Permissions
-----------

All ameh commands are designed to be run as a normal user, without requiring
root access. It's recommended that you use ``sudo`` only when you actually need
elevated permissions for something.


init
----

Atlassian products tend not to include ``/etc/init.d`` scripts for starting,
stopping, or checking the status of your applications. The ``init`` command
aims to remedy this by providing an init-script generator::

    $ ameh init jira

    #!/bin/sh -e
    # /etc/init.d/jira

    # [runlevels] [start order] [stop order]
    # chkconfig: 2345 80 20
    # description: jira

    APP="jira"
    USER="jira"
    START="/opt/atlassian/jira/bin/startup.sh"
    STOP="/opt/atlassian/jira/bin/shutdown.sh"

    case "$1" in
        start)
            echo "Starting $APP"
            /bin/su -m $USER -c "$START &> /dev/null"
            ;;
        stop)
            echo "Stopping $APP"
            /bin/su -m $USER -c "$STOP &> /dev/null"
            ;;
        restart)
            $0 stop
            sleep 5
            $0 start
            ;;
        *)
            echo "Usage: $0 {start|restart|stop}"
            exit 1
            ;;
    esac

This command simply generates an init-script based on the settings you have
configured in ``/etc/ameh.ini``, and prints it on standard output. This way
you, being a responsible sysadmin, can review everything it does before
installing it into your ``/etc/init.d`` folder. To do that, you can pipe into a
``tee`` command with elevated permissions::

    $ ameh init jira | sudo tee /etc/init.d/jira

You may need to customize the resulting script for your particular environment,
but this will at least give you a starting point.


config
------

Jira, Confluence, and other Atlassian products have configuration files
scattered all over the place. It can be tedious trying to remember where each
one is. The ``config`` command can help you keep track of them.

When you run ``ameh config <app>``, all of the properties defined in the
``[app]`` section of your ``/etc/ameh.ini`` file are printed. For example, you
might get something like::

    $ ameh config jira
    jira install: /opt/atlassian/jira
    jira start: /opt/atlassian/jira/bin/startup.sh
    jira stop: /opt/atlassian/jira/bin/shutdown.sh
    jira home: /var/atlassian/application-data/jira-home
    jira classes: /opt/atlassian/jira/atlassian-jira/WEB-INF/classes
    jira db: /var/atlassian/application-data/jira-home/dbconfig.xml

Some of these are configuration files, and others are directories or shell
scripts. If it's configured, it's printed here. Let's say you want to modify your database configuration, and you don't remember which file that's in::

    $ ameh config jira db
    /var/atlassian/application-data/jira-home/dbconfig.xml

To edit this file, you can simply surround that command in backticks::

    $ vim `ameh config jira db`

Or, if you need elevated permissions::

    $ sudo vim `ameh config jira db`


