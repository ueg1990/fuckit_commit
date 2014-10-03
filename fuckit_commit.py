'''
This module will send SMS reminders periodically, using Twilio.
The aim is to encourage user to code, commit and push to GitHub everyday

To set up SMS reminders, user has to have a Twilio account and a GitHub
username. From the Twilio account, the SID, auth_token, number to send from
and number to send to are required. This twilio info and the github username
can be filled in the configuration.json file. Once that is one, user can set
up a cron job on his/her server
'''

import requests
from twilio.rest import TwilioRestClient
from datetime import datetime, date
import json

def get_config_info():
    with open('configuration.json') as f:
	data = json.load(f)
    return data

def send_sms(twilio_info):
    '''
    Send SMS reminder
    '''
    client = TwilioRestClient(twilio_info['sid'], twilio_info['auth_token'])
    message = client.messages.create(to=twilio_info["number_to"], from_=twilio_info["number_from"],
                                     body="You need to commit today!!!\nFuck it!!! Commit!!!")
def check_commit_activity(github_info):
    '''
    Check if there was any change in the commit history of the user. If date of 
    latest event is the same as current date, commit was made, hence return True
    else return False. Returning False triggers sending of an SMS reminder
    '''
    get_recent_event = requests.get("https://api.github.com/users/%s/events/public" % github_info['username'])
    event_date =  datetime.strptime(get_recent_event.json()[0]['created_at'].split('T')[0], '%Y-%m-%d').date()
    return event_date == date.today()

def main():
    config = get_config_info() 
    if not check_commit_activity(config['github']):
        send_sms(config['twilio'])

if __name__ == "__main__":
    main()

