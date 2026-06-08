# https://www.twilio.com/
from twilio.rest import Client

account_sid = "string"
auth_token = "string"

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="...",
    from_="...",
    body="..."
)
