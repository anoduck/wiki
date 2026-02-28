```text
#  _        _    _   _  ____ _   _   _    ____ _____   _____ ___   ___  _
# | |      / \  | \ | |/ ___| | | | / \  / ___| ____| |_   _/ _ \ / _ \| |
# | |     / _ \ |  \| | |  _| | | |/ _ \| |  _|  _|     | || | | | | | | |
# | |___ / ___ \| |\  | |_| | |_| / ___ \ |_| | |___    | || |_| | |_| | |___
# |_____/_/   \_\_| \_|\____|\___/_/   \_\____|_____|   |_| \___/ \___/|_____|
#
```

# Language Tool: Spelling and Grammar Checking Language Server

The best way to use LanguageTool on Unix and Linux systems is to run your own instance of it, in fact this
was at one time the only way to use it. Well, that is before they started charging people to use. Anyways, if
you run your own server, then you can use it for free, which is something the developers proabably don't want
too many people to know about.

## Installation and configuration

Here are the steps to get your own server running. 

1. Download the most recent snapshot from: https://internal1.languagetool.org/snapshots/
2. Extract the zip archive somewhere in your home folder. `unzip LanguageTool-latest-snapshot.zip`
3. Next clone the repo for fastText: `git clone https://github.com/facebookresearch/fastText.git ` and `cd
   fastText`
4. Then perform the build of the fastText tool with make: `make`
5. Next you will need to download a language model, they offer two: https://fasttext.cc/docs/en/language-identification.html
6. Then you will need to create a file called `server.properties` somewhere on your system with the following
   settings set.
    ```ini
    fasttextModel=/path/to/fasttext/lid.176.bin
    fasttextBinary=/path/to/fasttext/fasttext
    ```
7. Last, execute the server with: java -cp languagetool-server.jar org.languagetool.server.HTTPServer --config server.properties --port 8081 --allow-origin

