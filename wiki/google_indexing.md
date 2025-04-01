```text
#   ____                   _        ___           _           _
#  / ___| ___   ___   __ _| | ___  |_ _|_ __   __| | _____  _(_)_ __   __ _
# | |  _ / _ \ / _ \ / _` | |/ _ \  | || '_ \ / _` |/ _ \ \/ / | '_ \ / _` |
# | |_| | (_) | (_) | (_| | |  __/  | || | | | (_| |  __/>  <| | | | | (_| |
#  \____|\___/ \___/ \__, |_|\___| |___|_| |_|\__,_|\___/_/\_\_|_| |_|\__, |
#                    |___/                                            |___/
```

Google Indexing
===============

There is a reason people earn money registering sites and optimizing them so google's webcrawler can index
them, it is because this process is a massive pain in the ass. The page indexing error report messages are
rather vaguely written, so it is difficult to discern what they acutally mean sometimes. If you ever change
your site, and you are destined to at some point, this entire process of troubleshooting google indexing
errors starts all over again. For google indexing, these are the facts of life.

1. If you remove or move a page, you will have to create an alias to mark it's place and forward the user to the new location. 
2. If you remove a section, you will need to either block or disallow google from continueing to search for
   it. It is easiest to do this with a "Disallow" entry in `robots.txt` than add a header on your webserver.
3. Although, google provides a means for you to remove a file from indexing, it is not intended for what you
   think it is, and you will in fact never use that feature.
4. 404 errors are tricky, because Google provides you with "examples". These "examples" are not the cause of
   the error, because they consist of valid 404 responses (because there is no file there). The "details" tab
   should list the url causing the issue. One 404 error will prevent your entire site from being indexed, and
   often result from an overworked server.

