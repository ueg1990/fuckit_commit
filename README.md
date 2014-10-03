#fuckit_commit


Get SMS reminders to commit code daily and aim for your longest contribution streak!!! 

## Requirements
### Python dependencies
Using requirements.txt and pip, run the following command:

    pip install -r requirements.txt
    
### Others
* User will need access to a server e.g. DigitalOcean to run script as a cronjob so that script will run continuously as long as server is running
* User will need a Twilio account to receive SMS reminders. Go to the following link to set up a Twilio account: <https://www.twilio.com/try-twilio>
* Once user has a Twilio account, user can fill relevant information in configuration.json, including user's GitHub username

##Setting up crontab on the server
Example command on crontab for SMS reminder every four hours everyday. 

    0 0,4,8,12,16,20 * * * cd /root/fuckit_commit/; python fuckit_commit.py
