```txt
#  ____  _           _____     _        __     __
# |  _ \(_)_ __   __|_   _|_ _| |__     \ \   / /
# | |_) | | '_ \ / _ \| |/ _` | '_ \ ____\ \ / /
# |  __/| | | | |  __/| | (_| | |_) |_____\ V /
# |_|   |_|_| |_|\___||_|\__,_|_.__/       \_/
#
```

# PineTab-V: PineTab on RISCV64

This is a small introduction to getting the pinetab-v to boot NetBSD. 

```bash
jh7110-starfive-pinetab-v.dtb
```

```bash
setenv bootcmd "load mmc 1:3 ${fdt_addr_r} dtb/starfive/jh7110-starfive-pinetab-v.dtb; load mmc 1:3 ${kernel_addr_r} EFI/BOOT/bootriscv64.efi; bootefi ${kernel_addr_r} ${fdt_addr_r}"
saveenv
```

Error recieved: `EQOS_DMA_MODE_SWR stuckFAILED: -110EQOS_DMA_MODE_SWR stuckFAILED: -110net0: cannot init. interface (status=8000000000000007)`

```bash
setenv bootcmd "load mmc 1:3 ${fdt_addr_r} dtb/starfive/jh7110-starfive-pinetab-v.dtb; fdt addr ${fdt_addr_r}; fdt rm /soc/ethernet@16030000; load mmc 1:3 ${kernel_addr_r} EFI/BOOT/bootriscv64.efi; bootefi ${kernel_addr_r} ${fdt_addr_r}"
saveenv
```

```bash
setenv bootcmd "load mmc 1:3 ${fdt_addr_r} dtb/starfive/jh7110-starfive-pinetab-v.dtb; fdt addr ${fdt_addr_r}; fdt rm /soc/ethernet@16030000; fdt rm /soc/ethernet@16040000; fdt rm /soc/pcie@940000000; \
fdt set /soc/i2s@16010000 status disabled; fdt set /soc/i2s@16020000 status disabled; fdt set /soc/spi@16050000 status disabled; fdt set /soc/spi@16060000 status disabled; load mmc 1:3 ${kernel_addr_r} EFI/BOOT/bootriscv64.efi; \
bootefi ${kernel_addr_r} ${fdt_addr_r}"
saveenv
```

fdt rm /soc/ethernet@16030000; \
fdt rm /soc/ethernet@16040000; \
fdt rm /soc/pcie@940000000; \
