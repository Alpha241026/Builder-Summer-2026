from dotenv import load_dotenv #importing load_dotenv to parse the .env file and get the api key (environment variable)

import os #built-in module for reading environment variables (like os.getenv)

load_dotenv() #loads .env contents into the environment

print(os.getenv("API_KEY")) #pulls it back out