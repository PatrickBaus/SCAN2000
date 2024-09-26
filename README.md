[![Build manufacturing files](https://github.com/PatrickBaus/SCAN2000/actions/workflows/ci.yml/badge.svg)](https://github.com/PatrickBaus/SCAN2000/actions/workflows/ci.yml)
# Keithley SCAN2000 SSR Replacement

This repository contains the KiCAD PCB project files for a Keithley SCAN2000 replacement card. It uses solid-state relays instead of mechanical relays. See [below](#introduction) for a list of compatible devices. The design files can be found on the [releases](../../releases) page.

## Contents
- [Introduction](#introduction)
- [Design Files](#design-files)
- [Installation](#installation)
- [Related Repositories](#related-repositories)
- [Versioning](#versioning)
- [License](#license)

![Keithley SCAN2000 board](images/pcb.png)

## Introduction
|DMM|Tested|Note|
|--|--|--|
|[DMM6500](https://www.tek.com/en/products/keithley/digital-multimeter/dmm6500)|:heavy_check_mark:||
|2000|:x:|Not tested, but should work. The latest firmware seems to support [20 channels](https://www.eevblog.com/forum/circuit-studio/example-project-20-channel-solid-state-scan-card-for-k2000-dmm/msg3101128/#msg3101128).|
|2000-20|:x:|Not tested, but should work.|
|[2010](https://www.tek.com/en/products/keithley/digital-multimeter/2010-series)|:x:|Not tested, but should work. [Only 10 channels supported.](https://www.eevblog.com/forum/projects/20-channel-diy-scanner-card-for-keithley-dmms-and-daqs/msg3514228/#msg3514228)|
|[2001](https://www.tek.com/en/products/keithley/digital-multimeter/2001-series)|:x:|Not tested, but should work.|
|[2002](https://www.tek.com/en/products/keithley/digital-multimeter/2002-series)|:heavy_check_mark:|Does not work. The serial clock is 2 MHz, which is too fast for the MCU.|

## Design Files
The root folder contains the KiCAD files. The bill of materials can be found on the [releases](../../releases) page along with Gerber files for production.

## Description
The design is based on the SCAN2000 pcb made by [George Christidis](https://github.com/macgeorge/SCAN2000STM32). It also uses an STM32G0, but the pcb design is done in [KiCAD 8](https://www.kicad.org/) and corrects several problems like incorrect dimensions of the original design and replaces hard to obtain parts like the resistor arrays. The card was tested in a Keithley DMM6500 and a Keithley Model 2002. The latter model is **not** supported by the card.

A photo of a version 1.0.0 board. Note: Later revisions have a pin header instead of the Picoblade connector for programming and the MCU is rotated.
![Keithley SCAN2000 board photo](images/pcb_photo.JPG)

## Installation
The source code and installation instructions can be found [here](https://github.com/PatrickBaus/SCAN2000_Firmware). You will need a ST-Link adapter to flash the MCU.

## Related Repositories
See the following repositories for more information as these are part of the [design files](#design Files).

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
