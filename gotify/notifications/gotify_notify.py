#!/usr/bin/env python3

# sudo apt install python3 python3-pip
# chmod +x <filename>

# crontab command
# @reboot /home/bisina/scripts/gotify_notify.py


import requests #pip install requests

resp = requests.post('http://10.10.10.134:8080/message?token=ApEV6PB4iIfwS_p', json={
    "title": "Ubuntu Login",
    "message": "Ubuntu Server Login Successful BISI-UBSER02-DOK",
    "priority": 5
})