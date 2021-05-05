# CoWIN Vaccine Availability

### Usage:

```
python3 utils.py [pincode] [duration (in sec)] [freq (in Hz)] [cadence] [sleep_time]
```

- pincode: pincode
- duration: duration of buzzer (buzzes if it finds availability of vaccines in that pincode)
- freq: sound frequency of buzzer
- cadence: the number of times the buzzer is going to buzz
- sleep_time: number of seconds to sleep before running the script again


### Eg:
```
python3 utils.py 410206 1 440 3 60
```