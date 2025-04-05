KEY = "AIzaSyANFwup2wz2S_DELETE_THIS_VRrgCRmTUOedpJmADJ5CAQ"

from google import genai

client = genai.Client(api_key=KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="How can I use a raspberry pi to record audio"
)
print(response.text)
