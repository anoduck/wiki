```text
#  ___        __ _            ____  ____
# |_ _|_ __  / _| |_   ___  _|  _ \| __ )
#  | || '_ \| |_| | | | \ \/ / | | |  _ \
#  | || | | |  _| | |_| |>  <| |_| | |_) |
# |___|_| |_|_| |_|\__,_/_/\_\____/|____/
#
```

InfluxDB
========

A NonTraditional database I know nothing about.
-----------------------------------------------

I don't know enough about influxdb to write an introduction, I just know I need a DB to store my data, and
influxdb appears to be the only natively supported option. So we are just going to have to suck it up and
get to the meat of it.

### A note about Influxdb versions

At the time of writing this, there are three separate versions of InfluxDB. All three versions are distinctly
different from one another, and possess different features. Prima Factia, the client appears to vary, and even
the query language appears to vary from version to version. Out of those three, only V.1 and V.2 appear to be
used in open source projects, and V.3 is suspected to be currently closed source. v1 and v2, are open source. 
All of this may prove to be not exactly the situation, but it is important to stress the need to be attentive
to these differences.

In order to gain fuller understanding of the concepts of InfluxDB, it would be wise to facilitate the use of
the [glossary](https://docs.influxdata.com/influxdb/v1/concepts/glossary/).

### Command table

For version one, a reference to the query language may be found [here](https://docs.influxdata.com/influxdb/v1/query_language/spec/)
Below is a table where some of the more routine and basic commands may be referenced.

| Command                                         | Description                        |
| ----------------------------------------------- | ---------------------------------- |
| `SHOW DATABASES`                                | Display the name of all databases  |
| `CREATE DATABASE {$db_name}`                    | Create a database named {$db_name} |
| `CREATE USER {$user} WITH PASSWORD {$password}` | Create user with password          |
| `DROP DATABASE {$db}`                           | Delete database                    |
| `CREATE CONTINUOUS QUERY {$cq_name}` ON {$db}   | Create a continuous query          |

#### Retention policies

Retention policies in InfluxDB declare how long information is stored in the database, which is an interesting
feature. By default, InfluxDB's retention policy is set to `autogen` which means data is retained for
eternity.

```influxdb
CREATE RETENTION POLICY <retention_policy_name> ON <database_name> DURATION <duration> REPLICATION <n> [SHARD DURATION <duration>] [DEFAULT]
```
