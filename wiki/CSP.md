```text
   ____            _             _     ____                       _ _
  / ___|___  _ __ | |_ ___ _ __ | |_  / ___|  ___  ___ _   _ _ __(_) |_ _   _
 | |   / _ \| '_ \| __/ _ \ '_ \| __| \___ \ / _ \/ __| | | | '__| | __| | | |
 | |__| (_) | | | | ||  __/ | | | |_   ___) |  __/ (__| |_| | |  | | |_| |_| |
  \____\___/|_| |_|\__\___|_| |_|\__| |____/ \___|\___|\__,_|_|  |_|\__|\__, |
                                                                        |___/
  ____       _ _
 |  _ \ ___ | (_) ___ _   _
 | |_) / _ \| | |/ __| | | |
 |  __/ (_) | | | (__| |_| |
 |_|   \___/|_|_|\___|\__, |
                      |___/
```

Content Security Policy
=======================

> Shit be changing, Bro.

In the ignorance of youth, this did not seem like such a big deal, and would have been disregarded as
unnecessary details. This was before cross site scripting was commonly used, now you have to keep that shit
locked down to prevent these types of attacks.

Content Security Policy header value is one part of the server header that is sent from the client to the server
during every http transaction. It only can be set at the server configuration level, but effects the client as well.
The CSP does not have to be broken down into individual directives, but it is much more secure if it is.

Below is an example of what was considered to be a "Secure" server header a few years ago.

```Caddyfile
header / {
    Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
    X-Xss-Protection "1; mode=block"
    X-Content-Type-Options "nosniff"
    X-Frame-Options "DENY"
    Content-Security-Policy "upgrade-insecure-requests"
    Referrer-Policy "strict-origin-when-cross-origin"
    Cache-Control "public, max-age=15, must-revalidate"
    Feature-Policy "accelerometer 'none'; ambient-light-sensor 'none'; autoplay 'self'; camera 'none'; encrypted-media 'none'; fullscreen 'self'; geolocation 'none'; gyroscope 'none'; magnetometer 'none'; microphone 'none'; midi 'none'; payment 'none'; picture-in-picture *; speaker 'none'; sync-xhr 'none'; usb 'none'; vr 'none'"
}
```

Notice how the CSP is simply "upgrade insecure requests", back in 2018 that was considered secure.

Now, lets break down the most common used directives into a nice table. Oh, all the directives end in `*-src`,
which might make it easier to remember.  `¯\_(ツ)_/¯`

| Directive    | Definition                                                 |
| -----------  | ------------------                                         |
| default-src  | the default policy                                         |
| script-src   | valid JS sources                                           |
| style-src    | valid css sources                                          |
| img-src      | valid image sources                                        |
| font-src     | valid font sources                                         |
| object-src   | valid plugin sources for embed and applet tags             |
| media-src    | valid audio and vid sources                                |
| frame-src    | valid sources for loading frames                           |
| base-uri     | allowed urls for use in src attribute                      |
| child-src    | valid sources for web workers and nested browsing contexts |
| manifest-src | valid sources for application manifests                    |
| connect-src  | Valid sources for AJAX, websocket, fetch, etc...           |

Any of the above, except `base-uri`, can accept similar values. These values are known as a source list, and
trust me, that won't be on Jeopardy.

| Source Value       | Example                                    | Description                                                                                                                                                                                                                                            |
| -------------      | --------                                   | --------------                                                                                                                                                                                                                                         |
| `*`                | img-src *                                  | Wildcard, allows any URL except data: blob: filesystem: schemes.                                                                                                                                                                                       |
| 'none'             | object-src 'none'                          | Prevents loading resources from any source.                                                                                                                                                                                                            |
| 'self'             | script-src 'self'                          | Allows loading resources from the same origin (same scheme, host and port).                                                                                                                                                                            |
| data:              | img-src 'self' data:                       | Allows loading resources via the data scheme (eg Base64 encoded images).                                                                                                                                                                               |
| domain.example.com | img-src domain.example.com                 | Allows loading resources from the specified domain name.                                                                                                                                                                                               |
| *.example.com      | img-src *.example.com                      | Allows loading resources from any subdomain under example.com.                                                                                                                                                                                         |
| https://cdn.com    | img-src https://cdn.com                    | Allows loading resources only over HTTPS matching the given domain.                                                                                                                                                                                    |
| https:             | img-src https:                             | Allows loading resources only over HTTPS on any domain.                                                                                                                                                                                                |
| 'unsafe-inline'    | script-src 'unsafe-inline'                 | Allows use of inline source elements such as style attribute, onclick, or script tag bodies (depends on the context of the source it is applied to) and javascript: URIs                                                                               |
| 'unsafe-eval'      | script-src 'unsafe-eval'                   | Allows unsafe dynamic code evaluation such as JavaScript eval()                                                                                                                                                                                        |
| 'sha256-'          | script-src 'sha256-xyz...'                 | Allows an inline script or CSS to execute if its hash matches the specified hash in the header. Currently supports SHA256, SHA384 or SHA512. CSP Level 2                                                                                               |
| 'nonce-'           | script-src 'nonce-rAnd0m'                  | Allows an inline script or CSS to execute if the script (eg: <script nonce="rAnd0m">) tag contains a nonce attribute matching the nonce specified in the CSP header. The nonce should be a secure random string, and should not be reused. CSP Level 2 |
| 'strict-dynamic'   | script-src 'strict-dynamic'                | Enables an allowed script to load additional scripts via non-"parser-inserted" script elements (for example document.createElement('script'); is allowed). CSP Level 3                                                                                 |
| 'unsafe-hashes'    | script-src 'unsafe-hashes' 'sha256-abc...' | Allows you to enable scripts in event handlers (eg onclick). Does not apply to javascript: or inline <script> CSP Level 3                                                                                                                              |

Not too shabby, since I copied and pasted those directly.

### Quick Answer

For those who are like myself, and hate to read anything at length. Below is considered a "good" starter
policy.

```
default-src 'none'; script-src 'self'; connect-src 'self'; img-src 'self'; style-src 'self';base-uri 'self';form-action 'self'
```

### References

- [Content Security Policy](https://content-security-policy.com/)
