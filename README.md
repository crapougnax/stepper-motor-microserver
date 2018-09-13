# Stepper Motor Microserver for Raspberry Pi

A Python microserver to command 4 (or more) stepper motors

## Installation

### Install packages

```
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip python-virtualenv
```

### Configure Python Virtual Env

```
python3 -m venv venv
virtualenv venv
. venv/bin/activate
```

### Install Flask

```
pip install flask
```

### Install Adafruit drivers
```
git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
cd Adafruit-Motor-HAT-Python-Library/
sudo ../venv/bin/python setup.py install
```

## Start

```
./start-server.sh
```

## Usage

```
http://raspberrypi.local:5000/forward/4/50
```

PATH FORMAT = `/<direction>/<motor_id>/<steps>`
