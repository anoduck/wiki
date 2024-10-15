```text
#   ___                   ____ ____  _
#  / _ \ _ __   ___ _ __ / ___/ ___|| |
# | | | | '_ \ / _ \ '_ \\___ \___ \| |
# | |_| | |_) |  __/ | | |___) |__) | |___
#  \___/| .__/ \___|_| |_|____/____/|_____|
#       |_|
#
```

OpenSSL
-------

> I don't care, I need sleep. So here it is.

OpenSSL stands for the Open Source Secure Socket Layer, it is a standard of an cryptographic security implementation that is more than likely the most widely used security standard in the world. So there ya go.

At one time in their life or another all system administrators will need to understand how to generate OpenSSL certificates on their own. It is not a difficult thing to do, and can routinely be performed with a single command.
The difficulty is, most administrators do not do it often enough to remember the full syntax for that single command. Which is obviously occurring as this post is written.

```bash
openssl req -x509 -newkey rsa:4096 -days days -keyout NAME.key -out NAME.pem
```

So there ya go. 

OpenSSL can also be used to do some really neat stuff, like encrypt files.

```bash
# To encrypt
openssl enc -e -aes-256-cbc \
  -salt \
  -pbkdf2 \
  -iter 1000000 \
  -md sha512 \
  -base64 \
  -in somefile \
  -out somefile.enc # to encrypt

# To decrypt.
openssl enc -d -aes-256-cbc \
  -salt \
  -pbkdf2 \
  -iter 1000000 \
  -md sha512 \
  -base64 \
  -in somefile.enc \
  -out somefile # to decrypt
```
