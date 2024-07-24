```text
 __        __             ____                    _ _                 _
 \ \      / / __   __ _  / ___| _   _ _ __  _ __ | (_) ___ __ _ _ __ | |_
  \ \ /\ / / '_ \ / _` | \___ \| | | | '_ \| '_ \| | |/ __/ _` | '_ \| __|
   \ V  V /| |_) | (_| |  ___) | |_| | |_) | |_) | | | (_| (_| | | | | |_
    \_/\_/ | .__/ \__,_| |____/ \__,_| .__/| .__/|_|_|\___\__,_|_| |_|\__|
           |_|                       |_|   |_|
```

Wpa Supplicant
--------------

If you are running linux and need to connect to a wifi network that has wpa password protection, then you will
need to use the service "wpa_supplicant" to connect to that network. In the past, and still a valid means of
configuration, you would generate a configuration file using the `wpa_passphrase >> file.conf` method, and
then launch wpa_supplicant in the background with `wpa_supplicant -f file.conf`. In an attempt to make this
process easier, while providing users with an overall easier means to configure various aspects of
wpa_supplicant, the shell environment `wpa_cli` was created. Which is now the standard means of configuring
and working with the wpa_supplicant service.

Although the intention of creating `wpa_cli` was to make things easier, it actually involves more steps to
properly configure than before. Which is what will be demonstrated in this wiki page.

### Configuration of WPA Supplicant

Now to properly configure wpa_supplicant and have a persistent connection in the instance you are
disconnected, you have to do a little more elbow work. You will need to create a configuration file for
wpa_supplicant and enable wpa_supplicant to write configured network parameters to this file. For this, open
up your favorite text editor to the file `/etc/wpa_supplicant/wpa_supplicant.conf`, and add the below lines to
create a minimal configuration.

```conf
# wpa_supplicant configuration file
# ---------------------------------

# Designate the primary process 
ctrl_interface=/run/wpa_supplicant

# enable writing conf info to file.
update_config=1
```

Now it is time to start the wpa_supplicant service, with the newly created configuration file, on the desired
interface, and background that process. All of this is done with the command below.

```bash
wpa_supplicant -B -i <$INTERFACE> -c /etc/wpa_supplicant/wpa_supplicant.conf
```

> [!failure] If you recieve: `ctrl_iface exists and seems to be in use`
> This means that a interface lock file has already been created on your system. You will need to delete that
> file before continuing. Which you can do with `sudo rm /run/wpa_supplicant/<$INTERFACE>`. Once that file has
> been deleted then run the above command again, and it should work.

> [!success] If successful you may see `nl80211: kernel reports: match already configured`
> This is perfectly normal, and nothing to worry about, and is to be expected especially if you recieved the
> previous error message.

Now, your all set and ready to get rolling.

### Running wpa_cli

From this point out your pretty much on easy street, and the rest of the configuration will take place using
the `wpa_cli`. Follow the steps below to finish up.

1. Enter the CLI: `wpa_cli`
2. Scan for the network you want to connect to: `> scan`
3. Retrieve the results of the scan: `> scan_results`
4. Add the network you want to connect to: `> add_network`
5. Set network ssid: `> set_network 0 ssid "<$NETWORK>"`
6. Set network passphrase: `> set_network 0 psk "<$PASSPHRASE>"`
7. Enable the network on your system: `> enable_network 0`
8. Save your configuration: `> save_config`
9. Quit the CLI: `> quit`

You should now be connected and surfing good. Please note, when you executed the command `add_network` this
automatically generated a single digit identifier for the network "slot", because there were no previous
configurations, it assigned it the value 0.

