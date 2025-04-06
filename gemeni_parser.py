import os
import json
from google import genai
from google.genai.types import GenerateContentConfig

# Initialize client once
KEY = "AIzaSyANFwup2wz2SVRrgCRmTUOedpJmADJ5CAQ"
client = genai.Client(api_key=KEY)

# Updated system instruction for dialogue analysis
SYSTEM_INSTRUCTION = """Analyze this conversation transcript and create a concise summary that:
- Identifies key revelations and turning points
- Tracks speaker dynamics and roles
- Highlights chronological progression
- Presents main points in bullet format
- Marks important timestamps where crucial information occurs"""

def process_files():
    dtr_path = 'Recorded_texts'
    all_summaries = []
    for root, _, files in os.walk(dtr_path):
        for filename in files:
            print(filename)
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                print(f"\nProcessing: {filename}")
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        json_data = json.load(f)
    
                        # API call
                        response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            config=GenerateContentConfig(
                                system_instruction=SYSTEM_INSTRUCTION
                            ),
                            contents=str(json_data)
                        )
                        
                        summary = response.text.strip()
                        all_summaries.append(summary)
                        print(f"Success! Summary:\n{summary}")
                        
                except json.JSONDecodeError:
                    print(f"Invalid JSON format in {filename}")
                except KeyError as ke:
                    print(f"Missing required field {ke} in {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")
    
    return all_summaries

if __name__ == "__main__":
    summaries = process_files()
    print("\nFinal Summaries:")
    for idx, summary in enumerate(summaries, 1):
        print(f"\nSummary #{idx}:\n{summary}")
        print("-" * 50)