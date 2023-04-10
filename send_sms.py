# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC8450b5db3a8484df19e37fe40b31257a"
auth_token = "40a1e15fe4b9f63d1ee965b07c4a6c2a"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Ürününüz düğün.com'a yüklendi.",
                     from_='+15005550006',
                     to='+15005550010'
                 )

print(message.sid)

