# Import os to read environment variables
import os

# Load variables from the .env file
from dotenv import load_dotenv

# Import Google's Gemini SDK
from google import genai

# Load all variables from the .env file
load_dotenv()

# Read the Gemini API key from the environment
API_KEY = os.getenv("GEMINI_API_KEY")

# Stop the program if no API key is found
if not API_KEY:
    raise ValueError("Gemini API key not found. Check your .env file.")

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# Ask the user for notes
print("Enter your notes.")
print("Press Enter twice to finish.\n")

lines = []

while True:
    line = input()

    if line == "":
        break

    lines.append(line)

notes = "\n".join(lines)

# Build the prompt
prompt = f"""
You are a helpful study assistant.

Summarize these notes.

Also provide:

1. Key points
2. Important concepts
3. A short revision summary

Notes:

{notes}
"""

# Send the prompt to Gemini and store the response
try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(response.text)

except Exception as e:
    print("\nGemini request failed.")
    print(e)