from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls, idle

bot = Client(
    "Titanium",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers"),
    )

shivam = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    
    )

user = PyTgCalls(shivam,
    cache_duration=100,
    overload_quiet_mode=True,)

call_py = PyTgCalls(shivam, overload_quiet_mode=True)

with Client("Titanium", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with shivam as app:
    me_shivam = app.get_me()
