import requests
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import RPi.GPIO as GPIO

from src.pythonREPL import execute_python, install_package
import src.services as services

app = Flask(__name__)
sid="ENTER SID FROM TWILIO"
token="ENTER TOKEN"
client = Client(sid,token)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip()
    isPythonCode = False
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg.startswith('#!python3'):
        code = incoming_msg.lstrip('#!python3')
        output = execute_python(code)
        msg.body(output)
        isPythonCode = True

    elif incoming_msg.startswith('!pip install'):
        package = incoming_msg.split()[-1]
        output = install_package(package)
        msg.body(output)
        isPythonCode = True

    if isPythonCode:
        return str(resp)

    incoming_msg = incoming_msg.lower()

    if "turn on lights" in incoming_msg:
        output = services.turnOnLight()

    elif "turn off lights" in incoming_msg:
        output = services.turnOffLights()
    elif "show water level" in incoming_msg:
        output = services.waterLevel()
    elif "show temperature" in incoming_msg:
        output = services.monitor_dht11()
     

    else:
        output=incoming_msg
    message=client.messages.create(to="whatsapp:[YOUR NUMBER]", from_="whatsapp:[NUMBER GIVEN BY TWILIO]", body=output)
    return jsonify({"message":output})



if __name__ == '__main__':
        app.run()
