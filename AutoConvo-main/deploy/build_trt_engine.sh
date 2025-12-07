#!/bin/bash
# Requires: TensorRT and trtexec tool installed on Jetson device

echo "Building TensorRT engine from ONNX model..."
trtexec --onnx=models/onnx/intent_model.onnx --saveEngine=models/tensorrt/intent_model.trt --fp16
echo "Engine saved to models/tensorrt/intent_model.trt"
