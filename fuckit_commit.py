'''
This module will send SMS reminders periodically, using Twilio.
The aim is to encourage user to code, commit and push to GitHub everyday
'''

import requests
from twilio.rest import TwilioRestClient

def get_configuration():
    '''
    Set Twilio configuration
    '''
    pass

def get_twilio_client(config):
    '''
    Connect to Twilio Client
    '''
    return TwilioRestClient(config.account_sid, config.auth_token)

def send_sms(client):
    '''
    Send SMS reminder
    '''
    pass

def main():
    config = get_configuration()
    client = get_configuration(config)
    send_sms(client)

if __name__ == "__main__":
    main()

