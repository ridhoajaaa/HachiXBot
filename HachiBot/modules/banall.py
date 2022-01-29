from time import sleep
from typing import Optional, List
from telegram import TelegramError
from telegram import Update
from telegram.error import BadRequest
from telegram.ext import Filters, CommandHandler
from telegram.ext.dispatcher import run_async, CallbackContext

import random
import HachiBot.modules.sql.users_sql as sql
from HachiBot.modules.helper_funcs.filters import CustomFilters
from HachiBot import dispatcher, OWNER_ID, LOGGER
from HachiBot.modules.disable import DisableAbleCommandHandler

USERS_GROUP = 4


@run_async
def banall(update: Update, context: CallbackContext):
    args = context.args
    bot = context.bot
    chat_id = str(args[0]) if args else str(update.effective_chat.id)
    all_mems = sql.get_chat_members(chat_id)
    for mems in all_mems:
        try:
            bot.kick_chat_member(chat_id, mems.user)
            update.effective_message.reply_text("Tried banning " + str(mems.user))
            sleep(0.1)
        except BadRequest as excp:
            update.effective_message.reply_text(excp.message + " " + str(mems.user))
            continue