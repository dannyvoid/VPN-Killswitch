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

* Edit lines 11-16 of **app.py**.

```python
adapter = 'Ethernet'                    # name of your primary network adaptor
socket_test_url = 'www.google.com'      # don't change
check_ip_url = 'https://api.ipify.org'  # don't change
vpn_check_int = 10                      # interval in seconds
offline_check_int = 30                  # interval in minutes
auto_restart = True                     # restarts machine if offline for an extended period
```

* And finally, run **start.bat** as an administrator.

## To-do

* Work with more ISPs.

## Built With

* Python 3
* apscheduler

## Authors

* **DannyVoid**
