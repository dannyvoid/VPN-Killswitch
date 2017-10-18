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

Edit line 13 of **start.bat** to cd to the correct path of your VPN-Killswitch.

Replace **Ethernet** on line 14 of **disable_adapter.bat** and line 13 of **enable_adapter.bat** with the name of your primary adapter.


## To-do

* Have actual error handling.
* Remove the use of .bat files.
* Work with more ISPs.

## Built With

* Python 3
* apscheduler

## Authors

* **DannyVoid**
