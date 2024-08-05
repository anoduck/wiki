```text
#  __  __            _       ____  ____
# |  \/  | __ _ _ __(_) __ _|  _ \| __ )
# | |\/| |/ _` | '__| |/ _` | | | |  _ \
# | |  | | (_| | |  | | (_| | |_| | |_) |
# |_|  |_|\__,_|_|  |_|\__,_|____/|____/
#
```

Maria Database
---------------

MariaDB is a fork of mysql created by the original developers of mysql. They were concerned over the future
direction mysql was being taken since it was not fully open source and owned by a corporate entity. MariaDB is
fully compatible with mysql, and can be used as a dropin replacement for it. MariaDB does include several
performance enhancements over mysql, which makes it superior for use.

### Basic MariaDB SQL syntax

Since MariaDB is a traditional SQL language compliant database, it's syntax shadows other SQL compliant
databases, and should feel intuitive.

1. Show Databases: `SHOW DATABASES`
2. Create a Database: `CREATE DATABASE <%NAME> CHARACTER SET utf8`
3. Delete Database: `DROP DATABASE <%NAME>`

#### Basic Database Setup

Below are the set of commands performed to setup a mariadb instance up for use. More recently, the application
using MariaDB will do this automatically, but it is still important to know how. 

```SQL
CREATE DATABASE %name CHARACTER SET utf8;
# The single quotes are important here, so is the ";".
CREATE USER '%username'@'localhost' IDENTIFIED BY '%password';
SET PASSWORD FOR '%user'@'localhost' = PASSWORD('%password');
GRANT SELECT, INSERT, DELETE ON %name TO '%user'@'localhost' IDENTIFIED BY '%password';
```

