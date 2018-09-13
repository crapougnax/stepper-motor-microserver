#!/usr/bin/python

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor
from flask import Flask
from flask import render_template

import time
import atexit
import math

motorsQty = 4

motors = {}
app = Flask(__name__)

# get the motor hat id from a motor number (1,2 => 0x60, 3,4 => 0x61)
def getHat(motor_id):
    return int(0x60 + math.floor((motor_id - 1 ) /2))

def getPos(motor_id):
    return 1 if motor_id%2 else 2

def addMotor(motor_id):
    i2c = getHat(motor_id)
    pos = getPos(motor_id)
    app.logger.info("Adding motor #" + str(motor_id))
    app.logger.info('i2c = ' + hex(i2c) + ' @ pos #' + str(pos))
    motor = Adafruit_MotorHAT(i2c).getStepper(200, pos)
    motor.setSpeed(30)
    motors[motor_id] = motor

for m in range(1, motorsQty + 1):
    addMotor(m)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/forward/<int:motor_id>/<int:steps>')
def motor_fwd(motor_id, steps = 100):
    res = motors[motor_id].step(
        steps,
        Adafruit_MotorHAT.FORWARD,
        Adafruit_MotorHAT.DOUBLE
        )
    return render_template('index.html', name=motor_id, steps=steps, direction='forward')

@app.route('/backward/<int:motor_id>/<int:steps>')
def motor_bwd(motor_id, steps = 100):
    res = motors[motor_id].step(
        steps,
        Adafruit_MotorHAT.BACKWARD,
        Adafruit_MotorHAT.DOUBLE
        )
    return render_template('index.html', name=motor_id, steps=steps, direction='backward')
