# VPN-Killswitch

Disables your primary network adapter if you're using an xfinity IP address. Checks every 5 seconds.

## Getting Started

This will get you up and running

### Prerequisites

* Python 3
* apscheduler via [pip](http://pypi.python.org/pypi/pip)

```
pip install apscheduler
```

### Config

* Edit lines 12-19 of **app.py**.

```python
adapter = 'Ethernet'                    # name of your primary network adaptor
socket_url = 'www.google.com'           # don't change
ip_url = 'https://api.ipify.org'        # don't change
vpn_interval = 1                        # interval in seconds
off_interval = 30                       # interval in minutes
auto_reboot = True                      # restarts machine if offline for an extended period
start_on_boot = False                   # starts VPN-Killswitch on windows startup
debug = True                            # outputs your IP
```

* And finally, run **start.bat** as an administrator.

## To-do

* Work with more ISPs.

## Built With

* Python 3
* apscheduler

## Authors

* **DannyVoid**
