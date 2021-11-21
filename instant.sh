#!/bin/sh
sudo apt update
sudo apt install python3 python3-pip python3-dev -y
sudo apt install openssl -y
sudo mkdir /tmp/cahelper
sudo cp ./CAhelper.py /tmp/cahelper/CAhelper.py
cd /tmp/cahelper
sudo python3 CAhelper.py
