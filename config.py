import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TitaniumXd")
BOT_USERNAME = getenv("BOT_USERNAME", "TITANIUMXYZBOT")
SESSION_NAME = getenv("SESSION_NAME", "BQCKNLkqpXd8l9SgHnKNzO0GiTPctByvVPn5sJTVNQjA4oAP6cdFcfLOVoP729bX0B7l5UDrNQyGb8I92IJFd0lYjqlKqpJdaJJkM1RA3kd0npblMuYDSXARLi3nhw03OeqqVDZIIagHNObaifQB3FBmJGi-NkVE1EcKqoUU-kZrn6GRiDNVs1KE80GunNttTFbnJ271tYeTyvqMMvgvWfLt_vMnwdRENHqRflwFkoAEHCrOrMUzv40kruN4Npcfgjbq_68Y2XtVjKB9u5_cEMlja2xl8pIcxvivcuDf5Tstr13PhBpvvRrZMFgjdznH4BdvgdXjR-KyfKFuJp6P7RP3AAAAASogKNEA")
BOT_TOKEN = getenv("BOT_TOKEN", "5373933240:AAFyzbScHY0rr4oJwOlcYnThhQ6tcBqW8kc")
OWNER_ID = int(getenv("OWNER_ID", "5001717969")
API_ID = int(getenv("API_ID", "8186557")) #oP
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
