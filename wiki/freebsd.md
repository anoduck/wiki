```text
#  _____              ____ ____  ____
# |  ___| __ ___  ___| __ ) ___||  _ \
# | |_ | '__/ _ \/ _ \  _ \___ \| | | |
# |  _|| | |  __/  __/ |_) |__) | |_| |
# |_|  |_|  \___|\___|____/____/|____/
#
```

## FreeBSD

That other BSD. 

### Working with FreeBSD's gpart

* To show a drive's partition table.`gpart show ada0`
* To delete a partition.`gpart delete -i $PARTITION_NUMBER $DISK`
* Resize a partition. `gpart resize -i $PART_NUM -s $NEW_SIZE -a 4k $DISK`
* create a partition. `gpart add -t $LABEL -a 4k $DISK`
* growfs `growfs /dev/${DEVICE}p${PARTITION_NUMBER}` ex. 'ada0p3'

#### What is difficult

How to rearrange partitions without corrupting data or wasting mor than 512MB? You have:
1. boot = >1Mb
2. efi = >=35m
3. swap = 1g
4. root = 45g

Swap is reportedly too small for you to complete building packages, but to enlargen your swap you will need to
shrink the last partition ("4") that is used for mounting the root filesystem. 

##### Feasible solution

The only feasible solution is to allow 1G of memory go to waste. Reduce the size of the root parition ("4"),
and add a swap partition behind it, consuming the remaining disk space after reduction.
