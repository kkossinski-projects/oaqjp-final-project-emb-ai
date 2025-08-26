"""
Flask application for Emotion Detection using Watson NLP service.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotion of the text provided via query parameter 'textToAnalyze'.
    Returns a formatted string with emotion scores and dominant emotion.
    If the input is invalid or dominant emotion is None, returns an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Get the emotion detection response dictionary
    response = emotion_detector(text_to_analyze)

    # Extract individual emotion scores with default 0
    anger = response.get('anger', 0)
    disgust = response.get('disgust', 0)
    fear = response.get('fear', 0)
    joy = response.get('joy', 0)
    sadness = response.get('sadness', 0)
    dominant_emotion = response.get('dominant_emotion', 'Unknown')

    # Check if dominant_emotion is None or missing
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Format the output string as per the example
    output = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

    return output


@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5006)
    