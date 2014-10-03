'''
This module will send SMS reminders periodically, using Twilio.
The aim is to encourage user to code, commit and push to GitHub everyday
'''

import requests
from twilio.rest import TwilioRestClient
from datetime import datetime, date
import json

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
    Check if there was any change in the commit history of the user. If date of 
    latest event is the same as current date, commit was made, hence return True
    else return False. Returning False triggers sending of an SMS reminder
    '''
    get_recent_event = requests.get("https://api.github.com/users/%s/events/public" % '')
    event_date =  datetime.strptime(get_recent_event.json()[0]['created_at'].split('T')[0], '%Y-%m-%d').date()
    return event_date == date.today()

def main():
    with open('configuration.json') as f:
	data = json.loads(f)
    print data
    print type(data)
    #if not check_commit_activity():
    #    send_sms()

if __name__ == "__main__":
    main()

