#!/usr/bin/env python3
"""
Script to download GGUF models from Hugging Face
"""

from huggingface_hub import hf_hub_download
import os

def download_gguf_model(repo_id, filename, local_dir="./models"):
    """
    Download a GGUF model from Hugging Face Hub
    
    Args:
        repo_id: Repository ID (e.g., "microsoft/DialoGPT-medium")
        filename: Name of the GGUF file to download
        local_dir: Local directory to save the model
    """
    # Create models directory if it doesn't exist
    os.makedirs(local_dir, exist_ok=True)
    
    print(f"Downloading {filename} from {repo_id}...")
    
    try:
        model_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=local_dir,
            local_dir_use_symlinks=False
        )
        print(f"Model downloaded successfully to: {model_path}")
        return model_path
    except Exception as e:
        print(f"Error downloading model: {e}")
        return None

# Popular small GGUF models you can try:
RECOMMENDED_MODELS = {
    "TinyLlama-1.1B": {
        "repo_id": "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF",
        "filename": "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
    },
    "Phi-3-Mini": {
        "repo_id": "microsoft/Phi-3-mini-4k-instruct-gguf", 
        "filename": "Phi-3-mini-4k-instruct-q4.gguf"
    },
    "CodeQwen-1.5B": {
        "repo_id": "Qwen/CodeQwen1.5-7B-Chat-GGUF",
        "filename": "codeqwen-1_5-7b-chat-q4_0.gguf"
    }
}

if __name__ == "__main__":
    print("Available models:")
    for name, info in RECOMMENDED_MODELS.items():
        print(f"  {name}: {info['repo_id']}")
    
    # Download TinyLlama (small and fast)
    model_info = RECOMMENDED_MODELS["TinyLlama-1.1B"]
    
    print(f"\nDownloading {model_info['filename']}...")
    model_path = download_gguf_model(
        repo_id=model_info["repo_id"],
        filename=model_info["filename"]
    )
    
    if model_path:
        print(f"\nYou can now use this model path in your GGML_test.py:")
        print(f'model_path = "{model_path}"')
