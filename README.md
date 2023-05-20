# WhatsApp Bot with Raspberry Pi Integration

This project implements a WhatsApp bot that interacts with users and performs various actions using the Twilio API and Raspberry Pi. The bot can execute Python code snippets, control lights, monitor temperature, and check the water level. It utilizes Flask as a web framework, the Twilio library for WhatsApp integration, and RPi.GPIO for Raspberry Pi GPIO control.

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.x
- Flask
- requests
- twilio
- RPi.GPIO
- adafruit_dht
- gpiozero

Install the required packages using pip:

```
pip install Flask requests twilio gpiozero adafruit_dht
```

## Configuration

To use the WhatsApp bot, you need to configure your Twilio account credentials:

1. Sign up for a [Twilio](https://www.twilio.com/) account if you haven't already.
2. Replace the placeholders `ENTER SID FROM TWILIO` and `ENTER TOKEN` in the `main.py` file with your Twilio account SID and token, respectively.

Additionally, for the Raspberry Pi components:

- Connect a PIR motion sensor to GPIO 23.
- Connect a buzzer to GPIO 24.
- Connect a DHT11 temperature and humidity sensor to GPIO 25.
- Connect a water level sensor to an available serial port on the Raspberry Pi (e.g., `/dev/ttyACM0`).

## Usage

1. Start the Flask application by running the `main.py` script:

```
python main.py
```

2. Make sure the Flask app is running and accessible from the internet or using ngrok if testing locally.

3. Set up a Twilio Sandbox for WhatsApp using the guide provided by Twilio. Configure the WhatsApp Sandbox to forward incoming messages to the Flask app URL.

4. Send messages to the configured Twilio phone number on WhatsApp to interact with the bot. Available commands include:

- `#!python3` followed by a Python code snippet to execute the code.
- `!pip install <package-name>` to install a Python package.
- `turn on lights` to turn on the connected lights.
- `turn off lights` to turn off the connected lights.
- `show water level` to get the current water level.
- `show temperature` to get the current temperature.

## Motion Detection

The `motiondetection.py` script detects motion using a PIR motion sensor and sends an alert to the WhatsApp bot. It relies on the Flask application being up and running. You need to set up the necessary GPIO connections for the motion sensor.

Run the script as follows:

```
python motiondetection.py
```

## Temperature Monitoring

The `temperature.py` script monitors the temperature using a DHT11 sensor connected to the Raspberry Pi and sends an alert to the WhatsApp bot when the temperature exceeds a threshold. Ensure the DHT11 sensor is properly connected to GPIO 25.

Run the script as follows:

```
python temperature.py
```

## Water Level Monitoring

The `waterlevel.py` script monitors the water level using a water level sensor connected to the Raspberry Pi's serial port. It sends an alert to the WhatsApp bot when the water level falls below a certain threshold. Connect the water level sensor to an available serial port (e.g., `/dev/ttyACM0`).

Run the script as follows:

```
python waterlevel.py
```

## Customizing and Extending

Feel free to customize and extend the functionality of the bot according to your needs. You can modify the commands, add more sensors, or include additional actions based on your specific requirements.

## Disclaimer



Make sure to follow proper safety guidelines and handle electrical components with caution when working with Raspberry Pi and GPIO.

---
