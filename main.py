import asyncio
from pytgcalls import idle
#from config import api_id, api_hash, bot_token, session_name
import os
import sys
import random
import telethon.utils
from telethon import TelegramClient, events
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls
from pyrogram import Client

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "handlers"},
)

BOT = TelegramClient('BOT', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)
op = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'handlers'})
app = PyTgCalls(op)

bot.run
app.start

