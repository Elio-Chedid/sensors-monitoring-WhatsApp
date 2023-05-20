import time
import board
import adafruit_dht


import requests
api_url = "http://127.0.0.1:5000/bot"
incoming_msg = ""
def monitor_dht11():
    dhtDevice = None

    try:
        dhtDevice = adafruit_dht.DHT11(board.D25)

        while True:
            try:
                dhtDevice = adafruit_dht.DHT11(board.D25, use_pulseio=False)
                temperature_c = dhtDevice.temperature
                
                print(temperature_c)
                with open("/home/kali/IOTproj/temp.txt",'w')as tmp:
                    tmp.writelines(str(temperature_c))
                
                if temperature_c>38.0:
                    incoming_msg="Alert! high temperature"
                    payload = {'Body': incoming_msg.strip()}

                    try:
                        response = requests.post(api_url, params=payload)

                        if response.status_code == 200:
                            print(response.text)
                        else:
                            print(f"Request failed with status code {response.status_code}")
                    except requests.RequestException as e:
                        print(f"An error occurred: {e}")

                dhtDevice.exit()
                time.sleep(4.0)

            except KeyboardInterrupt:
                break
            except RuntimeError as error:
                time.sleep(2.0)  
    finally:
        if dhtDevice is not None:
            dhtDevice.exit()  





if __name__ == '__main__':
    monitor_dht11()
