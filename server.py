from flask import render_template, Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', system_response="")

@app.route('/emotionDetector')
def emotionDetector():
    textToAnalyze = request.args.get("textToAnalyze")
    response = emotion_detector(textToAnalyze)
    return response

if __name__ == "__main__":
    app.run(debug=True)