import os
import os.path
import socket
import subprocess
import time

from datetime import datetime
from requests import get

from apscheduler.schedulers.background import BackgroundScheduler

adapter = 'Ethernet'                    # name of your primary network adaptor
socket_url = 'www.google.com'           # don't change
ip_url = 'https://api.ipify.org'        # don't change
vpn_interval = 1                        # interval in seconds to check your vpn state
off_interval = 30                       # interval in minutes to check if your machine needs to reboot
auto_reboot = True                      # restarts machine if offline for an extended period
start_on_boot = False                   # starts VPN-Killswitch on windows startup
debug = True                            # outputs your IP

xfinity_prefixes = ['24.0', '24.16', '24.30', '24.34', '24.60', '24.91',
                    '24.98', '24.118', '24.125', '24.126', '24.128', '24.129', '24.130', '24.147',
                    '24.218', '24.245', '50.128', '65.96', '66.30', '66.41', '66.56', '66.176',
                    '66.229', '67.160', '67.176', '67.180', '67.184', '68.32', '68.80', '68.84',
                    '69.136', '69.138', '69.139', '69.140', '69.180', '69.242', '69.244', '69.248',
                    '65.34.128', '69.253', '69.254 ', '71.56', '71.192', '71.224', '73.', '75.64',
                    '75.72', '75.74', '75.75', '75.75', '76.16', '76.97', '76.98', '76.100',
                    '76.104', '76.112', '98.192', '98.200', '98.204', '98.206', '98.208', '98.224',
                    '98.240', '98.242', '98.244', '98.248', '107.2', '107.4', '174.48']


def motd():
    print('############################')
    print('###  VPN-Killswitch 2.5  ###')
    print('### Created by DannyVoid ###')
    print('############################')
    print('\nStarted at {}'.format(str(datetime.now())))
    print('-------------------------------------\n')
    handle_startup()


def is_online():
    try:
        socket.create_connection((socket_url, 80))
        return True
    except Exception:
        pass
    return False


def vpn_check():
    if is_online():
        try:
            ip = get(ip_url).text
            if ip.startswith(tuple(xfinity_prefixes)):
                print('{} - VPN Not Detected!'.format(str(datetime.now())))
                subprocess.call('netsh interface set interface {} DISABLED'.format(adapter),
                                stdout=open(os.devnull, 'wb'))
                if debug:
                    print('{} - {}'.format(str(datetime.now()), ip))
            else:
                print('{} - VPN Working!'.format(str(datetime.now())))
                if debug:
                    print('{} - {}'.format(str(datetime.now()), ip))
        except Exception:
            pass
    else:
        print('{} - Network Offline!'.format(str(datetime.now())))


def reboot_if_offline():
    if auto_reboot:
        if not is_online:
            print('{} - Machine has been offline for {} minutes.'.format(str(datetime.now()), str(off_interval)))
            print('{} - Rebooting in 60 seconds!'.format(str(datetime.now())))
            subprocess.call('shutdown -t 60 -r -f', stdout=open(os.devnull, 'wb'))
        else:
            print('{} - Checking for errors again in {} minutes.'.format(str(datetime.now()), str(off_interval)))
            pass
    else:
        pass


def handle_startup():
    current_dir = os.getcwd()
    startup_dir = 'C:/Users/{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'.format(os.getlogin())
    filename = 'VPN-Killswitch.bat'

    if start_on_boot:
        with open(os.path.join(startup_dir, filename), 'w') as batch:
            batch_file = (
                '@echo off\n\n'

                'NET SESSION >NUL\n'
                'IF %ERRORLEVEL% NEQ 0 GOTO ELEVATE >NUL\n'
                'goto :start\n\n'

                ':ELEVATE\n'
                'CD /d %~dp0\n'
                'MSHTA \"javascript: var shell = new ActiveXObject(\'shell.application\');'
                'shell.ShellExecute(\'%~nx0\', \'\', \'\', \'runas\', 1);close();\" >NUL\n'
                'EXIT\n\n'

                ':start\n'
                'cd /d "{}"\n'
                'ping -n 30 -w 1 127.0.0.1>nul\n'
                'python3 app.py\n\n'.format(current_dir)
            )
            batch.write('{}'.format(batch_file))
    else:
        try:
            os.remove(os.path.join(startup_dir, filename))
        except OSError:
            pass


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(vpn_check, 'interval', seconds=vpn_interval)
    scheduler.add_job(reboot_if_offline, 'interval', minutes=off_interval)
    scheduler.start()
    motd()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
