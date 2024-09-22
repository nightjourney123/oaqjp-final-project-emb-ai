"""
This module implements an Emotion Detector web application using Flask.
It analyzes the emotions present in the provided text and returns the results.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the emotions in the given text."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the response is None
    if response is None:
        return "Invalid input! Try again."
    # Extract emotions and the dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    # Return a formatted string with the emotions and the dominant emotion
    return (f"For the given statement, the system response is "
            f"anger: {anger}, disgust: {disgust}, fear: {fear}, "
            f"joy: {joy}, sadness: {sadness}. The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
