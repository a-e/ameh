Ideas
-----

Some tools that it might be worthwhile to include:

- init.d scripts, autogenerated based on configured install/home directories
- Backup scripts
- Symlinking scripts, making configuration files and logs easier to manage by
  having them all in one place (preferably somewhere standard like ``/etc`` and
  ``/var/log``)
- User/group maintainer to prevent multiple jira1, jira2 users from being
  created, and to run each service as a dedicated user

Will probably need:

- A single configuration file to define which Atlassian products you have
  installed, where their install/home directories are, what database backend
  you're using, etc.
- A nice wrapper executable that can be installed system-wide



