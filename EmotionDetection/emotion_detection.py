import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)  # Send a POST request to the API with the text and headers

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        formatted_response = json.loads(response.text)

        emotions = formatted_response['emotionPredictions'][0]['emotion']

        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']

        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return the formatted dictionary
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}



