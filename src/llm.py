import os
import json
import base64
import requests
from pathlib import Path
from dotenv import load_dotenv

from src.prompt import VISION_PROMPT

load_dotenv()


def get_ollama_config():
    return {
        "host": os.getenv("OLLAMA_HOST", "http://localhost:11434"),
        #"model": os.getenv("OLLAMA_MODEL", "llama3.2-vision")
        "model": os.getenv("OLLAMA_MODEL", "qwen2.5vl:3b")
    }


def image_to_base64(image_path):
    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def ask_vision_model(image_path, prompt=VISION_PROMPT):
    config = get_ollama_config()

    print(f"[LLM] Host: {config['host']}")
    print(f"[LLM] Model: {config['model']}")

    image_b64 = image_to_base64(image_path)
    print(f"[LLM] Image converted to base64, length: {len(image_b64)}")

    payload = {
        "model": config["model"],
        "prompt": prompt,
        "images": [image_b64],
        "stream": False
    }

    print("[LLM] Calling Ollama API...")

    response = requests.post(
        f'{config["host"]}/api/generate',
        json=payload,
        timeout=120
    )

    print(f"[LLM] Status code: {response.status_code}")

    response.raise_for_status()

    print("[LLM] Response received")

    return response.json()["response"]



def parse_json_response(text):
    start = text.find("{")
    end = text.rfind("}") + 1

    if start == -1 or end == 0:
        raise ValueError("No JSON found in model response")

    json_text = text[start:end]
    return json.loads(json_text)


def extract_chart_data(image_path):
    print("[1] Starting chart extraction...")
    print(f"[2] Image path: {image_path}")

    print("[3] Sending image to Llama 3.2 Vision...")
    raw_output = ask_vision_model(image_path)

    print("[4] Raw model response received")
    print(raw_output)

    print("[5] Parsing JSON response...")
    parsed_data = parse_json_response(raw_output)

    print("[6] JSON parsed successfully")

    return parsed_data