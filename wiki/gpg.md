```text
#   ____ _   _ _   _ ____   ____
#  / ___| \ | | | | |  _ \ / ___|
# | |  _|  \| | | | | |_) | |  _
# | |_| | |\  | |_| |  __/| |_| |
#  \____|_| \_|\___/|_|    \____|
#
```

# GPG: The Gnu Privacy Guard encryption standard.

It does pretty cool shit.

It started off as a completely free and open source implementation of the PGP standard, but has diverged
significantly recently to make it no long 100% compatible with PGP.

GnuPG is a hybrid-encryption software program because it uses a combination of conventional symmetric-key
cryptography for speed, and public-key cryptography for ease of secure key exchange, typically by using
the recipient's public key to encrypt a session key which is used only once.

## Working with GPG

It is one of those thing every developer should be able to do, but they do not use it often enough to
completely memorize how to do everything.

### Setup and Configuration

The default directory for gpg is `~/.gnupg`. This can be overwritten with the `--homedir` flag or the
`$GNUPGHOME` environement variable.

Add these two lines to either `~/.gnupg/gpg.conf` for user level or `/etc/gnupg/gpg.conf` for system level.

```ini
no-default-keyring
keyring keyring-path
```

### Basic Operations

All operations with gpg begin with the `gpg` command followed by a flag that indicates the desired operation.

|                     Flag(s)                      |           Operation            |        Notes        |
| :----------------------------------------------: | :----------------------------: | :-----------------: |
|                 `--full-gen-key`                 |      Create a new GPG Key      | Interactive Prompt. |
| `--export --armor --output "$KEYFILE" "$USERID"` | Exports GPG key to "$KEYFILE"  |                     |
|              `--import "$KEYFILE"`               | Imports GPG key into key ring. |                     |
|                  `--list-keys`                   |  list keys in public keyring   |                     |
|               `--list-secret-keys`               |  list keys in secret keyring.  |                     |

To create a new key simply use `gpg --full-gen-key`.

### Further info

- Further info can be found on the [Arch Wiki](https://wiki.archlinux.org/title/Gpg)
