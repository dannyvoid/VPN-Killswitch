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
int_is_vpn = 1                          # interval in seconds to check your vpn state
int_is_stuck = 30                       # interval in minutes to check if your machine needs to reboot
auto_reboot = False                     # restarts machine if offline for an extended period
auto_start = False                      # starts VPN-Killswitch on windows startup
debug = False                           # prints your IP on each check
```

* And finally, run **start.bat** as an administrator.

## To-do

* Work with more ISPs.

## Built With

* Python 3
* apscheduler

## Authors

* **DannyVoid**
