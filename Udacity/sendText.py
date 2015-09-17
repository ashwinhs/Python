from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "<Get From Twilio>"
auth_token  = "<Get From Twilio>"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hello Annaji please?! Sending Text to you <3",
    to="+<Your number>",    # Replace with your phone number
    from_="+<Twilio Number>") # Replace with your Twilio number
print message.sid

call = client.calls.create(to="+<Your number>",
                           from_="+<Twilio Number>",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)