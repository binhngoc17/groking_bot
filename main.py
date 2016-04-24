# -*- coding: utf-8 -*-
import time
from slackclient import SlackClient
import os


BOT_TOKEN = os.environ.get('API_TOKEN')
CHANNEL_NAME = "testing"

def main():
    # Create the slackclient instance
    sc = SlackClient(BOT_TOKEN)

    # Connect to slack
    if sc.rtm_connect():

        while True:
            # Read latest messages
            for slack_message in sc.rtm_read():
                print slack_message
                if slack_message.get('type') == 'message':


                    if slack_message.get('subtype') == 'channel_join':
                        user = slack_message.get('user')
                        print user
                        sc.rtm_send_message(CHANNEL_NAME, """
Hello, <@{user}> welcome to {channel}! \n
Can you introduce yourself in this format:
1. Tên + tuổi
2. Nghề nghiệp. Location
3. Skills (programming languages, databases, frameworks)
4. Show-off (projects worked on or currently working on + side projects, etc)
5. (optional) FB/linkedin/github
6.  (optional) Sở thích (ngoài programming)
                        """.format(
                                user=user,
                                channel=CHANNEL_NAME
                            )
                        )
                    else:
                        message = slack_message.get("text")
                        user = slack_message.get("user")
                        if not message or not user:
                            continue
                        sc.rtm_send_message(CHANNEL_NAME, "<@{}> wrote something...".format(user))

            time.sleep(0.5)

if __name__ == '__main__':
    main()
