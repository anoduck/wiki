```text
#  ____                        _         _   _
# |  _ \  ___  _ __ ___   __ _(_)_ __   | \ | | __ _ _ __ ___   ___
# | | | |/ _ \| '_ ` _ \ / _` | | '_ \  |  \| |/ _` | '_ ` _ \ / _ \
# | |_| | (_) | | | | | | (_| | | | | | | |\  | (_| | | | | | |  __/
# |____/ \___/|_| |_| |_|\__,_|_|_| |_| |_| \_|\__,_|_| |_| |_|\___|
#  ____
# / ___|  ___ _ ____   _____ _ __
# \___ \ / _ \ '__\ \ / / _ \ '__|
#  ___) |  __/ |   \ V /  __/ |
# |____/ \___|_|    \_/ \___|_|
```

Domain Name Server
==================

A Domain Name Server (DNS) is like the internet's phonebook. It’s a system that translates human-friendly website names,
like "google.com," into the numerical IP addresses (e.g., 142.250.190.14) that computers use to locate each other on the
network. When you type a URL into your browser, the DNS quickly looks up the corresponding IP address, connecting you to
the right server so you can access the site. It’s a critical part of how the internet works, making navigation simple and
seamless.

## DNS Types

There are numerous different types of dns records. They all do something fancy.

* CNAME:
* A:
* AAAA:
* ALIAS:
* MX:

## Setting up dns for mail 

DNS records

How it is configured depends on your DNS provider (or server, if you run your own). Here is how your DNS zone should look like:

; Basic domain->IP records, you probably already have them.
example.org.   A     10.2.3.4
example.org.   AAAA  2001:beef::1

; It says that "server mx1.example.org is handling messages for example.org".
example.org.   MX    10 mx1.example.org.
; Of course, mx1 should have A/AAAA entry as well:
mx1.example.org.   A     10.2.3.4
mx1.example.org.   AAAA  2001:beef::1

; Use SPF to say that the servers in "MX" above are allowed to send email
; for this domain, and nobody else.
example.org.     TXT   "v=spf1 mx ~all"
; It is recommended to server SPF record for both domain and MX hostname
mx1.example.org. TXT   "v=spf1 a ~all"

; Opt-in into DMARC with permissive policy and request reports about broken
; messages.
_dmarc.example.org.   TXT    "v=DMARC1; p=quarantine; ruf=mailto:postmaster@example.org"

; Mark domain as MTA-STS compatible (see the next section)
; and request reports about failures to be sent to postmaster@example.org
_mta-sts.example.org.   TXT    "v=STSv1; id=1"
_smtp._tls.example.org. TXT    "v=TLSRPTv1;rua=mailto:postmaster@example.org"

And the last one, DKIM key, is a bit tricky. maddy generated a key for you on the first start-up. You can find it in /var/lib/maddy/dkim_keys/example.org_default.dns. You need to put it in a TXT record for default._domainkey.example.org. domain, like that:

default._domainkey.example.org.    TXT   "v=DKIM1; k=ed25519; p=nAcUUozPlhc4VPhp7hZl+owES7j7OlEv0laaDEDBAqg="

MTA-STS and DANE

By default SMTP is not protected against active attacks. MTA-STS policy tells compatible senders to always use properly authenticated TLS when talking to your server, offering a simple-to-deploy way to protect your server against MitM attacks on port 25.

Basically, you to create a file with following contents and make it available at https://mta-sts.example.org/.well-known/mta-sts.txt:

version: STSv1
mode: enforce
max_age: 604800
mx: mx1.example.org

Note: mx1.example.org in the file is your MX hostname, In a simple configuration, it will be the same as your hostname example.org. In a more complex setups, you would have multiple MX servers - add them all once per line, like that:

mx: mx1.example.org
mx: mx2.example.org

It is also recommended to set a TLSA (DANE) record. Use https://www.huque.com/bin/gen_tlsa to generate one. Set port to 25, Transport Protocol to "tcp" and Domain Name to the MX hostname. Example of a valid record:

_25._tcp.mx1.example.org. TLSA 3 1 1 7f59d873a70e224b184c95a4eb54caa9621e47d48b4a25d312d83d96e3498238

## Public DNS Servers

Just a simple list of publicly available DNS servers for use.

* Cloudflare: 1.1.1.1 1.0.0.1
* Cloudflare anti malware: 1.1.1.2 1.0.0.2
* Google: 8.8.8.8 8.8.4.4
* Quad9: 9.9.9.9 149.112.112.112
* DNS Watch: 84.200.69.80 84.200.70.40
* Comodo Secure DNS: 8.26.56.26 8.20.247.20
* Yandex: 77.88.8.7 77.88.8.3
* Uncensored DNS: 91.239.100.100 89.233.43.71
