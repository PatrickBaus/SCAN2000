[![Build manufacturing files](https://github.com/PatrickBaus/SCAN2000/actions/workflows/ci.yml/badge.svg)](https://github.com/PatrickBaus/SCAN2000/actions/workflows/ci.yml)
# Keithley 2000-SCAN SSR Replacement

This repository contains the KiCAD PCB project files for a [Keithley Model 2000-SCAN](https://download.tek.com/manual/2000SCAN-901-01_F-Jan-2014.pdf) replacement card. It uses solid-state relays instead of mechanical relays. See [below](#introduction) for a list of compatible devices. The design files can be found on the [releases](../../releases) page.

![SCAN2000 board](images/pcb.png)

## Contents
- [Introduction](#introduction)
- [Design Files](#design-files)
- [Installation](#installation)
- [Accesories](#accesories)
- [Related Repositories](#related-repositories)
- [Versioning](#versioning)
- [License](#license)

## Introduction
The design is the successor of the SCAN2000 STM32 board previously released as [v1.x](https://github.com/PatrickBaus/SCAN2000/tree/v1). Instead of an STM32 microcontroller it uses an [iCE40](https://www.latticesemi.com/iCE40) FPGA to emulate the shift registers found on the 10 channel [Model 2000-SCAN](https://download.tek.com/manual/2000SCAN-901-01_F-Jan-2014.pdf) card and is also capable of decoding the protcol used by the 20-channel [Model 2000-SCAN-20](https://download.tek.com/manual/2000-20-901-01C_Jul2003_Instruction.pdf). The advantage of the FPGA is that the shift registers are implemented in hardware. The protocol spoken by the 10 channnel card requires freezing 24 bits clocked in _before_ the strobe bin is triggered, similar to the positive lookahead assertion of a [regular expression](https://en.wikipedia.org/wiki/Regular_expression). This is in stark contrast to typical protocols used by microcontrollers like, for example, [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface) that uses a [chip select](https://en.wikipedia.org/wiki/Chip_select) control line to announce incoming data arriving _after_ the CS signal. A more detailed analysis of the problem can be found in the [doc/serial_protocol](doc/serial_protocol) folder.

The card was tested in a [Keithley DMM6500](https://www.tek.com/en/products/keithley/digital-multimeter/dmm6500) and a [Keithley Model 2002](https://www.tek.com/en/products/keithley/digital-multimeter/2002-series) in both configurations as a 10 channel and 20 channel card. The more recent [Keithley DMM6500](https://www.tek.com/en/products/keithley/digital-multimeter/dmm6500) supports both the older 10 channel [Model 2000-SCAN](https://download.tek.com/manual/2000SCAN-901-01_F-Jan-2014.pdf) and the newer [Model 2000-SCAN-20](https://download.tek.com/manual/2000-20-901-01C_Jul2003_Instruction.pdf) 20 channel scanner card. The same goes for the [Model 2000](https://www.tek.com/en/products/keithley/digital-multimeter/keithley-2000-series-6-digit-multimeter-scanning) and Model 2000-20. The Model 2000-20 is similar to the [Model 2000](https://www.tek.com/en/products/keithley/digital-multimeter/keithley-2000-series-6-digit-multimeter-scanning), but has a different firmware. The latest firmare of the [Model 2000](https://www.tek.com/en/products/keithley/digital-multimeter/keithley-2000-series-6-digit-multimeter-scanning) seems to support the 20 channel cards as well as suggested [here](https://www.eevblog.com/forum/circuit-studio/example-project-20-channel-solid-state-scan-card-for-k2000-dmm/msg3101128/#msg3101128). The [Model 2002](https://www.tek.com/en/products/keithley/digital-multimeter/2002-series) only supports 10 channel cards.

|DMM|Tested|Note|
|--|--|--|
|[DMM6500](https://www.tek.com/en/products/keithley/digital-multimeter/dmm6500)|:heavy_check_mark:|Works.|
|[2000](https://www.tek.com/en/products/keithley/digital-multimeter/keithley-2000-series-6-digit-multimeter-scanning)|:x:|Not tested, but should work. The latest firmware seems to support [20 channels](https://www.eevblog.com/forum/circuit-studio/example-project-20-channel-solid-state-scan-card-for-k2000-dmm/msg3101128/#msg3101128).|
|[2000-20](https://www.tek.com/en/products/keithley/digital-multimeter/keithley-2000-series-6-digit-multimeter-scanning)|:x:|Not tested, but should work.|
|[2010](https://www.tek.com/en/products/keithley/digital-multimeter/2010-series)|:heavy_check_mark:|Works, but only 10 channels cards are supported by the firmware.|
|[2001](https://www.tek.com/en/products/keithley/digital-multimeter/2001-series)|:x:|Not tested, but should work.|
|[2002](https://www.tek.com/en/products/keithley/digital-multimeter/2002-series)|:heavy_check_mark:|Works. Only 10 channels supported.|

## Design Files
The root folder contains the KiCAD files. The bill of materials can be found on the [releases](../../releases) page along with Gerber files for production.

## Installation
The source code for the FPGA and the installation instructions for the firmware can be found [here](https://github.com/PatrickBaus/SCAN2000_iCE40_Firmware). The FPGA source code must be written to the onboard SPI flash chip. One way to do so is to use an USB to SPI converter with an FT232H chip.

The SCAN2000 SSR board has two solder jumpers, ```JP1``` and ```JP2```. To enable only 10 channels close ```JP2``` and connect the two left pads of ```JP1``` together using a soldering iron. To enable 20 channel operation, leave ```JP2``` open and connect the two rightmost pads of ```JP1```.

The assembled card can then wired up and simply inserted into the multimeter. It will be supplied by the DMM through the Molex connector. To connect the scanner outputs to the, connect the screw terminals labeled ```Input``` to the DMM terminals labeled ```Input```. The same goes for the ```Sense``` terminals if operating in 4-wire mode.

## Accesories
The [Model 2000-SCAN](https://download.tek.com/manual/2000SCAN-901-01_F-Jan-2014.pdf) comes with 4 10″ connectors that have a right angle 4mm connector on one side and a tinned wire on the other. They are sold by Keithley as [CA-109A](https://download.tek.com/document/1KW-50660-1_Keithley_Test_Leads_Probes_Selector_Guide_100622.pdf) and are made by Mueller Electric. Their part numbers are [BU-0062-N-108-2 (red)](https://www.muellerelectric.com/products/bu-0062-n-108-2) and [BU-0062-N-108-0 (black)](https://www.muellerelectric.com/products/bu-0062-n-108-0). Keithley shortens the Mueller Electric parts to 10″. The same length is fine for this board as well.

## Related Repositories
See the following repositories for more information as these are part of the [design files](#design-files).

- [KiCad footprints](https://github.com/PatrickBaus/footprints.pretty)
- [KiCAD 3D models](https://github.com/PatrickBaus/footprints.3dshapes)
- [KiCAD schematic libraries](https://github.com/PatrickBaus/KiCad-libraries)

## Versioning
I use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags](../../tags) available for this repository.

- MAJOR versions in this context mean a breaking change to the external interface of the hardware like different connectors or functions.
- MINOR versions contain changes to the hardware that only affect the inner workings of the circuit, but otherwise the performance is unaffected.
- PATCH versions do not affect the schematics or invalidate older bill of materials. These changes may include updated components (to replace obsolete parts for example), an updated silkscreen, or fixed typos.

## License
This work is released under the CERN-OHL-W
See [https://ohwr.org/cern_ohl_w_v2.pdf](https://ohwr.org/cern_ohl_w_v2.pdf) or the included LICENSE file for more information.
