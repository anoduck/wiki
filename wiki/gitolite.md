```text
#   ____ ___ _____ ___  _     ___ _____ _____
#  / ___|_ _|_   _/ _ \| |   |_ _|_   _| ____|
# | |  _ | |  | || | | | |    | |  | | |  _|
# | |_| || |  | || |_| | |___ | |  | | | |___
#  \____|___| |_| \___/|_____|___| |_| |_____|
#
```

# Gitolite: There is nothing "lite" or "light" about it.

Gitolite is a public git repository server, although that is probably not what the official service designation is stated as,
but it is close enough. Gitolite allows users to host their own publicly accessible git repository on their
server, and it supports every protocol git supports. Although, it does not provide a frontend web interface,
you will have to use other packages for that. 

## Setup

No lie here, bro. If you got Linux, gitolite is pretty damn easy. If you are running OpenBSD, like some people
we all know (cough, cough...Me), then it will constantly be a pain in the ass. 

So, why is Gitolite configuration so difficult in OpenBSD? Permissions. OpenBSD is designed with a vary rigid
permissions system. It is this very rigid, and highly secure, permission system that makes a hell of a lot of
trouble.

### General install and configuration

Keep in mind:

* Server = Remote
* Desktop = Local

1. Begin by ssh-ing into your Server
2. Create the system user and group "git".
3. Install the gitolite package from the distro repository.
4. If your local machine does not have an ssh-key generated yet, generate one.
5. Upload the ssh key from your local machine to the server's /tmp directory.
6. Make sure the git user can access and modify it.
7. ssh back into your remote server.
8. Become the "git" user. `su - git`
9. change directory to `/tmp`
10. Run the install script. `gitolite setup -pk $YOUR_SSH_KEY.pub`
11. Follow the messages.

### Special care for OpenBSD hosts

If you want to use gitolite in conjunction with cgit, then you will need to place the gitolite repository
where your webserver can access it to. 

