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

    text = "For the given statement, the system response is " \
    f"'anger': {response['anger']}, " \
    f"'disgust': {response['disgust']}, " \
    f"'fear': {response['fear']}, " \
    f"'joy': {response['joy']} and " \
    f"'sadness': {response['sadness']}. " \
    f"The dominant emotion is {response['dominant_emotion']}."

    return text

if __name__ == "__main__":
    app.run(debug=True)