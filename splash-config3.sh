#!/bin/sh
echo '# Disable the rainbow splash screen
disable_splash=1 
# Set the bootloader delay to 0 seconds. The default is 1s if not specified.
boot_delay=0

# Overclock the raspberry pi. This voids its warranty. Make sure you have a good power supply.
force_turbo=1' >> /boot/config.txt
sudo reboot