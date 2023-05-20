import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR
GPIO.setup(24, GPIO.OUT) #BUzzer
api_url = "http://127.0.0.1:5000/bot"
incoming_msg = ""
try:
    time.sleep(2) 
    while True:

        if GPIO.input(23):
            time.sleep(0.5)
            print("Motion Detected")
            incoming_msg="Alert! motion detected"
            payload = {'Body': incoming_msg.strip()}

            try:
                response = requests.post(api_url, params=payload)

                if response.status_code == 200:
                    print(response.text)
                else:
                    print(f"Request failed with status code {response.status_code}")
            except requests.RequestException as e:
                print(f"An error occurred: {e}")
            time.sleep(5) 
        else:
            print("no motion detected")
        time.sleep(20) 

except:
    GPIO.cleanup()