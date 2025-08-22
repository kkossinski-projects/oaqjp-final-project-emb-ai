import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  # Define a function
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj= { "raw_document": { "text": text_to_analyse }}
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API
    # Parsing the JSON response from the API
   
    formatted_response = json.loads(response.text)
   
    # Extracting emotions from the response
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # Establishing which is the strongest emotion
        # Extract the emotion dictionary
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Find the emotion with the highest value
        strongest_emotion = max(emotions, key=emotions.get)
    
    # Returning a dictionary containing sentiment analysis results

    return {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': strongest_emotion
    }
