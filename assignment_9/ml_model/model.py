from PIL import Image
import random

def predict_dental_issues(image: Image.Image) -> dict:
    """
    Simulated ML model for testing UI integration.
    Replace this with actual ML model inference later.
    """
    issues = {
        "Cavity": {
            "detected": random.choice([True, False]),
        },
        "Discoloration": {
            "detected": random.choice([True, False]),
        },
        "Plaque/Swelling": {
            "detected": random.choice([True, False]),
        },
        "Malalignment": {
            "detected": random.choice([True, False]),
        }
    }
    return issues
