#!/bin/sh
sudo apt-get update
sudo apt-get install python3-pyqt5.qtmultimedia
sudo apt-get install libqt5multimedia5-plugins
sudo apt-get install python3-self
sudo apt-get install pyqt5.Qtsql
sudo apt-get install python3-pyqt5
sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
sudo apt-get install xinput-calibrator
sudo apt-get install qtcreator
sudo update-rc.d ssh defaults
sudo systemctl enable ssh.socket
sudo systemctl enable ssh.service
sudo service ssh start
sudo service ssh status
git clone https://github.com/waveshare/LCD-show.git
cd LCD-show/
chmod +x LCD5-show
./LCD5-show


