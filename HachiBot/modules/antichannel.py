import html

from telegram.ext.filters import Filters
from telegram import Update, message, ParseMode
from telegram.ext import CallbackContext
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)

import HachiBot.modules.sql.antilinkedchannel_sql as sql
from HachiBot.modules.helper_funcs.decorators import ddocmd, ddomsg
from HachiBot.modules.helper_funcs.channel_mode import user_admin, AdminPerms
from HachiBot.modules.helper_funcs.anonymous import AdminPerms, user_admin
from HachiBot.modules.sql.antichannel_sql import antichannel_status, disable_antichannel, enable_antichannel
from HachiBot.modules.helper_funcs.chat_status import bot_admin, bot_can_delete
from HachiBot.modules.helper_funcs.chat_status import user_admin as u_admin

@ddocmd(command="antich", group=100)
@user_admin(AdminPerms.CAN_RESTRICT_MEMBERS)
def set_antichannel(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    args = context.args
    if len(args) > 0:
        s = args[0].lower()
        if s in ["yes", "on"]:
            enable_antichannel(chat.id)
            message.reply_html("Enabled antichannel in {}".format(html.escape(chat.title)))
        elif s in ["off", "no"]:
            disable_antichannel(chat.id)
            message.reply_html("Disabled antichannel in {}".format(html.escape(chat.title)))
        else:
            message.reply_text("Unrecognized arguments {}".format(s))
        return
    message.reply_html(
        "Antichannel setting is currently {} in {}".format(antichannel_status(chat.id), html.escape(chat.title)))

@ddomsg(Filters.chat_type.groups, group=110)
def eliminate_channel(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    bot = context.bot
    if not antichannel_status(chat.id):
        return
    if message.sender_chat and message.sender_chat.type == "channel" and not message.is_automatic_forward:
        message.delete()
        sender_chat = message.sender_chat
        bot.ban_chat_sender_chat(sender_chat_id=sender_chat.id, chat_id=chat.id)


@ddocmd(command="antichannelpin", group=114)
@bot_admin
@user_admin(AdminPerms.CAN_RESTRICT_MEMBERS)
def set_antipinchannel(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    args = context.args
    if len(args) > 0:
        s = args[0].lower()
        if s in ["yes", "on"]:
            if sql.status_linked(chat.id):
                sql.disable_linked(chat.id)
                sql.enable_pin(chat.id)
                message.reply_html(
                    "Disabled Linked channel deletion and Enabled anti channel pin in {}".format(
                        html.escape(chat.title)
                    )
                )
            else:
                sql.enable_pin(chat.id)
                message.reply_html(
                    "Enabled anti channel pin in {}".format(html.escape(chat.title))
                )
        elif s in ["off", "no"]:
            sql.disable_pin(chat.id)
            message.reply_html(
                "Disabled anti channel pin in {}".format(html.escape(chat.title))
            )
        else:
            message.reply_text("Unrecognized arguments {}".format(s))
        return
    message.reply_html(
        "Linked channel message unpin is currently {} in {}".format(
            sql.status_pin(chat.id), html.escape(chat.title)
        )
    )

@ddomsg(Filters.is_automatic_forward | Filters.status_update.pinned_message, group=113)
def eliminate_linked_channel_msg(update: Update, _: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    if not sql.status_pin(chat.id):
        return
    try:
        message.unpin()
    except TelegramError:
        return

        
__help__ = """
──「 Anti-Channels 」──
    ⚠️ WARNING ⚠️
*IF YOU USE THIS MODE, THE RESULT IS IN THE GROUP FOREVER YOU CAN'T CHAT USING THE CHANNEL*
Anti Channel Mode is a mode to automatically ban users who chat using Channels. 
This command can only be used by *Admins*.

❂ /antich <'on'/'yes'> *:* enables anti-channel-mode
❂ /antich <'off'/'no'> *:* disabled anti-channel-mode
"""

__mod_name__ = "Anti-Channel"
