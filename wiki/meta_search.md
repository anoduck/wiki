```text
#  __  __      _          ____                      _
# |  \/  | ___| |_ __ _  / ___|  ___  __ _ _ __ ___| |__
# | |\/| |/ _ \ __/ _` | \___ \ / _ \/ _` | '__/ __| '_ \
# | |  | |  __/ || (_| |  ___) |  __/ (_| | | | (__| | | |
# |_|  |_|\___|\__\__,_| |____/ \___|\__,_|_|  \___|_| |_|
#
#  _____             _
# | ____|_ __   __ _(_)_ __   ___  ___
# |  _| | '_ \ / _` | | '_ \ / _ \/ __|
# | |___| | | | (_| | | | | |  __/\__ \
# |_____|_| |_|\__, |_|_| |_|\___||___/
#              |___/
```

Mega Search Engines
===================

Meta Search Engines basically are search engines that act as a search proxy, which then queries a predefined
set of external search engines and returns the results. They do not perform the actual task of crawling and
scraping relevant information from websites, but rely on other search engines to do this from them. The
reported benefits of using these search engines are increased user security and privacy. Although, it is
unclear exactly how this is accomplished when the user is hosting the meta search engine locally and/or himself.

Available Engines
-----------------

There are numerous meta search engines available, unfortunately most of these are no longer being actively
maintained. We are going to focus on two of the most popular engines that are still actively maintained.

### SearX-NG

SearxNG is the successor to the original and ever so popular meta search engine SearX. SearX-NG centers around
a community driven effort to provide users with improved features over the original SearX. The project is
quite stable and possesses a stable codebase. Sources used to forward search queries to are organized into
engines, and can be enabled and disabled as one prefers. Developing custom engines does not appear to be much
of a challenge either, in case it does not provide a solution that is desired. There are already numerous
publicly available instances of SearX-NG available, which means installation is not required. 

### WebsurfX

WebsurfX is a meta search engine inspired by SearX-NG written in rust, and as with everything written in rust
it is fast. WebSurfX's footprint and load is considerably smaller than SearX-NG's, explaining why it's
developers claim it is twice as fast as SearX-NG. Whether WebSurfX will be able to hold onto this title is
currently unforseen, as WebsurfX only scrapes search queries from two sources, SearX-NG and DuckDuckGo.
Regardless of this limitation, WebsurfX boasts an improved web user interface over it's inspiring competitor.
