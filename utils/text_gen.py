from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import pipeline, BitsAndBytesConfig
import torch
from dotenv import load_dotenv
import json
import os

def get_api_token():
    load_dotenv()
    api_token = os.getenv("token_hgf")

    if api_token is None:
        raise ValueError("API token not found. Please set the 'token_hgf' environment variable.")
    return api_token

def load_model(model_name):
  model_name = model_name  # or other model
  token =   get_api_token()
  
  # Quantization configuration
  quant_config = BitsAndBytesConfig(
        load_in_8bit=True,              # Enable 8-bit loading
        llm_int8_threshold=6.0,         # Optional tuning
        llm_int8_skip_modules=None,     # Optional tuning
    )

  try:
      model = AutoModelForCausalLM.from_pretrained(model_name, 
                                                   token=token, 
                                                   device_map="auto",                # Important for offloading
                                                   quantization_config=quant_config) # ← HERE!)
      tokenizer = AutoTokenizer.from_pretrained(model_name, token=token)
      print("Model and tokenizer loaded successfully!")

      return model, tokenizer

  except OSError as e:
      print(f"Error: {e}")
      print("Please verify the model name and ensure you have the correct token.")


# Get the size of the model in memory
def get_size(model):
  param_size = 0
  for param in model.parameters():
      param_size += param.nelement() * param.element_size()

  buffer_size = 0
  for buffer in model.buffers():
      buffer_size += buffer.nelement() * buffer.element_size()

  size_all_mb = (param_size + buffer_size) / 1024**2
  print(f"Model size: {size_all_mb:.2f} MB")

# use GPU cuda
def use_gpu():
  if torch.cuda.is_available():
      device = 0
      print("GPU available")
      return device
  else:
      device = -1
      print("No GPU available")
      return device

def load_history(filepath):
    if os.path.exists(filepath):
        if os.path.getsize(filepath) == 0:      # File exists but is empty
            return []
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

def save_history(chat_history, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(chat_history, f, ensure_ascii=False, indent=4)

def gen_text_chat(model, tokenizer, temperature=0.7, top_p=0.9, top_k=50, max_length=1024, num_beams=4, do_sample=True, 
                  device=-1, history_file="chat_history.json"):
    # Load chat history if it exists
    chat_history = load_history(history_file)
    device = model.device  # Get model device (CPU or CUDA)

    print("Type 'exit' or 'quit' to end the chat.\n")
    for entry in chat_history:
        print(entry)

    while True:
        user_input = input("User: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        # Append user input to chat history
        chat_history.append(f"User: {user_input}")

        # Construct context
        context = "\n".join(chat_history) + "\nAssistant:"

        # Tokenize and generate
        inputs = tokenizer(context, 
                           return_tensors="pt", 
                           truncation=True, 
                           max_length=max_length).to(device)
        output_ids = model.generate(**inputs, 
                                    temperature=temperature,
                                    top_p=top_p,
                                    top_k=top_k,
                                    num_beams=num_beams,
                                    max_length=max_length,
                                    do_sample=do_sample,
                                    pad_token_id=tokenizer.eos_token_id)
        full_output = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()

        # Extract response
        if full_output.startswith(context):
            response = full_output[len(context):].strip()
        else:
            response = full_output

        for marker in ["User:", "Assistant:"]:
            if marker in response:
                response = response.split(marker)[0].strip()
        response = response.rsplit("Assistant", 1)[0].strip()

        # Append response
        chat_history.append(f"Assistant: {response}")
        print(f"Assistant: {response}\n")

    # Save chat history to file
    save_history(chat_history, history_file)
    return chat_history
