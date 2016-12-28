
import logging

from flask import Flask
from flask_ask import Ask, question, statement

from scraper.tivix import get_random_tivix_member_bio


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

REPROMPT_TEXT = 'Sorry, I did not understand you. Please say Yes or No. Would you like to hear about a Tivix member?'

@ask.launch
def launch():
    welcome_message = "Greetings. Would you like to hear about a Tivix member?"
    return question(welcome_message).reprompt(REPROMPT_TEXT)

@ask.intent('YesIntent')
def hello():
    tivix_member_bio = get_random_tivix_member_bio()
    message = tivix_member_bio + 'Would you like to hear more?'
    return question(message).reprompt(REPROMPT_TEXT)

@ask.intent('NoIntent')
def no_intent():
    what = 'Thank you for listening. Have a great day. Goodbye'
    return statement(what)


if __name__ == '__main__':
    app.run(debug=True)
