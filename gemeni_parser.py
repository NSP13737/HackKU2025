import os
import json
from google import genai
from google.genai.types import GenerateContentConfig

# Initialize client once
KEY = "AIzaSyANFwup2wz2SVRrgCRmTUOedpJmADJ5CAQ"
OFFICER_PATH = os.path.join(os.getcwd(), 'officer_data/officer_001/')
client = genai.Client(api_key=KEY)

# Updated system instruction for dialogue analysis
SYSTEM_INSTRUCTION = """Hello Gemini, I have a transcribed text file from an audio journal of a police bodycam interaction, and I need your help in converting it into a concise, well-organized summary. Please analyze the transcription and produce summarized notes that capture the key insights, main ideas, and any actionable items mentioned in the original text. Your summary should: Eliminate any redundant or extraneous dialogue, focusing only on the core content. Be structured in clear, bullet-point format, or use short paragraphs if that improves clarity. Retain the original tone and context where appropriate, ensuring that no important nuance is lost. Highlight any recommendations or action steps that the speaker might have implied or stated explicitly. Please output your summary in a way that allows a reader to quickly understand the most important information without needing to refer back to the full transcript. The full transcript will be provided underneath this contextual paragraph."""

def process_files(path_to_search):
    all_summaries = []
    full_text = ''
    for root, _, files in os.walk(path_to_search):
        for filename in files:
            print(filename)
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                print(f"\nProcessing: {filename}")
                full_text += f"FILENAME: {filename}\n"
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        json_data = json.load(f)
                        full_text += str(json_data) + '\n\n'
                        
                except json.JSONDecodeError:
                    print(f"Invalid JSON format in {filename}")
                except KeyError as ke:
                    print(f"Missing required field {ke} in {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")
    print(full_text)
    return full_text

if __name__ == "__main__":
    file_path = os.path.join(OFFICER_PATH, 'transcripts')
    long_text = process_files(file_path)

    # API call
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION
        ),
        contents=str(long_text)
    )
    with open(os.path.join(OFFICER_PATH, 'summaries/summary.txt'), 'w') as summary_file:
        summary_file.write(response.text)
    print("\nFinal Summaries:")
    # for idx, summary in enumerate(summaries, 1):
    #     print(f"\nSummary #{idx}:\n{summary}")
    #     print("-" * 50)