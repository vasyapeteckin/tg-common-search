import os

from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

app = Client("my_account", api_id=api_id, api_hash=api_hash)

app.run()
