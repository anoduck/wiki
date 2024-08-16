```text
                                    ..::::.                                                                                                                     
         :=+*****+++=-:.-+******++*##*****###*=:                                                                                                                
       +%#+=-------==+*#*=--:::---. .---:::::-+##+.                                                                                                             
     :%#:.:=++***++==-  :=+*****++=-::-*##**+=:.:*%=                                                                                                            
    .@* -*##*******#+.-*##********##*+:.-*****#*= :@+                                                                                                           
    #@ -#**********+ -#***************#+: +#****#* +@                                                                                                           
    @+ ************ :#******************#- =****** -@                                                                                                           
   .@-.**********#= *#****#***********#***- +***** =%                                                                                                           
    @= **********#: =:::::-***********-.:.: :****+ #+                                                                                                           
    %* +**********. :=+=.:..*********..=:-*.:#**#:.@.                                                                .---=---:      :-===--:.    ::             
    =@ -#*********:.##**=++ =#******* -#+*+ =#**+ **     -=--====:                                                  -*-.  ..:++.  -+=:.  .:-++.  *+             
     @- *********#:.******* :#******#- ***+ =***.:@      #*..::::#+                    =.                           *=        +- ++.         -*: +=             
     +% =********#..*******.:#********..*** -*#- @-      #+      :@. .::-:.   .:---.  :%+:. .::-: :   .--. .::::    -*-:..      -#            =* +=             
     .@:.********* :#****** -#********* :#* :#= #+       #*:::::-#= ++-::-*- =*:..:*= -#+::*=:::-+% =%=--.+=:..-*:   .--=====-: =*            :*.+=             
      +% =#*******..#****#: ***********+ :* -+ *#        ##----=-. +*     .%.-*-::.:.  #: *+     :% =#   +#::::.=#  .     ..:-*--*.           -* +=             
       %= ********+ -##*#= +************+ ..- +*         #+        +*     .%....::-+*  #- *+     -% =*   **.....:- :#:        -#.++          .*- +=             
       :@.:#******#*  :=+ :***************.  *@::-=+-    #*        .*=:.:-*= ++....=*  *+:.++-:-=+% =*   .*-...-*-  =*-..    :*=  =+-...   :=*:  *+.........    
        +% -#****#*:.+*=  :.-************-::.--==:.=@:   ..          :---:.   :----:    ::.-..:. -# ..     :---:     :-======-.    .-=======-=+: -=------=--    
         *# :*##*- -##*=.=#= +**********= -++--:. -#+                                      *+--:-+:                                           ..                
          +%:.--.:*: .:-+=:  =*********#- ----=+*##-                                         ..:.                                                               
           -#*+++*@*==----+* =*********#::@====-:.                                                                                                              
             .:-.  :--===-*% =********** =#                                                                                                                     
                          =@ =*********+ #+                                                                                                                     
                          -@ -#*******#= %-                                                                                                                     
                          :@.:#*******#.:@.                                                                                                                     
                           @* =#####**: %+                                                                                                                      
                           -@+.:----::=%+                                                                                                                       
                            :*#*++++**=.                                                                                                                        
                               .:::. 
```

Postgresql
-----------

> The most technologically advanced relational database ever created.

Postgresql is one of the many "traditional" databases available on the market, it was the second most popular
database, and by coincidence it was written by the same programmers who created both MySQL and MariaDB.
Although configuration of Postgresql is different than MySQL/MariaDB, it accepts nearly the exact same syntax
as MySQL/MariaDB, but it is slightly more resource heavy than the other two.

For a while there, installation and configuration of Postgresql was a breeze up until a few years ago. It was
then when the Postgresql took on a new design objective, and this was to target database clusters. In order to
target these large database clusters Postgresql has to implement strict version adherence and database
isolation. The benefit to this strategy is it allowed large scale database systems of 100 or more database
servers to run and manage several different versions of Postgresql at one time, the drawback is it created
previously nonexistent obstacles for systems administrators to go through in order to upgrade their database
from one version to the next. As one can guess, these new obstacles resulted in Postgresql becoming less commonly
encountered outside a corporate or academic environment.

### Installation

Installation can be easily achieved through the use of the whatever distrobution package manager your system
uses, but after the initial install things will increase in initial complication. 

For the remainder of this page, we will assume the user is using a Debian derivative system. This is mentioned
as a precaution, because although other linux systems might be identically structured, the following
information isn't precise for those systems, and should be treated as a mere estimation.

#### Post Installation

Your next step is to discover what version of Postgresql you are using. You can easily discover this by
running `sudo pg_config --version` and this should output a string like this `PostgreSQL 16.3 (Debian 16.3-1+b1)`,
which clearly says our version is "16.3". 

##### Add to path

It is rather inconvenient to write the full path to a binary everytime you go to execute it, so to make this
easier we will need to add the location of PostgreSQL's binaries to our path.
