# create module by dear moezilla
# copyright sylviorus
# join sylviorus_support

import os
import json
import re
import os
import html
import requests
from telegram.ext.filters import Filters
from telegram.parsemode import ParseMode

import HachiBot.modules.sql.syl_sql as sql

from time import sleep
from telegram import ParseMode
from telegram import (CallbackQuery, Chat, MessageEntity, InlineKeyboardButton,
                      InlineKeyboardMarkup, Message, ParseMode, Update, Bot, User)
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler,
                          DispatcherHandlerStop, Filters, MessageHandler,
                          run_async)
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.utils.helpers import mention_html, mention_markdown, escape_markdown

from HachiBot.modules.helper_funcs.filters import CustomFilters
from HachiBot.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from HachiBot import dispatcher, updater, SUPPORT_CHAT, SYL
from HachiBot.modules.log_channel import gloggable

 
@user_admin_no_reply
@gloggable
def sylrm(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"rm_syl\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_syl = sql.rem_syl(chat.id)
        if is_syl:
            is_syl = sql.rem_syl(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"SYL_DISABLED\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            query.answer("Sylviorus System Enable")
            query.message.delete()

    return ""


@user_admin_no_reply
@gloggable
def syladd(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"add_syl\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_syl = sql.set_syl(chat.id)
        if is_syl:
            is_syl = sql.set_syl(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"SYL_ENABLE\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            query.answer("Sylviorus System Disable")
            query.message.delete()

    return ""


@user_admin
@gloggable
def bluemoon(update: Update, context: CallbackContext):
    user = update.effective_user
    message = update.effective_message
    video = "https://telegra.ph/file/08ee83677137fdf3c70ba.mp4"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Enable",
            callback_data="add_syl({})")],
       [
        InlineKeyboardButton(
            text="Disable",
            callback_data="rm_syl({})")],
       [
        InlineKeyboardButton(
            text="What Is Sylviorus",
            url="https://t.me/Sylviorussystems/3329")],
       [ 
        InlineKeyboardButton(
            text="Sylviorus Support",
            url="https://t.me/Sylviorus_support")],
       [
        InlineKeyboardButton(
            text="Sylviorus Report",
            url="https://t.me/+C5qOzLYDQrVkMWE1")],
       [
        InlineKeyboardButton(
            text="Sylviorus Log",
            url="https://t.me/sylvioruslog")]])
    message.reply_video(
        video, 
        caption= "Connection to Sylviorus System can be turned Enable and Disable",
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


def bluemoon_callback(update: Update, context: CallbackContext, should_message=True):
    message = update.effective_message
    chat_id = update.effective_chat.id
    user = update.effective_user

    is_syl = sql.is_syl(chat_id)
    if is_syl:
        return
        x = None
    try:
        x = SYL.check(int(user.id))
    except:
        x = None

    if x:
        update.effective_chat.ban_member(x.user)
        update.effective_chat.unban_member(x.user)
        if should_message:
            alertvideo = "https://telegra.ph/file/fed47f651097bb2f5e6ca.mp4"
            kkn = InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    text="Appeal Chat",
                    url="https://t.me/Sylviorus_support")]])
            update.effective_message.reply_video(
                alertvideo,
                caption= f"<b>Alert</b>: This User Is Blacklisted\n"
                f"<b>User ID</b>: <code>{x.user}</code>\n"
                f"<b>Enforcer</b>: <code>{x.enforcer}</code>\n"
                f"<b>Reason</b>: <code>{x.reason}</code>\n"
                f"<b>Report</b>: Using /sylreport feature in @BlueMoonVampireBot bot\n",            
                reply_markup=kkn,
                parse_mode=ParseMode.HTML,
            )
        return

BLUEMOON_HANDLER = CommandHandler("syl", bluemoon, run_async=True)
ADD_SYL_HANDLER = CallbackQueryHandler(syladd, pattern=r"add_syl", run_async=True)
RM_SYL_HANDLER = CallbackQueryHandler(sylrm, pattern=r"rm_syl", run_async=True)
BLUEMOON_HANDLERK = MessageHandler(filters=Filters.all & Filters.chat_type.groups, callback=bluemoon_callback)

dispatcher.add_handler(ADD_SYL_HANDLER)
dispatcher.add_handler(BLUEMOON_HANDLER)
dispatcher.add_handler(RM_SYL_HANDLER)
dispatcher.add_handler(BLUEMOON_HANDLERK, group=102)
