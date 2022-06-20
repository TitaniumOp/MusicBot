#KANGERS_GIVE_CREDITSOp
import os
import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from helpers.main import bot


from config import BOT_USERNAME
from helpers.msg import Messages as tr

Client = bot
client = bot

@Client.on_message(filters.private & filters.incoming & filters.command(["start"]))
def _start(client, message):
    client.send_message(
        message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group 🙋‍♀️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📲 Updates", url=f"https://t.me/TITANIUM_XYZ"
                    ),
                    InlineKeyboardButton(
                        "💬 Support", url=f"https://t.me/TITANIUMCHATS"
                    ),
                ],
                [InlineKeyboardButton("🛠 Source Code 🛠", url=f"https://github.com/TitaniumOp/MusicBot")],
            ]
        ),
        reply_to_message_id=message.message_id,
    )


@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🔴 Sumiko is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Support Chat", url=f"https://t.me/TITANIUMCHATS"
                    )
                ]
            ]
        ),
    )


