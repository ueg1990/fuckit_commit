import unittest
import json
from twilio.rest import TwilioRestClient

import fuckit_commit

class Fuckit_CommitTestCase(unittest.TestCase):
    '''
    Unit Test cases for fuckit_commit
    '''
    def setUp(self):
	with open('configuration.json') as f:
	    self.config = json.load(f)

    def test_send_sms(self):
	client = TwilioRestClient(self.config['twilio']['sid'], self.config['twilio']['auth_token'])
        message = client.messages.create(to=self.config['twilio']["number_to"], from_=self.config['twilio']["number_from"],
                                     body="You need to commit today!!!\nFuck it!!! Commit!!!")        
	self.assertEqual(message.account_sid, self.config['twilio']['sid'])

    def tearDown(self):
	pass

if __name__ == '__main__':
    unittest.main()
