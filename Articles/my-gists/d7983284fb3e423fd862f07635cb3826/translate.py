import requests
import gradio as gr
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

model_name = "google/flan-t5-xxl"
API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    # HTTP POST Request
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def translate(src_lang, tgt_lang, input_text):

    # Prompt Construction:
    prompt = f"Translate from {src_lang} to {tgt_lang}: {input_text}"
    # API Request:
    response = query({
        "inputs": prompt,
        "max_new_tokens": 250
    })

    translation = response[0]["generated_text"]

    return translation

languages = [
    'English', 'Spanish', 'Japanese', 'Persian', 'Hindi', 'French', 'Chinese',
    'Bengali', 'Gujarati', 'German', 'Telugu', 'Italian', 'Arabic', 'Polish',
    'Tamil', 'Marathi', 'Malayalam', 'Oriya', 'Panjabi', 'Portuguese', 'Urdu',
    'Galician', 'Hebrew', 'Korean', 'Catalan', 'Thai', 'Dutch', 'Indonesian',
    'Vietnamese', 'Bulgarian', 'Filipino', 'Central Khmer', 'Lao', 'Turkish',
    'Russian', 'Croatian', 'Swedish', 'Yoruba', 'Kurdish', 'Burmese', 'Malay',
    'Czech', 'Finnish', 'Somali', 'Tagalog', 'Swahili', 'Sinhala', 'Kannada',
    'Zhuang', 'Igbo', 'Xhosa', 'Romanian', 'Haitian', 'Estonian', 'Slovak',
    'Lithuanian', 'Greek', 'Nepali', 'Assamese', 'Norwegian'
]

desc = "<h1><em>tTranslaterR</em> is a translation app powered by AI models" \
       " capable of translating text between 50+ languages</h1>"

translator = gr.Interface(fn=translate,
                          inputs=[gr.Textbox(label="Input Text", placeholder="Input Text To Be Translated"),
                                  gr.Dropdown(label="From",
                                              choices=languages,
                                              value="English",),
                                  gr.Dropdown(label="To",
                                              choices=languages,
                                              value="French")],
                          outputs=gr.Textbox(label="Translation"),
                          title="tTranslatorR",
                          description=desc
                          )

translator.launch()
