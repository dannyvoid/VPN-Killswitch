import os
import socket
import subprocess
import time

from datetime import datetime
from requests import get

from apscheduler.schedulers.background import BackgroundScheduler

network_adapter = 'Ethernet'

xfinity_prefixes = ['24.0', '24.16', '24.30', '24.34', '24.60', '24.91',
                    '24.98', '24.118', '24.125', '24.126', '24.128', '24.129', '24.130', '24.147',
                    '24.218', '24.245', '50.128', '65.96', '66.30', '66.41', '66.56', '66.176',
                    '66.229', '67.160', '67.176', '67.180', '67.184', '68.32', '68.80', '68.84',
                    '69.136', '69.138', '69.139', '69.140', '69.180', '69.242', '69.244', '69.248',
                    '65.34.128', '69.253', '69.254 ', '71.56', '71.192', '71.224', '73.', '75.64',
                    '75.72', '75.74', '75.75', '75.75', '76.16', '76.97', '76.98', '76.100',
                    '76.104', '76.112', '98.192', '98.200', '98.204', '98.206', '98.208', '98.224',
                    '98.240', '98.242', '98.244', '98.248', '107.2', '107.4', '174.48']


def welcome():
    print('############################')
    print('###  VPN-Killswitch 2.0  ###')
    print('### Created by DannyVoid ###')
    print('############################')
    print('\nStarted at {}'.format(str(datetime.now())))
    print('-------------------------------------\n')


def is_online():
    try:
        socket.create_connection(('www.google.com', 80))
        return True
    except Exception:
        pass
    return False


def vpn_check():
    if is_online():
        try:
            ip = get('https://api.ipify.org').text
            if ip.startswith(tuple(xfinity_prefixes)):
                print('{} - VPN Not Detected!'.format(str(datetime.now())))
                subprocess.call('netsh interface set interface {} DISABLED'.format(
                    network_adapter), stdout=open(os.devnull, 'wb'))
            else:
                print('{} - VPN Working!'.format(str(datetime.now())))
        except Exception:
            pass
    else:
        print('{} - Network Offline!'.format(str(datetime.now())))


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(vpn_check, 'interval', seconds=1)
    scheduler.start()
    welcome()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
