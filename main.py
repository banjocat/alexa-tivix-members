
import logging

from flask import Flask
from flask_ask import Ask, question, statement


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
    greeting = 'Saying Hello to Walter is nice. But I asked a question. Is Walter the best baby?'
    return question(greeting).reprompt(REPROMPT_TEXT)

@ask.intent('NoIntent')
def no_intent():
    what = 'Thank you for listening. Have a great day. Goodbye'
    return statement(what)

if __name__ == '__main__':
    app.run(debug=True)
