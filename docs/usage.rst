Usage
=====

How it might be used (not implemented yet):

Install init.d scripts::

    $ ameh init jira
    $ ameh init confluence
    $ ameh init all

Display configuration settings::

    $ ameh config
    jira install: /opt/atlassian/jira
    jira home: /var/atlassian/application-data/jira-home
    confluence install: /opt/atlassian/confluence
    confluence home: /var/atlassian/application-data/confluence-home

Display the names of configuration files::

    $ ameh config jira db
    /var/atlassian/application-data/jira-home/dbconfig.xml

    $ ameh config confluence crowd
    /opt/atlassian/confluence/confluence/WEB-INF/classes/crowd.properties

Edit the Jira DB config file::

    $ vim `ameh config jira db`

Create a new configuration setting for Jira's log4j.properties::

    $ ameh config jira log4j /opt/atlassian/jira/atlassian-jira/WEB-INF/classes/log4j.properties

    $ ameh config jira log4j
    /opt/atlassian/jira/atlassian-jira/WEB-INF/classes/log4j.properties

Display the name of the log file for Jira::

    $ ameh log jira
    /opt/atlassian/jira/logs/catalina.out

Tail Jira's log file::

    $ tail -f `ameh log jira`

View Atlassian users and their groups::

    $ ameh user
    jira : jira atlas
    confluence : confluence atlas
    crowd : crowd atlas

Backup Jira (installation and home directories)::

    $ ameh backup jira


