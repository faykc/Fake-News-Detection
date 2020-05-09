from model import Model
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'ACCESS_TOKEN'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)
myModel = Model()

# Endpoint for verifying the token in initial setup
@app.route("/", methods=['GET'])
def verifyTokens():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

# Endpoint for actually recieving and sending messages
@app.route("/", methods=['POST'])
def receiveMessage():
    resultBody = request.get_json()
    # Determine message and respond accordingly
    messageDetails = (((resultBody['entry'])[0])['messaging'])[0]
    recipientId = messageDetails['sender']['id']
    messageSent = messageDetails['message']['text']
    sendMessage(recipientId, messageSent)
    return "processed"

# Sends the formatted response
def sendMessage(recipient_id, response):
    #sends user the text message provided via input response parameter
    new_corpus = [response]
    prediction = "real" if myModel.predict(new_corpus)=="REAL" else "fake"
    formattedResponse = "The model predicts that the news article that you have given is {}".format(prediction)
    disclaimer = "Disclaimer: This is a project for learning purposes, and the model predictions can be inaccurate"
    bot.send_text_message(recipient_id, formattedResponse)
    bot.send_text_message(recipient_id, disclaimer)
    return "success"

if __name__ == "__main__":
    app.run()