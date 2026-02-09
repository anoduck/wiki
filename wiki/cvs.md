```text
#   ______     ______
#  / ___\ \   / / ___|
# | |    \ \ / /\___ \
# | |___  \ V /  ___) |
#  \____|  \_/  |____/
#
```

# CVS: Concurrent Versioning System

CVS is a an older, but widley used version control system created by Dick Grune in 1987. It builds on top of
another, even older, version control system called Revision Control System by adding support for the client
server model and repository level change tracking. It does many fancy things.

## AnonCVS

One of the benefits of CVS during the time of it's creation is it's ability to allow users without an account
(guests) read access privileges to the source tree of the repository. This means any user can access the CVS
server pseudo-anonymously and "check out" a complete copy of all the files there in, while making no changes
to those files on the server. This can be extremely useful in terms of software distribution.

### Check Out and Upgrade

Now, since we primarily deal with CVS in coordination with the ports tree, lets go over how to perform an
initial checkout and upgrade.

#### Performing Initial Check Out

Before working with AnonCVS one must choose which AnonCVS server they will use. We will assume you have
already done so, and for demonstration purposes only, we will say `anoncvs@anoncvs.example.org` is the server
we have chosen.

If you are fetching the ports tree for the first time, you will want to change directory to `/usr`.

``` bash
# For Current.
cvs -q d anoncvs@anoncvs.example.org:/cvs checkout -P ports
# For a Release
cvs -qd anoncvs@anoncvs.example.org:/cvs checkout -rOPENBSD_$RELEASE -P ports
```

#### Updating after fetch

From then on, you should only have to perform maintenance updates via the `/usr/ports` directory.

```bash
# For Current
cvs -q up -Pd -A
# For Release
cvs -q up -Pd -rOPENBSD_$RELEASE
```

Of course, things do not always go as they should, and if the repository becomes stale with time, you will
have to update with the "refreshed" command, which is also the same command you would use if you wanted to
change which server you are pulling updates from.

```bash
# For Current
cvs -d anoncvs@anoncvs.example.org:/cvs -q up -Pd
# For Release
cvs -d anoncvs@anoncvs.example.org:/cvs -q up -Pd -rOPENBSD_$RELEASE
```
