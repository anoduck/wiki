```text
 __      __      ___.       _________                                       
/  \    /  \ ____\_ |__    /   _____/ ______________  __ ___________  ______
\   \/\/   // __ \| __ \   \_____  \_/ __ \_  __ \  \/ // __ \_  __ \/  ___/
 \        /\  ___/| \_\ \  /        \  ___/|  | \/\   /\  ___/|  | \/\___ \ 
  \__/\  /  \___  >___  / /_______  /\___  >__|    \_/  \___  >__|  /____  >
       \/       \/    \/          \/     \/                 \/           \/ 
```

Web Servers
-----------

The term "Web Server" is commonly used to refer two seperate items; the software that serves webpages and the
physical computational device that runs the software that serves the webpages. Misunderstanding is
often avoided due to context in which the term is applied, but to provide a technical definition to the
term, this difference of application had to be pointed out. In this article we are referring to later and it's
configuration.

(I remember know why I disabled the grammar linter "write good" from my editor. It is never satisfied.)

### Software Available

The oldest web server software that has stably maintained production is Apache, and it is also the most
popular. Next to Apache, is Nginx, which was originally written from code borrowed from a reverse proxy, but
has maintained quite a favorable following and is known for it's blazing fast speed. Lighttpd probably would
rank as the third most popular web server, which was known for it's small footprint and small resource load. A
forth option, that is a newer entry into the markey is caddy, which make quite a big splash on the scene due
to featuring it's single file size and automated ssl certificate generation.

It used to be the case that web servers were a required part of any website, simply because there was not
really any other means to communicate the webpage via the http protocol other than using a server. In the
early 2000's this changed and web servers are no longer a required feature of the world wide web. Languages
such as nodejs, go, and python implement http libraries that replace the need for webservers. This
"self-contained" method of hosting webpages is now more common and on it's way to becoming the norm. 

The actual plethora of web servers available on the market is nearly endless, many have grown and disappeared
from favorability, and if not already, are well on their way to disappearing into the oblivion of dead
software.

#### Which one?

A good network systems administrator knows how to configure and manage the two most popular webserver
applications; Apache and Nginx. Which with experience becomes rather a trivial accomplishment. Both of the two
have their benefits and drawbacks, but in general, which one is preferred is more dependent upon other
factors. Such as ease of installation and configuration, some web applications will actual prefer their
software to run in one over another. Apache has a small advantage over nginx in regards to applications that
are programmed in php, due to it's native php module. 

### Table of Articles

Enough of explaining! Let's get to business. So, a table.

| [Caddy](caddy) | [Apache](apache) | [Nginx](nginx) |


