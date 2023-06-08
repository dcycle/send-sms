#/bin/python
"""Send an SMS. See https://www.twilio.com/docs/sms/quickstart/python.
"""

# Download the helper library from https://www.twilio.com/docs/python/install
import os
import sys
# pylint: disable=E0401
from twilio.rest import Client

if "TWILIO_ACCOUNT_SID" not in os.environ or "TWILIO_AUTH_TOKEN" not in os.environ or "TO_NUMBER" not in os.environ or "FROM_NUMBER" not in os.environ or "MESSAGE" not in os.environ:
    print("[error] TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TO_NUMBER, FROM_NUMBER and MESSAGE environment variables need to exist. Please see README.md.")
    sys.exit(1)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
to_number = os.environ['TO_NUMBER']
from_number = os.environ['FROM_NUMBER']
message = os.environ['MESSAGE']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=message,
                     from_=from_number,
                     to=to_number
                 )

print(message.sid)
