import os
import time
import ctypes
import logging
import requests
import subprocess

from requests import get
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

network_adapter = 'Ethernet'

xfinity_prefixes = ["24.0", "24.16", "24.30", "24.34", "24.60", "24.91",
"24.98", "24.118", "24.125", "24.126", "24.128", "24.129", "24.130", "24.147",
"24.218", "24.245", "50.128", "65.96", "66.30", "66.41", "66.56", "66.176",
"66.229", "67.160", "67.176", "67.180", "67.184", "68.32", "68.80", "68.84",
"69.136", "69.138", "69.139", "69.140", "69.180", "69.242", "69.244", "69.248",
"65.34.128", "69.253", "69.254 ", "71.56", "71.192", "71.224", "73.", "75.64",
"75.72", "75.74", "75.75", "75.75", "76.16", "76.97", "76.98", "76.100",
"76.104", "76.112", "98.192", "98.200", "98.204", "98.206", "98.208", "98.224",
"98.240", "98.242", "98.244", "98.248", "107.2", "107.4", "174.48"]

def welcome():
    stamp = str(datetime.now())
    print('############################')
    print('###  VPN-Killswitch 1.0  ###')
    print('### Created by DannyVoid ###')
    print('############################')
    print('\nStarted at %s' % (stamp))
    print('-------------------------------------\n')

def check_if_vpn():
    try:
        ip = get('https://api.ipify.org').text

        if ip.startswith(tuple(xfinity_prefixes)):
            stamp = str(datetime.now())
            print('VPN Error! - %s' % (stamp))
            subprocess.call('netsh interface set interface %s DISABLED' % (str(network_adapter)))

        else:
            stamp = str(datetime.now())
            print('VPN Enabled! - %s' % (stamp))

    except requests.ConnectionError:
        stamp = str(datetime.now())
        print('Network Offline. - %s' % (stamp))

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_if_vpn, 'interval', seconds=10)
    scheduler.start()
    welcome()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
