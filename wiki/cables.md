``` text
#   ____      _     _                             _
#  / ___|__ _| |__ | | ___  ___    __ _ _ __   __| |
# | |   / _` | '_ \| |/ _ \/ __|  / _` | '_ \ / _` |
# | |__| (_| | |_) | |  __/\__ \ | (_| | | | | (_| |
#  \____\__,_|_.__/|_|\___||___/  \__,_|_| |_|\__,_|
#
#   ____      _     _ _
#  / ___|__ _| |__ | (_)_ __   __ _
# | |   / _` | '_ \| | | '_ \ / _` |
# | |__| (_| | |_) | | | | | | (_| |
#  \____\__,_|_.__/|_|_|_| |_|\__, |
#                             |___/
#
```

Cables and Cabling
==================

One thing my electronics instructor stressed was the importance in selecting the proper wiring. As the smaller
the diameter of the wire is, the faster the current will travel and the quicker the current will experience
voltage drop. In regards to RF applications cabling can be quite an overwhelming subject, as the number of
different cables, each with their own specific purpose, is too numerous to cover in this wiki. The same is the
case in regards to cabling connectors. This complexity is compounded by difference variations betwen
manufacturers and the requirement of manufacturers to use their own identification schema to avoid violating 
copyright laws.

Fortunately, only those who specialize in cabling have to know it all. For the average RF user, often what
they need can be purchased at any local hardware store, but it is still benefitial to have some basic
understanding of cable varieties in order to meet your specific needs.

Table Of Cable
---------------

Below is a table consisting of some of the many varieties of cable available. Included are those we possess
familiarity with, and these may or may not be the more popular varieties.

| Cable ID  | Impedence  | Bandwidth | Loss per Foot  | Insulation | Bend Rad | Outer Diameter | Features     |
| --------- | ---------- | --------- | -------------- | ---------- | -------- | -------------- | -----------  |
| RG316     | 50db       | 6ghz      | 0.55           | PTFE       | 0.50     | 0.098          | Buriable     |
| LMR100    | 90db       | 5.8ghz    | 0.64           | TPE        | 0.25     | 0.110          | Flexibility  |
| RG174     | 75db       | 5ghz      | 0.60           | PVC        | 0.25     | 0.110          | Flexibility  |
| RG188     | 50db       | 10ghz     | 1.33           | PTFE       | N/A      | 0.118          | High Temp Op |
| RG6       | 75db       | 2.5ghz    | 1.48           | Poly       | 0.90     | 0.33           | Impedence    |
| RG8       | 50db       | 4ghz      | 0.215          | Poly       | 4.00     | 0.403          | Low Loss     |
| RG58      | 50db       | 1ghz      | 0.60           | PVC        | 0.98     | 0.195          | Overall Perf |

Connectors
----------

Below is a hand diagram showing some of the most popular rf connectors.

![Rf Connectors](/assets/img/rf_conn.png)

It is important to remember each connector has a different frequency range in which it can operate.

![Connector Range](/assets/img/conn_range.png)

### Installation

Below is a graphic that explains the process of connector installation. The import bit is the outer shield
needs to be conductive with the outer portion of the connector, and the core wire with the inner core of the
connector. 

![Connector Installation](/assets/img/con_install.gif)
