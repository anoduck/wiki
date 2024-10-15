```text
#     _
#    / \   _ __ ___   __ _ ___ ___
#   / _ \ | '_ ` _ \ / _` / __/ __|
#  / ___ \| | | | | | (_| \__ \__ \
# /_/   \_\_| |_| |_|\__,_|___/___/
#
```

Amass
-----

In a little bit of a crunch today, as morning is arriving fast. So, no fancy informative introduction this
time. 

Amass began life as one tool with five different "subcommands". Beginning in July 19 2023, it's developer
OWASP, split the project in twain. This meant that Amass would from that moment forwards only have two
subcommands, "intel" and "enum". The other three subcommands would be partitioned off to their own project,
"oam-tools". The reason for mentioning this is because OWASP has allowed their documentation to go
unmaintained for four years, and the docs still claim the oam-tools subcommands are still present. They also
have allowed the example configuration file for Amass go unmaintained, because it still contains configuration
options that are no longer valid. We can only assume, they expect all network analysts to be able to read
minds.


### OAM-Tools

Is the new project that resolved from splintering off the two less popular, but more difficult to maintain, features
of the Amass project. 

#### Installing OAM-Tools

Oam tools can be easily installed from source using go. To install simply use:

```bash
go install -v github.com/owasp-amass/oam-tools/cmd/...@master
```

Since both Amass and OAM-Tools require libc, neither of them are compatible with OpenBSD or MUSL based linux
distributions. Which means that unlike when installing a go pkg in OpenBSD, you do not have to use sudo to
install it. Because that was awkwardly stated, let me simply state you will not use "sudo" to install
OAM-Tools.

After installation, you will find all three tools have been installed to `$GOBIN`, and should be in your path.
Rather than use a hyphen, all three have replaced the hyphen with an underscore. This is in spite of the
documentation claiming there is a hyphen.

#### OAM-Tools Usage

Well, it appears OWASP is still working out the documentation a year after forking off the project. For
Example, here is the output of `oam_sub --help`:

```bash
Usage: oam_subs [options]

# Notice here, the config option. What does it read at the end of the line?
  -config string
        Path to the YAML configuration file. Additional details below
  -d value
        Domain names separated by commas (can be used multiple times)
  -demo
        Censor output to make it suitable for demonstrations
  -df string
        Path to a file providing root domain names
  -dir string
        Path to the directory containing the graph database
  -h    Show the program usage message
  -help
        Show the program usage message
  -ip
        Show the IP addresses for discovered names
  -ipv4
        Show the IPv4 addresses for discovered names
  -ipv6
        Show the IPv6 addresses for discovered names
  -names
        Print Just Discovered Names
  -nocolor
        Disable colorized output
  -o string
        Path to the text file containing terminal stdout/stderr
  -show
        Print the results for the enumeration index + domains provided
  -silent
        Disable all output during execution
  -summary
        Print Just ASN Table Summary
```

Notice anything? If you guessed that it claims there is more information regarding the configuration file, but
yet fails to provide that information, you are correct. This is almost comical, almost, but not really.
