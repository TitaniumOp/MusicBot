import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
BOT_USERNAME = getenv("BOT_USERNAME", "")
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "1829202"))
API_ID = int(getenv("API_ID", "8186557")) #oP
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
