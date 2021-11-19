from flask import Flask
from time import strftime, localtime

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<p>Use the endpoint /time to get the local time</p>"

@app.route('/time')
# Solution to the exercise, it takes the localtime from the time library
# and return it in a JSON format as asked in the wording
def time():
    return {
        "currentDateTime": strftime("%Y-%m-%dT%H:%MZ", localtime())
    }
