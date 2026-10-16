#!/bin/bash
set -euo pipefail

sudo apt install -y build-essential libssl-dev libffi-dev python3-dev python3-tk
sudo python3 -m pip uninstall -y pip && sudo apt install -y python3-pip --reinstall
sudo pip3 install -r requirements.txt
sudo python3 main.py