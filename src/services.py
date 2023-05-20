import os
import json
import random
import requests
import board
import adafruit_dht
import RPi.GPIO as GPIO
from gpiozero import LED


def monitor_dht11():
    with open("temp.txt",'r') as tmp:
        temperature_c=tmp.read()
    return temperature_c

def turnOnLight():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(2,GPIO.OUT)
    GPIO.output(2,GPIO.HIGH)
    return "lights on"    
def turnOffLights():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(2,GPIO.OUT)
    GPIO.output(2,GPIO.LOW)
    return "lights off"
def waterLevel():
    with open("level.txt","r") as lvl:
        out=lvl.read()
    return out

    

