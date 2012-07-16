Configuration
=============

ameh stores its configuration in a file like this::

    [jira]
    install = /opt/atlassian/jira
    home = /var/atlassian/application-data/jira-home
    classes = %(install)s/atlassian-jira/WEB-INF/classes
    crowd = %(classes)s/crowd.properties
    db = %(home)s/dbconfig.xml

    [confluence]
    install = /opt/atlassian/confluence
    home = /var/atlassian/application-data/confluence-home
    db = %(home)s/confluence.cfg.xml

    # Any apps you don't use will have their sections commented out
    #[crowd]
    #[fisheye]

New configuration settings can be added using the ``ameh`` command-line, or by
directly editing the configuration file (which will typically live in
``/etc/ameh.ini``).



