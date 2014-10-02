'''
This module will send SMS reminders periodically, using Twilio.
The aim is to encourage user to code, commit and push to GitHub everyday
'''

import requests
from twilio.rest import TwilioRestClient
from datetime import datetime, date

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
    print datetime.strptime(get_recent_event.json()[0]['created_at'].split('T')[0], '%Y-%m-%d').date()
    print date.today()
    print datetime.strptime(get_recent_event.json()[0]['created_at'].split('T')[0], '%Y-%m-%d').date() ==  date.today()
    print type(datetime.strptime(get_recent_event.json()[0]['created_at'].split('T')[0], '%Y-%m-%d').date()), type(date.today())
    return False

def main():
    check_commit_activity()
    # send_sms()

if __name__ == "__main__":
    main()

