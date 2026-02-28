```txt
#   ____  ___ _____
#  / ___|/ _ \_   _|
# | |  _| | | || |
# | |_| | |_| || |
#  \____|\___/ |_|
#
```

# Got: Version Control Focused on Simplicity, not Flexibility

Got is a new version control system built on top of git, which is focused on making
git a little more easier to use.

## Setup and config

TBD

## Setup of gotd

1. `mkdir -p /git/myrepo.git`
2. `chmod 700 /git/myrepo.git`
3. # chown _gotd /git/myrepo.git
4. # su -m _gotd -c 'gotadmin init /git/myrepo.git'
5. Add the new repository to gotd.conf(5) granting read-write access to the
6. flan_hacker user account, and restart gotd:
7. # cat >> /etc/gotd.conf <<EOF
8. repository 'myrepo' {
    9. path '/git/myrepo.git'
    10. permit rw flan_hacker
    11. }
    12. EOF
    13. # rcctl restart gotd
    14. # Run as the default user:
    15. user _gotd
    16. # Listen on the default socket:
    17. listen on "/var/run/gotd.sock"
    18. # This repository can be accessed via ssh://user@example.com/src
    19. repository "src" {
        20. path "/var/git/src.git"
        21. permit rw flan_hacker
        22. permit rw :developers
        23. permit ro anonymous
        24. protect branch "main"
        25. protect tag namespace "refs/tags/"
        26. }
        27. # This repository can be accessed via
        28. # ssh://user@example.com/openbsd/ports
        29. repository "openbsd/ports" {
            30. path "/var/git/ports.git"  

