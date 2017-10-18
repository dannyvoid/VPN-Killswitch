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

* Edit line 13 of **start.bat** to cd to the correct path of your VPN-Killswitch.

```batch
cd "C:\Path\To\Your\VPN-Killswitch\Directory"
```

* Replace **Ethernet** on line 13 of **app.py**.

```python
network_adapter = 'Ethernet'
```

* And finally, run **start.bat** as an administrator.

## To-do

* Have actual error handling.
* ~~Remove the use of .bat files.~~
* Work with more ISPs.

## Built With

* Python 3
* apscheduler

## Authors

* **DannyVoid**
