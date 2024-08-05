```text
__/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\____/\\\________/\\\_        
 _\////////////\\\____/\\\/////////\\\_\/\\\_______\/\\\_       
  ___________/\\\/____\//\\\______\///__\/\\\_______\/\\\_      
   _________/\\\/_______\////\\\_________\/\\\\\\\\\\\\\\\_     
    _______/\\\/____________\////\\\______\/\\\/////////\\\_    
     _____/\\\/_________________\////\\\___\/\\\_______\/\\\_   
      ___/\\\/____________/\\\______\//\\\__\/\\\_______\/\\\_  
       __/\\\\\\\\\\\\\\\_\///\\\\\\\\\\\/___\/\\\_______\/\\\_ 
        _\///////////////____\///////////_____\///________\///__
```

ZSH: The baddest mower frecking shell on the planet...(we think)...
-------------------------------------------------------------------

> Only stone cold hard @$$ thugs need apply, and word to your momma.

### Zsh is not Bash

Obviously, it is a posix compliant shell, which is __mostly__ backwards compatible with bash. Although, do not
make the mistake of believing it is completely compatible with bash, because it is not, just mostly. Also,
keep in mind, ZSH is mostly compatible with bash, but bash is not compatible with ZSH. So, it doesn't
work in reverse. Zsh is not a dropin replacement for bash either. Bash is much older than ZSH, more commonly
found and distributed. Bash also possesses a considerably smaller footprint with less system load than ZSH,
and bash is exponentially more documented than zsh.

### Shell Frameworks

Shell frameworks are a means to make configuration/customization of shells easier for users. They almost
always come with a basic set of default configurations, prompt styles, completions, and additional functions.
Shell frameworks also provide a means to manage shell plugins. Shell plugins plugins are modularized shell
scripts that provide additional features to a shell. They can provide a fancy prompt, or completions for a
specific command, or extra commands. Shell frameworks manage these plugins by either enabling or disabling
their loading during runtime and can act like package managers by updating, installing, or removing plugins.
Use of shell frameworks really can result in some insanely awesome shell environments.

#### The Zsh framework wars

For some yet to be identified reason, the use of frameworks is much more common amongst zsh users than bash
users. There is a quite good shell framework for bash named [bash-it](https://github.com/Bash-it/bash-it),
but for some reason it hasn't recieved as much attention as zsh frameworks do. Before drifting too far off
subject, the fish shell does also have a framework or two that are quite good, but that is of lesser
importance. For zsh, frameworks are so commonly used that there is quite stiff competition over market share.

There is one zsh framework appears to have transcended the confines of being labeled a mere framework, that
framework also happens to be the first of it's kind, Oh-My-Zsh. Whose implementation can be included in nearly
every other framework for use as a library. 

### Zi: The Zenith

Having tried the majority of the available frameworks at one point or another, they all pale in comparison to
Zi. To coin a popular expression that is overused these days, Zi is a "Game Changer". 

#### Zi completion initialization

> [!INFO]
> The majority of shell intialization time is consumed generating completions.
> You should write your configuration to generate them only once.

If not configured correctly, zi's completion management system can generate some undesirable error messages.
Such as:

```zsh
(eval):62: command not found: compdef
complete:13: command not found: compdef
(eval):39: command not found: compdef
```

Which is the purpose of contributing to the wiki today, to hammer out how zi handles completion
initialization.

##### Zi Completions Management

__Commands__


| Command     | Description                   |
| ------      | ------------                  |
| zicompinit  | autoload compinit && compinit |
| compinit    | Refresh installed completions |
| cdreplay -q | Replay Completion definitions |



