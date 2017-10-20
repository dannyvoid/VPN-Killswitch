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

* Replace **Ethernet** with the name of your network adapter on line 11 of **app.py**.

```python
adapter = 'Ethernet'
```

* And finally, run **start.bat** as an administrator.

## To-do

* Work with more ISPs.

## Built With

* Python 3
* apscheduler

## Authors

* **DannyVoid**
