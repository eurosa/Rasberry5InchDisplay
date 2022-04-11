#!/bin/sh
# > means overrite everything
# >> means add new line to existing

echo '
max_usb_current=1
hdmi_group=2
hdmi_mode=87
hdmi_cvt 800 480 60 6 0 0 0
hdmi_drive=1' >> /boot/config.txt
echo '
network={
    ssid="FTTH-5G"
    psk="Digiline@123"
    key_mgmt=WPA-PSK
}' >> /etc/wpa_supplicant/wpa_supplicant.conf


sudo reboot