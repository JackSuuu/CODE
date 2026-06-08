import ctypes
import numpy as np
from llama_cpp import Llama

# Load a small GGML model (you'll need to download a model file first)
# Example with a small model like TinyLlama or similar
model_path = "models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"  # Downloaded TinyLlama model

# Initialize the Llama model
llm = Llama(
    model_path=model_path,
    n_ctx=512,  # Context length
    n_batch=128,  # Batch size
    verbose=False
)

def inference_text(prompt, max_tokens=100):
    """
    Perform inference on the given prompt
    """
    output = llm(
        prompt,
        max_tokens=max_tokens,
        stop=["</s>"],
        echo=True
    )
    
    return output['choices'][0]['text']

# Example usage
if __name__ == "__main__":
    prompt = "The quick brown fox"
    
    try:
        result = inference_text(prompt, max_tokens=50)
        print(f"Input: {prompt}")
        print(f"Output: {result}")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have:")
        print("1. Installed llama-cpp-python: pip install llama-cpp-python")
        print("2. Downloaded a GGUF model file")
        print("3. Updated the model_path variable")