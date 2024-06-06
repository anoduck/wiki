```
#   ___                   ____ ____  ____    _   _ _____ _____ ____  ____
#  / _ \ _ __   ___ _ __ | __ ) ___||  _ \  | | | |_   _|_   _|  _ \|  _ \
# | | | | '_ \ / _ \ '_ \|  _ \___ \| | | | | |_| | | |   | | | |_) | | | |
# | |_| | |_) |  __/ | | | |_) |__) | |_| | |  _  | | |   | | |  __/| |_| |
#  \___/| .__/ \___|_| |_|____/____/|____/  |_| |_| |_|   |_| |_|   |____/
#       |_|
#
```

OpenBSD's HTTPD
================

What a pain in the ass.
-----------------------

Ok, I have been working with this web server implementation for some time now, and have not had a single
reason to move to anything else. It is lightweight, secure, fast, and reasonably easy to configure. The most
difficultly I have ever run into was due to not reading the man pages fully.

### What I neglected to read about: The Directory directive

In Nginx, Apache, and Hiawatha(RIP) there is a directive to designate what the default file should be for the
website. As everyone knows, this file is `index.html`. The reason for you to be able to configure this option
is to allow you to service other primary hierarchical files, such as `index.php`, `index.py`, `start.html`,
etc, etc... The directive for this usally goes in the first tier after you have designated the site name
and/or site address, but not in OpenBSD's httpd. In OpenBSD's httpd, this directive get's placed under the
`Directory` directive leading one to mistakenly interpret it as a parameter to enable guests to view an index
of the contents of the directory defined in the above `directory` directive. Which it does do, but also
controls the ability for the server to serve any file named "index.html". Which makes it really fucking
confusing. Take a look at the example:

```conf
server "example.com" {
	alias www.example.com
	listen on egress tls port 443
	tls {
		certificate "/etc/ssl/example.com.fullchain.pem"
		key "/etc/ssl/private/example.com.key"
	}
	root "/htdocs/example"
	location "/.well-known/acme-challenge/*" {
		root "/acme"
		request strip 2
	}
	location match "^/$" {
	   	request rewrite "/index.html"
	   	directory no index
	}
	location match "^/(.+)$" {
	   	request rewrite "%1/index.html"
	   	directory no index
	}
	location match "^/(.+)[.](.+)$" {
		request no rewrite
		directory no index
	}
	location match "^/(.+)/(.+)[.](.+)$" {
		request no rewrite
		directory no index
	}
	location match "^/(.+)/(.+)$" {
		request rewrite "/%1/%2.html"
		directory no index
	}
	errdocs "/htdocs/errdocs"
	log { access "example-access.log", error "example-error.log" }
}
```

You see the directive for "directory"? Well, that's it. **Don't do this.**

#### Scenario 1

```conf
location "/*" {
    directory auto index
    }
```

In this scenario, a file, `index.html`, will be generated to display the contents of the directory.

#### Scenario 2

```conf
location "/*" {
    directory no index
    }
```

In this scenario, no file will be generated to display the contents of the directory **AND no file named
`index.html` will be served by HTTPD EITHER** 

#### Scenario 3

```conf
location "/*" {
    }
```

In this scenario, no file will be generated, **BUT your index.html file will be served as it is supposed to.**
