from dotenv import load_dotenv
from google import genai
import os

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain what a Large Language Model is in simple words."
)

# Display AI response
print(response.text)