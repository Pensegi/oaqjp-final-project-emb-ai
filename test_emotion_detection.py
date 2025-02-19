import EmotionDetection as ed

#{[Statement]: [Dominant Emotion]}
test_cases = {
    "I am glad this happened":	"joy",
    "I am really mad about this": "anger",
    "I feel disgusted just hearing about this": "disgust",
    "I am so sad about this": "sadness",
    "I am really afraid that this will happen": "fear",
}

def test_assert_dominant_emotion():
    for text, emotion in test_cases.items():
        print(f"text: {text}: emotion:: {emotion}")
        assert ed.emotion_detector(text) == emotion
