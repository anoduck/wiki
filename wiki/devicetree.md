```text
#  ____             _            _____
# |  _ \  _____   _(_) ___ ___  |_   _| __ ___  ___
# | | | |/ _ \ \ / / |/ __/ _ \   | || '__/ _ \/ _ \
# | |_| |  __/\ V /| | (_|  __/   | || | |  __/  __/
# |____/ \___| \_/ |_|\___\___|   |_||_|  \___|\___|
#
```

## What is a device tree

A device tree is a complete, static data structure which represents and describes the hardware of an
electronic device's PCB board. Device trees inform the kernel about what hardware is available for use.

## File Type Variations

Device trees come in several different variations, each of which possess a distinct set of features.

| File Type   | Extension   | Features                       | Readability|
|:------------|:------------|:-------------------------------|:-----------|
| Static DT   | dts         | Can reference `.dtsi` files    | yes        |
| DT Inclusion| dtsi        | Can be included in `dts` files | yes        |
| DT Blob     | dtb         | Binary compiled device tree    | no         |
| DT Overlay  | dto -> dtbo | Dynamic Hardware Allocation    | no         |


**Device Tree** vs **Device Tree Overlay** — here's the clear difference:

### 1. What is a Device Tree?

A **Device Tree** (DT) is a complete, static description of the hardware on your board.

- It tells the Linux kernel what hardware exists (CPU, memory, peripherals, buses, GPIOs, clocks, etc.).
- It is written in human-readable `.dts` + `.dtsi` files.
- It gets compiled into a binary file called a **Device Tree Blob** (`.dtb`).
- The bootloader (U-Boot, etc.) loads the `.dtb` file **at boot time** and passes it to the Linux kernel.
- Once the kernel boots, the device tree is fixed — you normally cannot change it without rebooting.

This is the **base** device tree. Every board has one.

### 2. What is a Device Tree Overlay?

A **Device Tree Overlay** (DTO) is a **partial** device tree that can be applied **on top of** the base device tree **at runtime** (after the system has already booted).

Think of it like a patch or plugin:
- It can **add** new devices
- It can **modify** existing nodes (change pinmux, enable/disable peripherals, change properties)
- It can be **loaded and unloaded** dynamically without rebooting

Overlays are compiled into **`.dtbo`** files (Device Tree Blob Overlay).

### 3. Side-by-Side Comparison

| Feature                        | Base Device Tree (`.dtb`)                  | Device Tree Overlay (`.dtbo`)                     |
|--------------------------------|--------------------------------------------|---------------------------------------------------|
| **Purpose**                    | Complete hardware description              | Incremental changes / additions                   |
| **When it is applied**         | At boot (by bootloader)                    | After boot (runtime)                              |
| **File extension**             | `.dtb`                                     | `.dtbo`                                           |
| **Can it stand alone?**        | Yes                                        | No — must be applied on top of a base DT          |
| **Compilation flag**           | Usually `dtc -I dts -O dtb`                | Requires `dtc -@` (generates `__symbols__`)       |
| **Syntax**                     | Normal `/ { ... };` tree                   | Uses `/plugin/`, fragments, and `&label {}`       |
| **Modification**               | Requires recompile + reboot                | Can be loaded/unloaded dynamically                |
| **Typical use cases**          | Main board description                     | HATs, capes, FPGA overlays, add-on boards, dynamic pinmux |
| **Kernel config**              | Always needed                              | Requires `CONFIG_OF_OVERLAY=y`                    |

### 4. Simple Overlay Example

Here’s what a typical overlay looks like:

```dts
/dts-v1/;
/plugin/;

/ {
    fragment@0 {
        target = <&i2c1>;           // Target an existing node
        __overlay__ {
            /* Add a new sensor on I2C */
            my_sensor@50 {
                compatible = "vendor,mysensor";
                reg = <0x50>;
            };
        };
    };
};
```

Using **labels** (cleaner, requires the `-@` flag when compiling the base DT):

```dts
/dts-v1/;
/plugin/;

&i2c1 {
    my_sensor@50 {
        compatible = "vendor,mysensor";
        reg = <0x50>;
    };
};
```

### 5. How This Relates to Compilation

From our previous discussion:

- **Base device tree**: Compile normally  
  ```bash
  dtc -I dts -O dtb -o board.dtb board.dts
  ```

- **Overlay**: You **must** use the `-@` flag (both when compiling the base DT **and** the overlay)  
  ```bash
  dtc -@ -I dts -O dtb -o myoverlay.dtbo myoverlay.dts
  ```

The `-@` flag tells `dtc` to generate a `__symbols__` node so the overlay can find and modify nodes in the base tree by label.

### Summary

| Question                        | Answer                                                                 |
|--------------------------------|------------------------------------------------------------------------|
| What is the main device tree?  | The full hardware description loaded at boot                           |
| What is an overlay?            | A runtime patch that modifies or extends the device tree after boot    |
| Do I need overlays?            | Only if you want dynamic hardware changes without rebooting            |
| Can I compile a `.dtsi` as an overlay? | Yes — if it uses overlay syntax, compile it to `.dtbo` with `-@` |

**You cannot directly compile a standalone `.dtsi` file into a `.dtb`** in the normal case.

`.dtsi` files are **include files** (analogous to C `.h` header files). They contain reusable fragments (SoC definitions, common peripherals, etc.) that must be pulled into a complete top-level `.dts` file using:

```dts
/include/ "imx6ull.dtsi"
/include/ "imx6ull-colibri.dtsi"
/include/ "my-custom-board.dtsi"
```

(or the older `#include "..."` syntax in some older files).

### 1. Install the Device Tree Compiler (`dtc`)

```bash
# Debian / Ubuntu
sudo apt update
sudo apt install device-tree-compiler

# Fedora / RHEL
sudo dnf install dtc

# Arch
sudo pacman -S dtc
```

You can also build it from the Linux kernel sources (`scripts/dtc/`) or clone it directly:

```bash
git clone https://git.kernel.org/pub/scm/utils/dtc/dtc.git
cd dtc && make && sudo make install
```

### 2. Compile a `.dts` file that includes your `.dtsi` files (Recommended)

```bash
dtc -I dts -O dtb -o myboard.dtb myboard.dts
```

**Useful flags**:

| Flag              | Purpose                                                                 | Common Use Case                     |
|-------------------|-------------------------------------------------------------------------|-------------------------------------|
| `-I dts`          | Input is Device Tree Source                                             | Almost always                       |
| `-O dtb`          | Output Device Tree Blob                                                 | Almost always                       |
| `-o file.dtb`     | Output filename                                                         | Always                              |
| `-i /path`        | Add include search directory                                            | When `.dtsi` files are in subdirs   |
| `-@`              | Generate `__symbols__` node (phandle resolution)                        | **Overlays** (`.dtbo`) and modern DT |
| `-f`              | Force overwrite output file                                             | Scripts / automation                |
| `-W no-xxx`       | Suppress specific warnings                                              | Cleaning noisy builds               |

**Example with include paths and overlay support**:

```bash
dtc -I dts \
    -i ./arch/arm/boot/dts \
    -i ./arch/arm/boot/dts/freescale \
    -O dtb -@ \
    -o my-custom-board.dtb my-custom-board.dts
```

### 3. Compiling Overlays (`.dtbo` from `.dtsi` or `.dts`)

If your file is an **overlay fragment** (starts with `/plugin/ { ... };` or uses `&node { ... };` overrides), you can often compile it directly:

```bash
dtc -@ -I dts -O dtb -o myoverlay.dtbo myoverlay.dtsi
# or
dtc -@ -I dts -O dtb -o myoverlay.dtbo myoverlay.dts
```

The `-@` flag is usually required for overlays.

### 4. Best Way: Use the Linux Kernel Build System

When working inside the kernel tree (recommended for real boards), let the Makefile handle includes:

```bash
# After configuring the kernel
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- myboard.dtb

# Or build all device trees
make dtbs
```

The kernel’s build system automatically sets up all the correct `-i` include paths and uses the version of `dtc` from `scripts/dtc/`.

### 5. Decompile (reverse) a `.dtb` back to `.dts`

```bash
dtc -I dtb -O dts -o myboard.dts myboard.dtb
```

Or use the more verbose `fdtdump`:

```bash
fdtdump myboard.dtb > myboard-dump.dts
```

### Quick Checklist / Common Pitfalls

- **Missing includes** → Use `-i /path/to/dts` or work inside the kernel tree.
- **Phandle / label errors** → Add the `-@` flag.
- **Syntax errors** → `dtc` gives reasonably good error messages with line numbers.
- **Unit address vs reg warnings** → Usually harmless; suppress with `-W no-unit_address_vs_reg` if needed.
- **Overlays not applying** → Almost always missing `-@` during compile.