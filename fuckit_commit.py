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
    message = client.messages.create(to="", from_="",
                                     body="Hello there!")
def check_commit_activity():
    '''
    Check if there was any change in the commit history of the user
    '''
    get_recent_event = requests.get("https://api.github.com/users/ueg1990/events/public")
    print get_recent_event.json()[0]['created_at']
    return False

def main():
    check_commit_activity()
    # send_sms()

if __name__ == "__main__":
    main()

