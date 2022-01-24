import time
import os
import re
import codecs
from typing import List
from random import randint
from asyncio.exceptions import TimeoutError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from HachiBot.modules.helper_funcs.chat_status import user_admin
from HachiBot.modules.disable import DisableAbleCommandHandler
from HachiBot import (
    dispatcher,
    WALL_API,
)
import requests as r
import wikipedia
from requests import get, post
from telegram import (
    Chat,
    ChatAction,
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Message,
    MessageEntity,
    TelegramError,
)
from telegram.error import BadRequest
from telegram.ext.dispatcher import run_async
from telegram.ext import CallbackContext, Filters, CommandHandler
from HachiBot import telethn as tbot
from HachiBot.events import register
from HachiBot import ubot
from HachiBot import StartTime
from HachiBot.modules.helper_funcs.chat_status import sudo_plus
from HachiBot.modules.helper_funcs.alternate import send_action, typing_action

MARKDOWN_HELP = f"""
Markdown is a very powerful formatting tool supported by telegram. {dispatcher.bot.first_name} has some enhancements, to make sure that \
saved messages are correctly parsed, and to allow you to create buttons.
❂ <code>_italic_</code>: wrapping text with '_' will produce italic text
❂ <code>*bold*</code>: wrapping text with '*' will produce bold text
❂ <code>`code`</code>: wrapping text with '`' will produce monospaced text, also known as 'code'
❂ <code>[sometext](someURL)</code>: this will create a link - the message will just show <code>sometext</code>, \
and tapping on it will open the page at <code>someURL</code>.
<b>Example:</b><code>[test](example.com)</code>
❂ <code>[buttontext](buttonurl:someURL)</code>: this is a special enhancement to allow users to have telegram \
buttons in their markdown. <code>buttontext</code> will be what is displayed on the button, and <code>someurl</code> \
will be the url which is opened.
<b>Example:</b> <code>[This is a button](buttonurl:example.com)</code>
If you want multiple buttons on the same line, use :same, as such:
<code>[one](buttonurl://example.com)
[two](buttonurl://google.com:same)</code>
This will create two buttons on a single line, instead of one button per line.
Keep in mind that your message <b>MUST</b> contain some text other than just a button!
"""


@user_admin
def echo(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(None, 1)
    message = update.effective_message

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            args[1], parse_mode="MARKDOWN", disable_web_page_preview=True
        )
    else:
        message.reply_text(
            args[1], quote=False, parse_mode="MARKDOWN", disable_web_page_preview=True
        )
    message.delete()


def markdown_help_sender(update: Update):
    update.effective_message.reply_text(MARKDOWN_HELP, parse_mode=ParseMode.HTML)
    update.effective_message.reply_text(
        "Try forwarding the following message to me, and you'll see, and Use #test!"
    )
    update.effective_message.reply_text(
        "/save test This is a markdown test. _italics_, *bold*, code, "
        "[URL](example.com) [button](buttonurl:github.com) "
        "[button2](buttonurl://google.com:same)"
    )


def markdown_help(update: Update, context: CallbackContext):
    if update.effective_chat.type != "private":
        update.effective_message.reply_text(
            "Contact me in pm",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Markdown help",
                            url=f"t.me/{context.bot.username}?start=markdownhelp",
                        )
                    ]
                ]
            ),
        )
        return
    markdown_help_sender(update)


def wiki(update: Update, context: CallbackContext):
    kueri = re.split(pattern="wiki", string=update.effective_message.text)
    wikipedia.set_lang("en")
    if len(str(kueri[1])) == 0:
        update.effective_message.reply_text("Enter keywords!")
    else:
        try:
            pertama = update.effective_message.reply_text("🔄 Loading...")
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🔧 More Info...",
                            url=wikipedia.page(kueri).url,
                        )
                    ]
                ]
            )
            context.bot.editMessageText(
                chat_id=update.effective_chat.id,
                message_id=pertama.message_id,
                text=wikipedia.summary(kueri, sentences=10),
                reply_markup=keyboard,
            )
        except wikipedia.PageError as e:
            update.effective_message.reply_text(f"⚠ Error: {e}")
        except BadRequest as et:
            update.effective_message.reply_text(f"⚠ Error: {et}")
        except wikipedia.exceptions.DisambiguationError as eet:
            update.effective_message.reply_text(
                f"⚠ Error\n There are too many query! Express it more!\nPossible query result:\n{eet}"
            )


@register(pattern="^/wall ?(.*)")
async def _(event):
    try:
        query = event.pattern_match.group(1)
        feri = await event.reply("`Searching for Images What you're looking for.....`")
        async with ubot.conversation("@AnosVoldigoadbot") as conv:
            try:
                query1 = await conv.send_message(f"/wall {query}")
                r1 = await conv.get_response()
                r2 = await conv.get_response()
                await ubot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                return await feri.edit("`Emrorr lol`")
            if r1.text.startswith("No"):
                return await feri.edit(f"`Cannot find the image`")
            img = await ubot.download_media(r1)
            img2 = await ubot.download_media(r2)
            await feri.edit("`Sending Image....`")
            p = await tbot.send_file(
                event.chat_id,
                img,
                force_document=False,
                reply_to=event.reply_to_msg_id,
            )
            await tbot.send_file(
                event.chat_id,
                img2,
                force_document=True,
                reply_to=p,
            )
            await feri.delete()
            await ubot.delete_messages(conv.chat_id, [r1.id, r2.id, query1.id])
        await event.delete()
        os.system("rm *.png *.jpg")
    except TimeoutError:
        return await feri.edit("`Cannot find the image`")


__help__ = """
*Available commands:*
❂ /markdownhelp*:* quick summary of how markdown works in telegram - can only be called in private chats
❂ /paste*:* Saves replied content to `nekobin.com` and replies with a url
❂ /react*:* Reacts with a random reaction 
❂ /ud <word>*:* Type the word or expression you want to search use
❂ /reverse*:* Does a reverse image search of the media which it was replied to.
❂ /wiki <query>*:* wikipedia your query
❂ /wall <query>*:* get a wallpaper from wall.alphacoders.com
❂ /cash*:* currency converter
 Example:
 `/cash 1 USD INR`  
      _OR_
 `/cash 1 usd inr`
 Output: `1.0 USD = 75.505 INR`
*Music Modules:*
❂ /video or /vsong (query): download video from youtube
❂ /music or /song (query): download song from yt servers. (API BASED)
❂ /lyrics (song name) : This plugin searches for song lyrics with song name.
"""

ECHO_HANDLER = DisableAbleCommandHandler(
    "echo", echo, filters=Filters.chat_type.groups, run_async=True)
MD_HELP_HANDLER = CommandHandler("markdownhelp", markdown_help, run_async=True)
WIKI_HANDLER = DisableAbleCommandHandler("wiki", wiki)

dispatcher.add_handler(ECHO_HANDLER)
dispatcher.add_handler(MD_HELP_HANDLER)
dispatcher.add_handler(WIKI_HANDLER)

__mod_name__ = "Extras"
__command_list__ = ["id", "echo", "wiki"]
__handlers__ = [
    ECHO_HANDLER,
    MD_HELP_HANDLER,
    WIKI_HANDLER,
]