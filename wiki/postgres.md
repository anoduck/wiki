```text
                                    ..::::.                                                                                                                     
         :=+*****+++=-:.-+******++*##*****###*=:                                                                                                                
       +%#+=-------==+*#*=--:::---. .---:::::-+##+.                                                                                                             
     :%#:.:=++***++==-  :=+*****++=-::-*##**+=:.:*%=                                                                                                            
    .@* -*##*******#+.-*##********##*+:.-*****#*= :@+                                                                                                           
    #@ -#**********+ -#***************#+: +#****#* +@                                                                                                           
    @+ ************ :#******************#- =****** -@                                                                                                           
   .@-.**********#= *#****#***********#***- +***** =%                                                                                                           
    @= **********#: =:::::-***********-.:.: :****+ #+                                                                                                           
    %* +**********. :=+=.:..*********..=:-*.:#**#:.@.                                                                .---=---:      :-===--:.    ::             
    =@ -#*********:.##**=++ =#******* -#+*+ =#**+ **     -=--====:                                                  -*-.  ..:++.  -+=:.  .:-++.  *+             
     @- *********#:.******* :#******#- ***+ =***.:@      #*..::::#+                    =.                           *=        +- ++.         -*: +=             
     +% =********#..*******.:#********..*** -*#- @-      #+      :@. .::-:.   .:---.  :%+:. .::-: :   .--. .::::    -*-:..      -#            =* +=             
     .@:.********* :#****** -#********* :#* :#= #+       #*:::::-#= ++-::-*- =*:..:*= -#+::*=:::-+% =%=--.+=:..-*:   .--=====-: =*            :*.+=             
      +% =#*******..#****#: ***********+ :* -+ *#        ##----=-. +*     .%.-*-::.:.  #: *+     :% =#   +#::::.=#  .     ..:-*--*.           -* +=             
       %= ********+ -##*#= +************+ ..- +*         #+        +*     .%....::-+*  #- *+     -% =*   **.....:- :#:        -#.++          .*- +=             
       :@.:#******#*  :=+ :***************.  *@::-=+-    #*        .*=:.:-*= ++....=*  *+:.++-:-=+% =*   .*-...-*-  =*-..    :*=  =+-...   :=*:  *+.........    
        +% -#****#*:.+*=  :.-************-::.--==:.=@:   ..          :---:.   :----:    ::.-..:. -# ..     :---:     :-======-.    .-=======-=+: -=------=--    
         *# :*##*- -##*=.=#= +**********= -++--:. -#+                                      *+--:-+:                                           ..                
          +%:.--.:*: .:-+=:  =*********#- ----=+*##-                                         ..:.                                                               
           -#*+++*@*==----+* =*********#::@====-:.                                                                                                              
             .:-.  :--===-*% =********** =#                                                                                                                     
                          =@ =*********+ #+                                                                                                                     
                          -@ -#*******#= %-                                                                                                                     
                          :@.:#*******#.:@.                                                                                                                     
                           @* =#####**: %+                                                                                                                      
                           -@+.:----::=%+                                                                                                                       
                            :*#*++++**=.                                                                                                                        
                               .:::. 
```

Postgresql
-----------

> The most technologically advanced relational database ever created.

Postgresql is one of the many "traditional" databases available on the market, it was the second most popular
database, and by coincidence it was written by the same programmers who created both MySQL and MariaDB.
Although configuration of Postgresql is different than MySQL/MariaDB, it accepts nearly the exact same syntax
as MySQL/MariaDB, but it is slightly more resource heavy than the other two.

For a while there, installation and configuration of Postgresql was a breeze up until a few years ago. It was
then when the Postgresql took on a new design objective, and this was to target database clusters. In order to
target these large database clusters Postgresql has to implement strict version adherence and database
isolation. The benefit to this strategy is it allowed large scale database systems of 100 or more database
servers to run and manage several different versions of Postgresql at one time, the drawback is it created
previously nonexistent obstacles for systems administrators to go through in order to upgrade their database
from one version to the next. As one can guess, these new obstacles resulted in Postgresql becoming less commonly
encountered outside a corporate or academic environment.

### Installation

Installation can be easily achieved through the use of the whatever distrobution package manager your system
uses, but after the initial install things will increase in initial complication. 

For the remainder of this page, we will assume the user is using a Debian or Arch derivative system. This is mentioned
as a precaution, because although other linux systems might be identically structured, the following
information isn't precise for those systems, and should be treated as a mere estimation.

### Post Installation

Simply installing the database software will not get you anywhare close to owning a working database, in fact,
your not even halfway. There are several steps that need to be performed before you even worry about enabling
it and starting it up. The first of which is understanding how postgresql directories are structured.

#### PostgreSQL Directory structuring

Your next step is to discover what version of Postgresql you are using. You can easily discover this by
running `sudo pg_config --version` and this should output a string like this `PostgreSQL 16.3 (Debian 16.3-1+b1)`,
which clearly says our version is "16.3". Below is a means to acquire only the major release number of your
PostgreSQL installation.

```awk
sudo pg_config --version | awk -F " " '{n = split($2, num, "."); print num[1]}'
```

Remember when we said that PostgreSQL is now aiming it's architecture toward high available large
installations? Well, that is the reason why the above is important, because inside ever "postgresql"
directories on your system you will find a set of subdirectories, each one labeled with the major release
version. You will need to know this version in order to use the correctory directory for your installation.

Several of PostgreSQL's directories take this a bit further, these are primarily those directories that would
require further distinction if environments where there are numerous versions and/or numerous instances of the
same version. As you will see below, during initialization of the database you will be asked to provide a name
for the instance you are initializing. It is this name that will be used to create another subdirectory which
will store file specific to one particular instance. 

So, in summary, some directories will use `postgres/VERSION`, while others will use
`/postgresql/VERSION/INSTANCE`.

#### Enabling and starting PostgreSQL in SystemdD

Recently great difficulties were encounted while attempting to start PostgreSQL with systemd, so to avoid
encountering these difficulties yourself, here is how to start prepare PostgreSQL to start.

##### As Usual, initialize the database

To initialize the database, you will need to become the user postgres and run the initdb command from the
pgctl command, and provide your specific instance. 

```bash
sudo -u postgres bash
pgctl initdb $NAME
```

If for some reason, the above command does not work for you, then you could try the following. 

```bash
sudo -u postgres /usr/lib/postgresql/16/bin/pgctl initdb
```

##### Ensure ssl-snakeoil.pem has proper permissions.

For some reason or another, the ssl snakeoil file did not have the correct permissions to allow PostgreSQL to
connect to it. Interestingly, the user `postgres` was already a member of the `ssl-cert` group, but the
permissions on the ssl snakeoil file were set to only allow root access. 

1. Check to see if the file has the correct permissions: `sudo stat /etc/openssl/path/to/snakeoil/file`
2. If it says `0600`, you need to change it, but if it says `0640`, skip the next step.
3. So, to give the file the correct permissions run: `sudo chmod 0640 /etc/openssl/path/to/snakeoil/file`

##### Enable the service and start it

__DON'T SKIP ME! READ__

This is important, in order to enable and start YOUR VERSION of PostgreSQL, you must enable and start the
OVERALL PostgreSQL service.

```bash
sudo systemctl enable postgresql.server
sudo systemctl start postgresql.service
# AND THEN
sudo systemctl enable postgresql@16.service
sudo systemctl start postgresql@16.service
```

Obviously you would want to replce "16" with whatever version of PostgreSQL you are running.

#### Install pgcli

Several years ago the python program "mycli" was discovered, and we immediately became a big fan of the
project. A year after "mycli" was discovered the same team of developers released "pgcli", which is the
PostgreSQL variation of the "mycli" client, and instantaneously we were a fan of it as well. So, we highly
recommend it. Pgcli provides command history, statement completion, minor autocorrection, and much more
features.

Pgcli can be installed from most distrobution package management systems, which is the recommended means to
install it.

### Configuration

Now that you have it installed, you still need to configure a few things to make it feasibly usable. All of
which can be done inside the PostgreSQL configuration directory, whichis located in `/etc/postgresql/`
under the directory with the same name as your major release version. So, for example:
`/etc/postgresql/16/` would be correct if your release version is 16.

#### Ensure correct port number

Open up the configuration file, `postgresql.conf` and make sure the port PostgreSQL is set to listen on 
is `5432`. This is important even if you plan on using only the filesystem socket, because the port number
is included as part of the name for the socket.

#### Secure your installation

Next you will need to restrict access to the database superuser to secure your installation. This is done
by editing the directory in `/var/lib/postgres/data/` and then in that directory you will need to follow the
schema mentioned above. Mainly, the major release followed by the name of your instance. Inside of that,
there will be a file named `pg_hba.conf`. Don't ask me what it's name stands for, because I have never known
nor needed to know.

You will need to change one word in that file, which is from `trust` to `peer`. Below is the original line to
look for, followed by what the same line should look like after you have made your alteration. Afterwards, if
you have already started the PostgreSQL service, you will need to restart it.

```conf
# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     trust
```

__TO:__

```conf
# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             postgres                                peer
```

#### Enable the Trigram Extension

If you ever see an error stating `operator class "gin_trgm_ops" does not exist for
access method "gin" (SQLSTATE 42704) handling 005_assets_indexes.sql`, then your database requires you to
enable the trigram extension. This can only be done on a per database case, which means if you have more than
one database that require the trigram extension, you will have to enable it for each database that requires
it. To do this, you will need to use the postgresql database shell, and connect to the database that requires
it. Once connected simply type `CREATE EXTENSION pg_trgm;` at the prompt, hit enter to execute the statement,
and exit the subshell with `exit;`. You will need to restart your postgresql server in order for postgresql to
load the extension. The steps to performing this will be shown below.

```bash
# Become the postgres user
sudo -u postgres pgcli
# Connect to the database in question.
USE <$DATABASE>
# Enable the extension
CREATE EXTENSION pg_trgm;
# Exit the shell
EXIT;
# Restart the database
sudo systemctl restart postgresql@16.main.service
```

### Basic Commands

__Via Command Line__

1. To Create a User: `createuser --interfactive "<$USER>"`
2. To Create a DB: `createdb <$DATABASE>`

__Via Postgresql Shell__

Please keep in mind all "formal" sql statements end with a ";".

| Function              | command                          |
| --------              | -------                          |
| `\l`                  | List all databases               |
| `\c $DB`              | Connect to database "$DB"        |
| `\dt`                 | List all tables in all databases |
| `\d`                  | Show database details            |
| `CREATE DATABASE $DB` | Create database named "$DB"      |
| `DROP DATABASE $DB`   | Delete database named "$DB"      |

#### Resetting postgres password

So lets say you lost your password to the postgresql user postgres (which is root user for postgresql), and you cannot recover it. But, the database is still good and you just need to reset it. Well, your in luck. Because your not the first to do this, and you won't be the last. There is a simple process to change things as long as you still root access to the machine running the DB.

1. Simply open up the file `pg_hba.conf` and modify it to where a passwordless login is used for user postgres as long as it is not remote. Do this by changing the bottom line.

From:
<code>
local  all  postgres
</code>
To:
<code>
local  all  postgres		trust sameuser
</code>

2. After this is completed you can log into psql without a password
<code>
psql -U postgres
</code>

3. After that simply change the password with the following:
<code>
ALTER USER postgres with password '$yourpassword$'
</code>

4. You should be good to go at this point. When your ready to use a
password again. simply remove trust from pg_hba.conf and replace it
with md5. Restart and you are ready to move again.

### References

- https://learnsql.com/blog/postgresql-cheat-sheet/
- https://wiki.archlinux.org/title/PostgreSQL
