from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch

class IntentClassifier:
    def __init__(self, model_path):
        self.tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
        self.model = DistilBertForSequenceClassification.from_pretrained(model_path)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        outputs = self.model(**inputs)
        logits = outputs.logits
        pred = torch.argmax(logits, dim=1)
        return pred.item()
