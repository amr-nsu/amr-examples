#!/bin/sh

HEX=${PWD##*/}.hex
if [ "$1" ]; then
    HEX="$1"
fi

BOOTLOADERPATH=../../mdrbootstrap

$BOOTLOADERPATH/mdrbootstrap -s 115200 -d /dev/ttyUSB0 -b $BOOTLOADERPATH/1986_BOOT_UART.hex -f $HEX
