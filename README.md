Send SMS using [Twilio](https://www.twilio.com/en-us).
-----

Requirements
-----

* Python3
* A Twilio account SID and auth token

How it works
-----

```
export TWILIO_ACCOUNT_SID=SOME_ACCOUNT
export TWILIO_AUTH_TOKEN=SOME_TOKEN
export TO_NUMBER="+15555555555"
export FROM_NUMBER="+15555555555"
export MESSAGE="Hello World"

pip3 install twilio
python3 ./send_sms.py
```
