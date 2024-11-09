```text
#  ____        _        _
# |  _ \  __ _| |_ __ _| |__   __ _ ___  ___  ___
# | | | |/ _` | __/ _` | '_ \ / _` / __|/ _ \/ __|
# | |_| | (_| | || (_| | |_) | (_| \__ \  __/\__ \
# |____/ \__,_|\__\__,_|_.__/ \__,_|___/\___||___/
#
```

Databases
==========

I brought the base.
-------------------

Databases are programs specifically written to store, catalog, and manage data. They can be pointlessly small
in size from less than a handful of entries to absurdly magnanimous consisting of millions upon millions of
entries. Databases in computing encompass two forms of databases, the traditional relational database
which incorporates the SQL query language, and the untraditional Non-SQL variant. The study of databases is a
discipline of computer science in it's own right, and is possesses great depth.

### Traditional Databases

Some of the more historical databases systems you might encounter would include IBM's DB2 and Berkley's
Database System, but they are more rare in occurrence. More popular implementations of a traditional database
would include MySQL/MariaDB, PostgreSQL, and SQLite. Oracle is still very popular, but not nearly as common as the
previous three. MySQL was the most popular SQL database on the market for sometime, until several of the
original developers forked it out of concerns it would become closed source and created MariaDB. Just to clarify,
MariaDB is the new standard, where mysql is yesterday's lunch.

Since most databases take advantage of the SQL specification, this means those databases can be managed and
queried using the same syntax.

| [MariaDB](mariadb) | [PostgreSQL](postgres) |

### NonTraditional Databases

One of the more irritating things about modern computing is it's tendency to be utterly faddish and completely
engrossed in zietgeist. Unfortunately, due to the modern rise in popularity of NonTraditional Databases, the
frequency of which one might encounter one of the many NonTraditional Databases suffers from this affliction
of fad obsession. (Worded awkwardly, and redundant.) As of the time this was currently written, Redis and
MongoDB were beginning to tedder in popularity, where InfluxDB was rising. 

| [InfluxDB](influxdb) | [MongoDB](mongodb) | [Victoria Metrics](victoria_metrics) |


