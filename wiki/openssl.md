```text
#   ___                   ____ ____  _
#  / _ \ _ __   ___ _ __ / ___/ ___|| |
# | | | | '_ \ / _ \ '_ \\___ \___ \| |
# | |_| | |_) |  __/ | | |___) |__) | |___
#  \___/| .__/ \___|_| |_|____/____/|_____|
#       |_|
```

OpenSSL
=======

> I don't care, I need sleep. So here it is.

OpenSSL stands for the Open Source Secure Socket Layer, it is a standard of an cryptographic security implementation that is more than likely the most widely used security standard in the world. So there ya go.

At one time in their life or another all system administrators will need to understand how to generate OpenSSL certificates on their own. It is not a difficult thing to do, and can routinely be performed with a single command.
The difficulty is, most administrators do not do it often enough to remember the full syntax for that single command. Which is obviously occurring as this post is written.

Doing Stuff
-----------

OpenSSL can be used to do a lot of really really neat stuff. Here are a few of them.

### Generate certificate

```bash
openssl req -x509 -newkey rsa:4096 -days days -keyout NAME.key -out NAME.pem
```

### File Encryption and decryption

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

### Converting formats

Openssl certificates and keys can come in a variety of different formats, each format possessing a different
file extension designating that format. While the content is often the same amongst these formats, the
formatting of the file is different. So, it is important to understand how to convert keys and certs between
these.

#### Converting a `crt` to a `pem`

`openssl x509 -in [$CERT FILE].crt -out [$CERT FILE].pem -outform PEM`
