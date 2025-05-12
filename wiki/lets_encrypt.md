 _         _   _       _____                             _   
| |    ___| |_( )___  | ____|_ __   ___ _ __ _   _ _ __ | |_ 
| |   / _ \ __|// __| |  _| | '_ \ / __| '__| | | | '_ \| __|
| |__|  __/ |_  \__ \ | |___| | | | (__| |  | |_| | |_) | |_ 
|_____\___|\__| |___/ |_____|_| |_|\___|_|   \__, | .__/ \__|
                                             |___/|_|        
```

Generating SSL Certificates with Let's Encrypt via Eff's Certbot
================================================================

This is another one of those things, where if you don't do it nearly every week, you will forget. Then when you
look up how to do it, it is so simple, you feel stupid for ever forgetting it. It is pretty easy to do, but it
is not uncommon to run into snags every once in a while. The most common of these snags is caused when a new
certificate is requested for a newly created domain record, and the record has not had enough time to be
propagated through out all the various required DNS servers to identify it's current address as authoritative.

Using Let's Encrypt was not always an option, not too horrifically long ago, there were only two means by
which one could acquire an ssl certificate for their site, either pay for a trusted body to generate one for
you or generate one yourself. Back then, things were not as strict about ssl certificates as they are now, and
you could get by with a self generated certificate. Let's Encrypt is one of the steps forward that allowed the
internet to have the level of security it now does.

## Implementations

It is not the point of this wiki entry to cover all the implementations of Let's Encrypt, as they are too
plentiful in number to exhaustively list, but we will cover two of the more popular implementations; acme.sh
and certbot. 

Of the two, acme.sh is reported as being the easiest and most accessible, but certbot is in our opinion nearly
identical. For both of these we shall assume you already have a webserver up and running.

### Certbot

Certbot is an implementation of Let's Encrypt created by the Electronic Frontier Foundation, who as of the last
time we checked were supposed to be the good guys. Although, these things do change.

#### Generate a certificate

> [!info] Always! Use the test servers first.
> It is ultra super duper highly recommended to check everything is configured correctly by obtaining a
> test certificate first from a staging server. This is done with the `--test-cert` flag.

```bash
sudo certbot certonly --cert-name {$SOME_NAME} --webroot --webroot-path {$SOME_PATH} -d {$DOMAIN or $COMMA_SEPARATED_DOMAINS}
```

#### List Certificates

```bash
sudo certbot certificates
```

#### Revoke Certificate

```bash
sudo certbot revoke --cert-name {$SOME_NAME}
```

1. It will then ask you if you would like to remove the certificate, you type "y" for yes.
2. It will then ask you to confirm, type "y" again for yes.

#### Renaming Certificates

Simply revoke the certificate in question and delete it. Then execute a new request for the desired
certificate. Specifically invoke the `--cert-name` flag.

#### Change webroot or domains

```bash
sudo certbot reconfigure --cert-name {$SOME_NAME}
```

This is interactive, and will prompt you for webroot paths for every domain.

### Acme.sh

TDL.
