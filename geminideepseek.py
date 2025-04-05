import os
import json
from google import genai
from google.genai.types import GenerateContentConfig

# Initialize client once
KEY = "AIzaSyANFwup2wz2SVRrgCRmTUOedpJmADJ5CAQ"  # Replace with your actual key
client = genai.Client(api_key=KEY)

# System instruction constant
SYSTEM_INSTRUCTION = """Hello Gemini, I have a transcribed text file from an audio journal. Please convert it into a concise summary with:
- Bullet-point format
- Key insights and action items
- Original tone preservation
- Clear organization"""

def process_files():
    dtr_path = r'C:\Users\smith\OneDrive\Documents\GitHub\HackKU2025\Recorded_texts'
    all_summaries = []
    
    for root, _, files in os.walk(dtr_path):
        for filename in files:
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                print(f"\nProcessing: {filename}")
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        json_data = json.load(f)
                        
                        # Format with required role field
                        formatted_contents = [
                            {
                                "role": "user",  # Critical fix
                                "parts": [{
                                    "text": f"Title: {entry['title']}\nContent: {entry['content']}"
                                }]
                            }
                            for entry in json_data.values()
                        ]
                        
                        # API call
                        response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            config=GenerateContentConfig(
                                system_instruction=SYSTEM_INSTRUCTION
                            ),
                            contents=formatted_contents
                        )
                        
                        summary = response.text.strip()
                        all_summaries.append(summary)
                        print(f"Success! Summary:\n{summary}")
                        
                except json.JSONDecodeError:
                    print(f"Invalid JSON format in {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")
    
    return all_summaries

if __name__ == "__main__":
    summaries = process_files()
    print("\nFinal Summaries:")
    for idx, summary in enumerate(summaries, 1):
        print(f"\nSummary #{idx}:\n{summary}")
        print("-" * 50)
