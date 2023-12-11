""" 
this application determines the emotionality of the text 
using the Watson NLP library
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """This function starts rendering the main page of the application"""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion():
    """This function runs an analysis of the emotionality of user-provided text"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    formatted_response = emotion_predictor(response)

    if formatted_response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {formatted_response['anger']}"
        f"'disgust': {formatted_response['disgust']}"
        f"'fear': {formatted_response['fear']}"
        f"'joy': {formatted_response['joy']}"
        f"'sadness': {formatted_response['sadness']}"
        f"The dominant emotion is: {formatted_response['dominant_emotion']}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
