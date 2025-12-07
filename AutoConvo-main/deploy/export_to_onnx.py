import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

def export_model(model_path, onnx_path="intent_model.onnx"):
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
    model = DistilBertForSequenceClassification.from_pretrained(model_path)
    model.eval()

    dummy_input = tokenizer("Call Pranjal", return_tensors="pt", padding=True, truncation=True)
    torch.onnx.export(model, (dummy_input['input_ids'],), onnx_path,
                      input_names=["input_ids"],
                      output_names=["logits"],
                      dynamic_axes={"input_ids": {0: "batch_size"}, "logits": {0: "batch_size"}},
                      opset_version=11)
    print(f"ONNX model exported to {onnx_path}")

if __name__ == "__main__":
    export_model("models/distilbert_finetuned", "models/onnx/intent_model.onnx")
