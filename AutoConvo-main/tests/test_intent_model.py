import unittest
from src.intent_model import IntentClassifier

class TestIntentModel(unittest.TestCase):
    def setUp(self):
        self.classifier = IntentClassifier("models/distilbert_finetuned")

    def test_prediction_type(self):
        intent = self.classifier.predict("Call Pranjal")
        self.assertIsInstance(intent, int)

if __name__ == "__main__":
    unittest.main()
