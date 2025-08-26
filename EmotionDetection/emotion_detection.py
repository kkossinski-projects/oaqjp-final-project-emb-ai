import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse or text_to_analyse.strip() == "":
        # Return None or a dictionary with None values for blank input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj= { "raw_document": { "text": text_to_analyse }}
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code != 200:
        # Handle non-200 responses similarly
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']

    strongest_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions.get('anger'),
        'disgust': emotions.get('disgust'),
        'fear': emotions.get('fear'),
        'joy': emotions.get('joy'),
        'sadness': emotions.get('sadness'),
        'dominant_emotion': strongest_emotion
    }