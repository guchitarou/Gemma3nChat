from transformers import AutoProcessor, Gemma3nForConditionalGeneration
from PIL import Image
import requests
import torch

model_id = "./model_weights"

dtype = torch.bfloat16

model = Gemma3nForConditionalGeneration.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=dtype,
).eval()
processor = AutoProcessor.from_pretrained(model_id)

messages = [
    {
        "role": "system",
        "content": [{"type": "text", "text": "You are a helpful assistant."}],
    },
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "./bee.jpg"},
            {"type": "text", "text": "入力した画像について説明してほしいお"},
        ],
    },
]

inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)


input_len = inputs["input_ids"].shape[-1]
inputs = inputs.to(model.device, dtype=model.dtype)
with torch.inference_mode():
    generation = model.generate(**inputs, max_new_tokens=100, do_sample=False)
    generation = generation[0][input_len:]

decoded = processor.decode(generation, skip_special_tokens=True)

print("出力は👇")
print(decoded)
