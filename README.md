# Stepper Motor Microserver

A python microserver to command 4 (or more) stepper motors

## Installation
```
sudo apt-get install python-virtualenv
python3 -m venv venv
virtualenv venv
. venv/bin/activate

pip install flask

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

PATH FORMAT = /<direction>/<motor_id>/<steps>
