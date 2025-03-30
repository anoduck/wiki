```text
# __     ___      _             _         __  __      _        _
# \ \   / (_) ___| |_ ___  _ __(_) __ _  |  \/  | ___| |_ _ __(_) ___ ___
#  \ \ / /| |/ __| __/ _ \| '__| |/ _` | | |\/| |/ _ \ __| '__| |/ __/ __|
#   \ V / | | (__| || (_) | |  | | (_| | | |  | |  __/ |_| |  | | (__\__ \
#    \_/  |_|\___|\__\___/|_|  |_|\__,_| |_|  |_|\___|\__|_|  |_|\___|___/
```

Victoria Metrics
----------------

Technically speaking, Victoria Metrics is more like a message logger than a database, but since there is no
"message logger/TSDB" section, it will go here.

It is part of an even newer breed of nontraditional databases focused around storing time series data. You
might ask, 'What is time series data?', and that would be a good question. Time series data is basically
program output that involve a time stamp or a series of time stamps. The entirety of an entry in a time series
would make up less than 80 characters. The best example of this is a temperature gauge, which will output the
time and temperature at the time of output. Victoria Metrics along with influxdb, and prometheus focuses on
providing data storage methods for services in "the internet of things". We will not pause to explain what that
is at the moment, so if unfamiliar, your are just going to have to look that one up. 

### Victoria Metric's Metrics QL

The query language for Victoria Metrics is Metrics QL, which is backwards compatible with and inspired by
PromQL, so basically it is a modified version of PromQL. Therefore, if you are familiar with PromQL, you are
in good shape, but if you are like the remainder of humanity, you are in rough waters. This is because PromQL
is a completely different breed to anything else that has come before. Not only is it not a follower of
traditional standardized query languages, it is not a follower of any of thher non-standardized query
languages. Which makes it unique all to it's own, and a pain in the ass due to having to start from the
beginning in order to learn a new query language for a handful of applications.

The developers of Victoria Metrics recommend user checkout [this blog entry](https://valyala.medium.com/promql-tutorial-for-beginners-9ab455142085) for
an introduction to promql, and recommend the user then familiarize themselves with [Victoria Metric's QL here.](https://docs.victoriametrics.com/keyconcepts/#metricsql)

* [Cheat Sheet provided by jitendra-1217](promql-chtsh)

### Misc References

- https://docs.victoriametrics.com/single-server-victoriametrics/?highlight=telegraf#how-to-send-data-from-influxdb-compatible-agents-such-as-telegraf
- https://github.com/gistart/prometheus-push-client
- https://docs.victoriametrics.com/scrape_config_examples/
- https://docs.victoriametrics.com/#how-to-scrape-prometheus-exporters-such-as-node-exporter
- https://docs.victoriametrics.com/vmagent/
- https://triq.org/rtl_433/INTEGRATION.html#influxdb
- https://github.com/merbanan/rtl_433/blob/master/examples/rtl_433_prometheus_relay.py
- https://github.com/AlbertWeichselbraun/sensoric
- https://github.com/robusta-dev/prometrix
- https://pypi.org/project/atro-victoria/ <-- No documentation :(

