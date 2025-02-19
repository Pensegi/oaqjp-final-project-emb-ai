import requests
import json

def emotion_detector(text_to_analyse: str):
    r = requests.post(
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json = { "raw_document": { "text": text_to_analyse } }
        )

    if r.status_code == 200:
        response_dict = json.loads(r.text)
        if "emotionPredictions" in response_dict:
            text = response_dict["emotionPredictions"][0]["emotion"]

            dominant_emotion = "none"
            dominant_emotion_value = 0            
            for emotion, value in text.items():
                if value > dominant_emotion_value: 
                    dominant_emotion = emotion
                    dominant_emotion_value = value

            text["dominant_emotion"] = dominant_emotion
            
        return text
