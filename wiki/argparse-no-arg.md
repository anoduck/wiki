```text
#     _              ____
#    / \   _ __ __ _|  _ \ __ _ _ __ ___  ___
#   / _ \ | '__/ _` | |_) / _` | '__/ __|/ _ \
#  / ___ \| | | (_| |  __/ (_| | |  \__ \  __/
# /_/   \_\_|  \__, |_|   \__,_|_|  |___/\___|
#              |___/
#
```

# Using argparse without be followed by an argparse statement to process the args.

> [!WARNING]
> There be junk code in these waters. Be careful before diving in.

This may just be a "me" thing, but since I am a self taught programmer I have always used an `If-Then`
statement behind my argparse statement to process the args with the appropriate functions and so on. Taking
this approach becomes quite burdensome when your commands accepts both commands and subcommands. So, I always
knew there had to be a different approach and/or another way of doing this.

Then one day, I ran into a stumbling block where the old approach no longer was viable, and it was time for me
to finally roll up my sleeves to figure out how it is done. Below, is what I came up with.


```python
  """                                                                                                                                                                                                                                                                      
    Main                                                                                                                                                                                                                                                                
    """                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                           
    tprint('Crouching Tiger', font='tarty3')                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                           
    # This script must be run as root!                                                                                                                                                                                                                                     
    if not os.geteuid() == 0:                                                                                                                                                                                                                                              
        sys.exit('Must be root! Damn, Shawty!')                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                           
    prog = os.path.basename(__file__)                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                           
    ##################                                                                                                                                                                                                                                                     
    # config parse   #                                                                                                                                                                                                                                                     
    ##################                                                                                                                                                                                                                                                     
    configp = ConfigParser(defaults=None, dict_type=collections.OrderedDict, allow_no_value=False, delimiters=, '=', ':')                                                                                                                                                  
    config_file = 'config.ini'                                                                                                                                                                                                                                             
    ##################                                                                                                                                                                                                                                                     
    # ArgParse Setup #                                                                                                                                                                                                                                                     
    ##################                                                                                                                                                                                                                                                     
    ap = argparse.ArgumentParser(                                                                                                                                                                                                                                          
        prog=prog,                                                                                                                                                                                                                                                         
        formatter_class=argparse.RawTextHelpFormatter,                                                                                                                                                                                                                     
        usage='%(prog)s -i $IFACE (-t $TARGET or -f $TARGET_FILE)',                                                                                                                                                                                                        
        description='Background scanning of wifi clients and APs, with a trigger.\n'                                                                                                                                                                                       
        '\n'                                                                                                                                                                                                                                                               
        'This program reads from a list of preselected targets, then runs in the background\n'                                                                                                                                                                             
        'and scans if those targets are available. If they are and the signal is strong\n'                                                                                                                                                                                
        'an action is performed on the target(s).\n'                                                                                                                                                                                                                       
        '\n'                                                                                                                                                                                                                                                               
        'There are four types of actions that can be performed:\n'                                                                                                                                                                                                         
        '\n'                                                                                                                                                                                                                                                               
        '1. CAPTURE [cap] = Airodump-ng will begin capturing packets when a target\n'                                                                                                                                                                                      
        '      is found.\n'                                                                                                                                                                                                                                                
        '\n'                                                                                                                                                                                                                                                               
        '2. EXECUTE [exe] = Execute command against target\n'                                                                                                                                                                                                              
        '      This action will execute a command when the target is found.\n'                                                                                                                                                                                             
        '\n'                                                                                                                                                                                                                                                               
        '3. SCRIPT [sh] = Launch script on target\n'                                                                                                                                                                                                                       
        '      This action will execute a script when a target is found.\n'                                                                                                                                                                                                
        '\n'                                                                                                                                                                                                                                                               
        '4. SCAN [scn] = Scan for target\n'                                                                                                                                                                                                                                
        '      This action only scans for the target(s) provided. It does not store any\n'                                                                                                                                                                                 
        '      packets or launch any other commands.\n'                                                                                                                                                                                                                    
        '\n'                                                                                                                                                                                                                                                               
        'The script was created with the intent to allow users to attack wifi targets\n'                                                                                                                                                                                  
        'that are only available some of the time.\n',                                                                                                                                                                                                           
        epilog='ADMISSIONS: There is a far more efficient way to do this.\n'                                                                                        
        '\n',                                                                                                                                                                                                                             
        conflict_handler='resolve')                 
    # options parser
        ap.add_argument('-i', '--interface', dest='interface',
                    required=True, help='Interface(s) to scan on')
    source = ap.add_mutually_exclusive_group(required=True)
    source.add_argument('-t', '--targets', action='extend', dest='tlist',
                        help='A single or comma seperated list of targets.')
    source.add_argument('-f', '--file', dest='tlist',
                        help='File containing targets, one per line.')
    # ap.add_argument('iaction', choices=['cap', 'exe', 'sh', 'scn'],
                    # help='Action to perform on the Target.')
    # Subparser
    subparse = ap.add_subparsers(title='actions', description='Action to perform',
                                required=True, dest='module',
                                help='You must use one.')
    # Rec Subcommands
    rec_parse = subparse.add_parser('cap', help='Capture packets from target')
    rec_parse.add_argument('-o', '--output', dest='output',
                            help='Pcap file to write capture to')
    rec_parse.add_argument('-t', '--time', dest='time',
                            help='Length of time to capture packets')
    rec_parse.set_defaults(fun=scan_cap)

    # Exe Subcommands
    exe_parse = subparse.add_parser('exe', help='Execute command on target')
    exe_parse.add_argument('-c', '--command', dest='command',
                            help='Command to execute on target.')
    exe_parse.add_argument('-l', '--log', required=False, dest='log',
                            help='Log file of the command')
    exe_parse.set_defaults(fun=scan_exe)

    # Sh Subcommands
    sh_parse = subparse.add_parser('sh', help='Perform script on target')
    sh_parse.add_argument('-s', '--script', dest='script',
                        help='Path to the script to run against the target.')
    sh_parse.set_defaults(fun=scan_sh)

    # scn Subcommands
    scn_parse = subparse.add_parser('scn', help='Scan for target')
    scn_parse.add_argument('-r', '--rfile', dest='rfile',
                            default='results.txt',
                            help='File to write results too.')
    scn_parse.set_defaults(fun=scan_scn)

    ##################
    # parse the args #
    ##################
    args = ap.parse_args(args=None if sys.argv[1:] else ['--help'])
    process_args(args)


# This is some fancy shit.
def process_args(args: argparse.Namespace):
    match args.module:
        case "cap":
            scan_cap(args.interface, args.tlist, args.output, args.time)
        case "exe":
            scan_exe(args.interface, args.tlist, args.command, args.log)
        case "sh":
            scan_sh(args.interface, args.tlist, args.script)
        case "scn":
            scan_sh(args.interface, args.tlist, args.rfile)


if __name__ == '__main__':
    main()
```
