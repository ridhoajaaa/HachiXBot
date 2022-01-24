import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from HachiBot.events import register
from HachiBot import telethn as tbot


PHOTO = "https://telegra.ph/file/4ba029703f45315735c45.jpg"

@register(pattern=("/alive"))
async def awake(event):
  HACHI = f"**Hai Ketot Uwow [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Hachi Robot.** \n\n"
  HACHI += "⚪ **I'm Working Properly** \n\n"
  HACHI += f"⚪ **Lord Bapa Gua Ni : [Lord](https://t.me/ddodxy)** \n\n"
  HACHI += f"⚪ **Library Version :** `{telever}` \n\n"
  HACHI += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  HACHI += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  HACHI += "**Thanks For Adding Me Here **"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/HachiXBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/demonszxx")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=HACHI,  buttons=BUTTON)
