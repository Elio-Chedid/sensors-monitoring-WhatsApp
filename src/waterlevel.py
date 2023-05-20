#!/usr/bin/env python3
from time import sleep
import serial
import requests
api_url = "http://127.0.0.1:5000/bot"
incoming_msg = ""
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            with open("/home/kali/IOTproj/level.txt",'w') as lvl:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                lvl.writelines(line)
            if float(line)<100:
                incoming_msg="Alert! water level too low"
                payload = {'Body': incoming_msg.strip()}

                try:
                    response = requests.post(api_url, params=payload)

                    if response.status_code == 200:
                        print(response.text)
                    else:
                        print(f"Request failed with status code {response.status_code}")
                except requests.RequestException as e:
                    print(f"An error occurred: {e}")

        sleep(20)