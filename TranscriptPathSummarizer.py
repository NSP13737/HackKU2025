import os
import json
from google import genai
from google.genai.types import GenerateContentConfig

class TranscriptSummarizer:
    def __init__(self, key="AIzaSyANFwup2wz2SVRrgCRmTUOedpJmADJ5CAQ", officer_number="001", base_path=None, system_instruction=None):
        """
        Initializes the TranscriptSummarizer with the API key, officer number (used for file paths),
        and an optional system instruction for the dialogue analysis.
        """
        self.key = key
        self.officer_number = officer_number
        self.base_path = base_path or os.getcwd()
        self.officer_path = os.path.join(self.base_path, f"officer_data/officer_{self.officer_number}")
        
        # Initialize the GenAI client once
        self.client = genai.Client(api_key=self.key)
        
        # If no system instruction is provided, use the default one.
        if system_instruction is None:
            system_instruction = (
                "Analyze this conversation transcript and create a concise summary that:\n"
                "- Identifies key revelations and turning points\n"
                "- Tracks speaker dynamics and roles\n"
                "- Highlights chronological progression\n"
                "- Presents main points in bullet format"
            )
            system_instruction = (
                "You are summarizing a log of audio filed from police officer (badge number 001) talking to citizens around the community while on duty. Your job is to summarize the logs in such a way that it provides the officer with information"
            )
        self.system_instruction = system_instruction

    def process_files(self, path_to_search):
        """
        Walks through the given directory (path_to_search), concatenates the contents
        of all JSON files found, and returns the combined text.
        """
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

    def generate_summary(self, transcripts_subdir='transcripts', summary_subdir='summaries', summary_filename='summary.txt'):
        """
        Processes the transcripts from the given subdirectory (relative to officer_path),
        calls the GenAI API to generate a summary, writes the summary to a file in the
        specified summaries subdirectory, and returns the summary text.
        """
        transcripts_path = os.path.join(self.officer_path, transcripts_subdir)
        long_text = self.process_files(transcripts_path)
        
        # API call to generate the content
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            config=GenerateContentConfig(
                system_instruction=self.system_instruction
            ),
            contents=str(long_text)
        )
        
        # Ensure the summaries directory exists
        summary_dir = os.path.join(self.officer_path, summary_subdir)
        os.makedirs(summary_dir, exist_ok=True)
        summary_path = os.path.join(summary_dir, summary_filename)
        
        with open(summary_path, 'w', encoding='utf-8') as summary_file:
            summary_file.write(response.text)
        
        return response.text

# Example usage:
if __name__ == "__main__":
    KEY = "AIzaSyANFwup2wz2SVRrgCRmTUOedpJmADJ5CAQ"
    summarizer = TranscriptSummarizer(key=KEY)
    summary = summarizer.generate_summary()
    print("Summary generated:")
    print(summary)