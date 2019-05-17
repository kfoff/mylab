#!/bin/bash

apt install -y fail2ban
apt install -y rsync
apt install -y net-tools
apt install -y python3-pip
apt install -y python3-venv

pip3 install virtualenv

chmod 600 /etc/rsyncd.secrets

ufw enable
ufw allow 22
ufw allow from 62.109.29.220 to any port 873
ufw deny 873