'''File for serving Emotion Detector web applicaion that analyzes text for emotion and returns 
   a score for each emotion or an error'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detective():
    '''analyzes text emotion and returns a score or an error'''
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given satement, the system response is 'anger': {response['anger']},\
     'disgust': {response['disgust']},\
     'fear': {response['fear']},\
     'joy': {response['joy']}, and\
     'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}"

@app.route("/")
def render_index_page():
    '''renders index.html'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
