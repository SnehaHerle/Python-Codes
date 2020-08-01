#!/usr/bin/python

import fbchat
from getpass import getpass

username = str(raw_input("\nYour username: "))
client = fbchat.Client(username, getpass())
no_of_friends = int(raw_input("\nNumber of friends to send: "))

for i in xrange(no_of_friends):

    name = str(raw_input("\nName of the friend: "))
    friends = client.getUsers(name)  # return a list of names
    friend = friends[0]

    print "\nHere is the information about the friend: \n" , client.getUserInfo(friend.uid)

    answer = str(raw_input("\n\nDo you want to send an image or a message?\nPress i for image. Or, press m for message: "))

    if answer is 'i':
        msg = str(raw_input("\nMessage along with image: "))
        answer = str(raw_input("\nDo you want to send a local image or a remote image from the internet?\nPress l for local. Or, press r for remote: "))
        if answer is 'l':
            img = str(raw_input("\nPath of the local image: "))
            sent = client.sendLocalImage(friend.uid,message=msg,image= img)
        elif answer is 'r':
            img = str(raw_input("\nEnter the full url of the image: "))
            sent = client.sendRemoteImage(friend.uid,message=msg, image=img)
        if sent:
            print("Yay! Message sent successfully!")

    elif answer is 'm':
        msg = str(raw_input("\nMessage to be sent is: "))
        num = int(raw_input("\nEnter the number of times you want to send this message: "))
        for i in range(num):
            sent = client.send(friend.uid, msg)
            if sent:
                print("Yay! Message sent successfully!")

    last_messages = client.getThreadInfo(friend.uid,0)

    last_messages.reverse() #Now the order becomes from older to recent.

    print "\nThe recent messages sent to this friend are: "
    for message in last_messages:
        print message.body, message.timestamp_relative
