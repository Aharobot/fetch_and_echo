#!/usr/bin/env python

from threading import Thread

import rospy

import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

import simple_disco

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_game():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent("DanceIntent")
def ask_confirmation():
    ask_msg = render_template('dance')
    return question(ask_msg)

@ask.intent("ConfirmIntent")
def dance_confirm():
    confirm_msg = render_template('confirmation')
    th = Thread(target = simple_disco.dance)
    th.start()
    return statement(confirm_msg)

def main():
    rospy.init_node("eva_lane")
    print "Running"
    app.run(host='0.0.0.0', port=1234)

if __name__ == '__main__':
    main()

