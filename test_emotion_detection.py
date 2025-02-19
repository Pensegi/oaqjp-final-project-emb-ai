import EmotionDetection as ed

#{[Statement]: [Dominant Emotion]}
test_cases = {
    "joy": "I am glad this happened",
    "anger": "I am really mad about this",
    "disgust": "I feel disgusted just hearing about this",
    "sadness": "I am so sad about this",
    "fear": "I am really afraid that this will happen",
}

def test_assert_dominant_emotion_joy():
    assert ed.emotion_detector(test_cases["joy"])["dominant_emotion"] == "joy"

def test_assert_dominant_emotion_anger():
    assert ed.emotion_detector(test_cases["anger"])["dominant_emotion"] == "anger"

def test_assert_dominant_emotion_disgust():
    assert ed.emotion_detector(test_cases["disgust"])["dominant_emotion"] == "disgust"

def test_assert_dominant_emotion_sadness():
    assert ed.emotion_detector(test_cases["sadness"])["dominant_emotion"] == "sadness"

def test_assert_dominant_emotion_fear():
    assert ed.emotion_detector(test_cases["fear"])["dominant_emotion"] == "fear"
