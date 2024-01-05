## Flask application

from flask import Flask

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def greet():
    return "Happy new year"

@app.route("/info",methods = ["GET"])
def info():
    return "This is the year of 2024"

@app.route("/success/<int:score>")
def success(score):
    return "The student has passed and the score is" + str(score)

if __name__=="__main__":
    app.run(debug=True)