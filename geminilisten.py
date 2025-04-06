import os
import json
from google import genai
from google.genai.types import GenerateContentConfig

KEY = "AIzaSyANFwup2wz2SVRrgCRmTUOedpJmADJ5CAQ"
client = genai.Client(api_key=KEY)

SYSTEM_PROMPT = """Hello Gemini, I have a transcribed text file from an audio journal. 
Please convert it into a concise summary with bullet points that highlight:
- Key insights and main ideas
- Actionable items or recommendations
- Important context and tone preservation"""

dtr_path = 'Recorded_texts'

for root, dirs, files in os.walk(dtr_path):
    for filename in files:
        if filename.endswith('.json'):
            print(f"\n=== Processing {filename} ===")
            
            try:
                # 1. Load JSON Data
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                
                # 2. Format for Gemini API
                messages = [{
                    "role": "user",
                    "parts": [{
                        "text": f"Title: {entry['title']}\nContent: {entry['content']}"
                    }]
                } for entry in json_data.values()]
                
                # 3. Get Gemini Response
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    config=GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT
                    ),
                    contents=messages
                )
                
                # 4. Guaranteed Output
                print("\nGemini Summary:")
                print(response.text)
                print("\n" + "="*50 + "\n")
                
            except Exception as e:
                print(f"! Processing Error: {str(e)}")