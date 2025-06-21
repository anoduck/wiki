```text
#     _          _   _ _             _
#    / \   _ __ | |_(_) |_ _   _  __| | ___
#   / _ \ | '_ \| __| | __| | | |/ _` |/ _ \
#  / ___ \| |_) | |_| | |_| |_| | (_| |  __/
# /_/   \_\ .__/ \__|_|\__|\__,_|\__,_|\___|
#         |_|
```

Aptitude
=========

apt (Advanced Package Tool) is a package management system used in Debian-based Linux
distributions, such as Ubuntu. It simplifies the process of managing software packages
by providing a command-line interface for installing, updating, and removing software.

Key features of apt include:
- Package Installation: You can easily install new software packages from repositories
    using commands like apt install package_name.
- Package Removal: It allows you to remove installed packages with commands like apt
    remove package_name.

    Updating Packages: You can update all installed packages to their latest versions using apt update followed by apt upgrade.

    Dependency Management: apt automatically handles dependencies, ensuring that all required packages are installed when you install a new package.

    Repository Management: It can manage software repositories, allowing users to add or remove sources from which packages can be downloaded.

Overall, apt is a powerful tool for managing software on Debian-based systems, making it easier for users to maintain their software environment.

```bash
comm -23 <(apt-mark showmanual | sort -u) <(gzip -dc /var/log/installer/initial-status.gz | sed -n 's/^Package: //p' | sort -u)
```
