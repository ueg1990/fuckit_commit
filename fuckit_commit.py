'''
This module will send SMS reminders periodically, using Twilio.
The aim is to encourage user to code, commit and push to GitHub everyday
'''

import requests
from twilio.rest import TwilioRestClient

def send_sms():
    '''
    Send SMS reminder
    '''
    config = {'account_sid' : '', 'auth_token' : ''}
    client = TwilioRestClient(config['account_sid'], config['auth_token'])
    message = client.messages.create(to="+15148871900", from_="+14387937890",
                                     body="Hello there!")

def main():
    send_sms()

if __name__ == "__main__":
    main()

