"""
Usage: python3 utils.py [pincode] [duration (in sec)] [freq (in Hz)] [cadence]

    pincode: pincode
    duration: duration of buzzer (buzzes if it finds availability of vaccines in that pincode)
    freq: sound frequency of buzzer
    cadence: the number of times the buzzer is going to buzz

Eg: python3 utils.py 410206 1 440 3
    
"""


import requests
import datetime
import json
import sys
import os
import time

def ring(duration = 1, freq = 440, cadence = 1):
    for i in range(cadence):
        os.system('play -nq -t alsa synth {} sine {}'.format(duration/cadence, freq))
        time.sleep(2*(duration/100))


def main(postcode = "410206", age = 22, num_days = 20, 
    duration = 0.2, freq = 440, cadence = 1):


    duration = float(duration)
    freq = int(freq)
    cadence = int(cadence)


    POST_CODE = postcode
    age = age

    # Print details flag
    print_flag = 'Y'

    numdays = num_days


    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
    date_str = [x.strftime("%d-%m-%Y") for x in date_list]

    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(POST_CODE, INP_DATE)
        response = requests.get(URL)
        if response.ok:

            resp_json = response.json()
            # print(json.dumps(resp_json, indent = 1))
            flag = False
            if resp_json["centers"]:
                # ring(duration=duration, freq=freq, cadence=cadence)
                print("Available on: {}".format(INP_DATE))
                if(print_flag=='y' or print_flag=='Y'):
                    for center in resp_json["centers"]:
                        for session in center["sessions"]:
                            if session["min_age_limit"] <= age:
                                print("\t", center["name"])
                                print("\t", center["block_name"])
                                print("\t Price: ", center["fee_type"])
                                print("\t Available Capacity: ", session["available_capacity"])
                                if int(session["available_capacity"]) > 0:
                                    ring(duration=duration, freq=freq, cadence=cadence)

                                if(session["vaccine"] != ''):

                                    print("\t Vaccine: ", session["vaccine"])
                                print("\n\n")
                                
                
                    
            else:
                print("No available slots on {}".format(INP_DATE))

if __name__ == "__main__":
    import sys
    import time
    import pyautogui
    
    """
    Usage: python3 utils.py [pincode] [duration (in sec)] [freq (in Hz)] [cadence]

        pincode: pincode
        duration: duration of buzzer (buzzes if it finds availability of vaccines in that pincode)
        freq: sound frequency of buzzer
        cadence: the number of times the buzzer is going to buzz

    Eg: python3 utils.py 410206 1 440 3
        
    """

    pincode = sys.argv[1]
    duration = sys.argv[2]
    freq = sys.argv[3]
    cadence = sys.argv[4]

    while True:
        main(postcode=pincode,
            duration = duration,
            freq = freq,
            cadence = cadence
            )
        pyautogui.press('shift')
        time.sleep(60)

