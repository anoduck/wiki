```text
   ____     _      ____     ____   __   __ 
U /"___|U  /"\  u |  _"\   |  _"\  \ \ / / 
\| | u   \/ _ \/ /| | | | /| | | |  \ V /  
 | |/__  / ___ \ U| |_| |\U| |_| |\U_|"|_u 
  \____|/_/   \_\ |____/ u |____/ u  |_|   
 _// \\  \\    >>  |||_     |||_ .-,//|(_  
(__)(__)(__)  (__)(__)_)   (__)_) \_) (__) 
```

Caddy: A new breed of server
----------------------------

Most of the big name webservers, such as Apache and Nginx, as well as most applications in general, have
libraries where resources are found that help the application perform it's functionality. Caddy is different,
because it is comprised of a single and reasonably sized file. It is completely self contained, and does not
come with or need any libraries. Which at it's time was quite unique. Also, Caddy provides automatic support
for ssl, which means it generates it own valid and secure ssl certificates. This later feature is to this day
still quite a "game changer". 

### Configuration

The developers of Caddy say that configuration of Caddy is easier than the other servers on the market.
Although not much work has been done with Caddy, this statement is still open for debate. It might be true
that one can become adept at performing a certain task if they do it often enough. In Caddy's situation, it
also might be true Caddy provides so many bells and whistles, system administrators don't quite know what to
do with all of them. Nonetheless, it is a different beast altogether, and because of this, there is a learning
curve.

#### One Configuration, two choices

Caddy can be configured in a file referred to as a "Caddyfile", and it can be configured in straight json as
well. The difficulty with the latter is it is a much more challenging due to lack of distinctive structure for
directives, and lack of labeling for distinction of values. Below is the same Caddy configuration provided in
the two different configuration formats. 

##### Two Formats Example: Caddyfile

First we will show what an actual in use caddyfile looks like.

```caddyfile
{
	log default {
		output file /var/log/caddy/caddy.log {
			roll_size 10MiB
			roll_keep 3
		}
		format json
		level DEBUG
	}
}
example {
	root * /var/www/example
	
	header +X-Frame-Options "SAMEORIGIN"
	header +X-Content-Type-Options "nosniff"

	php_fastcgi 127.0.0.1:9000 {
		root /var/www/example
		index off
	}

	try_files {path} {path}/ =404

	file_server 
}
```

##### Two Formats Example: Json

Now the exact same file, but in caddy's json format.

```json
{
	"logging": {
		"logs": {
			"default": {
				"writer": {
					"filename": "/var/log/caddy/caddy.log",
					"output": "file",
					"roll_keep": 3,
					"roll_size_mb": 10
				},
				"encoder": {
					"format": "json"
				},
				"level": "DEBUG"
			}
		}
	},
	"apps": {
		"http": {
			"servers": {
				"srv0": {
					"listen": [
						":443"
					],
					"routes": [
						{
							"match": [
								{
									"host": [
										"example.com"
									]
								}
							],
							"handle": [
								{
									"handler": "subroute",
									"routes": [
										{
											"handle": [
												{
													"handler": "vars",
													"root": "/var/www/example"
												},
												{
													"handler": "headers",
													"response": {
														"add": {
															"X-Frame-Options": [
																"SAMEORIGIN"
															]
														}
													}
												},
												{
													"handler": "headers",
													"response": {
														"add": {
															"X-Content-Type-Options": [
																"nosniff"
															]
														}
													}
												}
											]
										},
										{
											"handle": [
												{
													"handler": "rewrite",
													"uri": "{http.matchers.file.relative}"
												}
											],
											"match": [
												{
													"file": {
														"try_files": [
															"{http.request.uri.path}",
															"{http.request.uri.path}/",
															"=404"
														]
													}
												}
											]
										},
										{
											"handle": [
												{
													"handler": "reverse_proxy",
													"transport": {
														"protocol": "fastcgi",
														"root": "/var/www/example",
														"split_path": [
															".php"
														]
													},
													"upstreams": [
														{
															"dial": "127.0.0.1:9000"
														}
													]
												}
											],
											"match": [
												{
													"path": [
														"*.php"
													]
												}
											]
										},
										{
											"handle": [
												{
													"handler": "file_server",
													"hide": [
														"./Caddyfile"
													]
												}
											]
										}
									]
								}
							],
							"terminal": true
						}
					]
				}
			}
		}
	}
}
```

##### Conclusion: Caddyfile

Although completely unnecessary, this is a clear and evident demonstration as to why the Caddyfile format is
the really the only option for configuring Caddy. 

You might be wondering why configuring caddy in json is even an option? Which, to provide a simple answer would
be to explain that regardless of which of the two are used, both we end up being fed to Caddy as json before use.
This is because regardless of its shortcomings, json is an efficient means to store data. Outside of that, I
got nothing.

#### Caddyfile

> It's a bitch, but get used to it.

##### Structure

From a glance, it looks as if the Caddfile was originally modeled after the nginx configuration file. Both use
similar structure and directives. Although while writing an nginx configuration could be analogized to
performing break dancing, writing a Caddyfile would be analogous to doing the charleston. (Ok, I admit, that
analogy sucked, but stay with me.)

There are primarily two parts to a caddy configuration file, or at least two parts which actually matter.
These parts are the global section and the site section. You can have numerous site sections, but only one
global section.


