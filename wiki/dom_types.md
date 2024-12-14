```text
#  ____                        _         _____
# |  _ \  ___  _ __ ___   __ _(_)_ __   |_   _|   _ _ __   ___  ___
# | | | |/ _ \| '_ ` _ \ / _` | | '_ \    | || | | | '_ \ / _ \/ __|
# | |_| | (_) | | | | | | (_| | | | | |   | || |_| | |_) |  __/\__ \
# |____/ \___/|_| |_| |_|\__,_|_|_| |_|   |_| \__, | .__/ \___||___/
#                                             |___/|_|
#
```

Domain Record Types
===========================

If you have ever had to register your own domain or worked with any form of domain name server, then you have
already encountered many of these terms. They all can be rather confusing, and are rarely used enough to
implant a firm understanding of their meaning. Which is what is discussed in this entry, that is, mostly the
definitions to these terms.

Domain
------

A domain is readable and comprehendable identifier and resource locator used to represent a collection of computers or a single
computer. For the most part, they are alpha numeric and come in the form of secondary level domain followed by a period
and then followed by a top level domain. So in domain name address of google (google.com), the top level
domain would be simply the "com", and the secondary level domain would be the "google". 

Zone
----

A zone represents a single instance of a domain. So a zone would be "photos.google.com" or "yahoo.com". In the first example, "photos.google.com",
this distinction becomes more clear. As "google.com" and "photos.google.com" are within one domain,
"google.com", but represent two different zones. 

DNS Record
---------

Records refer to the entries of zones maintained by a domain name server. A zone can have more than one IP
address, and an IP address can have more than one zones assigned to it. It is the record that defines these
values, and there are several types. 

### "A" Record

The "A" record is the primary type of record that associate a zone with an ipv4 address or multiple ipv4 addresses.

### "AAA" Record

The "AAA" record does the same thing as an "A" record, except with ipv6.

### "CNAME" Record

"CNAME" is an abbreviation for "Canonical Name Record". CNAMEs are a form of zone records that do not point to
an IP address, but point to another zone, and inform the client to use the same routing information as the
zone it points to. They are only valid with subdomains.

### "MX" Record

"MX" records are used for mail exchanges, which we now refer to as mail servers. They are used to inform
clients of the ip address the zone is using to accept incoming mail.


References
----------

- https://www.pbrumby.com/2018/05/09/dns-records-explained/
