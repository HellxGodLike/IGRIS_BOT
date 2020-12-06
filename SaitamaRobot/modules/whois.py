import html
import json
import os
import psutil
import random
import time
import datetime
from typing import Optional, List
import re
import requests
from telegram.error import BadRequest
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from SaitamaRobot.modules.helper_funcs.chat_status import user_admin, sudo_plus, is_user_admin
from SaitamaRobot import dispatcher, OWNER_ID, DRAGONS, DEMONS, DEV_USERS, WOLFS
from SaitamaRobot.__main__ import STATS, USER_INFO, TOKEN
from SaitamaRobot.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler
from SaitamaRobot.modules.helper_funcs.extraction import extract_user
from SaitamaRobot.modules.helper_funcs.filters import CustomFilters
import SaitamaRobot.modules.sql.users_sql as sql
import SaitamaRobot.modules.helper_funcs.cas_api as cas

@run_async
def info(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    chat = update.effective_chat
    user_id = extract_user(update.effective_message, args)

    if user_id:
        user = bot.get_chat(user_id)

    elif not message.reply_to_message and not args:
        user = message.from_user

    elif not message.reply_to_message and (not args or (
            len(args) >= 1 and not args[0].startswith("@") and not args[0].isdigit() and not message.parse_entities(
        [MessageEntity.TEXT_MENTION]))):
        message.reply_text("I can't extract a user from this.")
        return

    else:
        return
    
    text = (f"<b>User Information:</b>\n"
            f"ID: <code>{user.id}</code>\n"
            f"Name: {html.escape(user.first_name)}")

    if user.last_name:
        text += f"\nLast Name: {html.escape(user.last_name)}"

    if user.username:
        text += f"\nUsername: @{html.escape(user.username)}"

    text += f"\nPermanent user link: {mention_html(user.id, 'link🚪')}"

    num_chats = sql.get_user_num_chats(user.id)
    text += f"\nChat count: <code>{num_chats}</code>"
    text += "\nNumber of profile pics: {}".format(bot.get_user_profile_photos(user.id).total_count)
   
    try:
        user_member = chat.get_member(user.id)
        if user_member.status == 'administrator':
            result = requests.post(f"https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={chat.id}&user_id={user.id}")
            result = result.json()["result"]
            if "custom_title" in result.keys():
                custom_title = result['custom_title']
                text += f"\nAdmin title⚜️ <b>{custom_title}</b> here."
    except BadRequest:
        pass

    

    
    if user.id ==1286562476:
        text += "\n🚶🏻‍♂️Uff,This person is sudo \n HE IS is the cutie!."

    if user.id == OWNER_ID:
        text += "\nThis person is my Owner\nI would never do anything against him!."
        
    elif user.id in DEV_USERS:
        text += "\nThis person is my dev\nI would never do anything against him!."
        
    elif user.id in DRAGONS:
        text += "\nThis person is one of my sudo users! " \
                    "Nearly as powerful as my owner🕊so watch it.."
        
    elif user.id in DEMONS:
        text += "\nThis person is one of my support users! " \
                        " He can gban you off the map."
        
  
       
    elif user.id in WOLFS:
        text += "\nThis person has been whitelisted! " \
                        "That means I'm not allowed to ban/kick them."
    


    text +="\n"
    text += "\nCAS banned: "
    result = cas.banchecker(user.id)
    text += str(result)
    for mod in USER_INFO:
        if mod.__mod_name__ == "WHOIS":
            continue

        try:
            mod_info = mod.__user_info__(user.id)
        except TypeError:
            mod_info = mod.__user_info__(user.id, chat.id)
        if mod_info:
            text += "\n" + mod_info
    try:
        profile = bot.get_user_profile_photos(user.id).photos[0][-1]
        _file = bot.get_file(profile["file_id"])
        _file.download(f"{user.id}.png")

        message.reply_document(
         document=open(f"{user.id}.png", "rb"),
         caption=(text),
          parse_mode=ParseMode.HTML,
          disable_web_page_preview=True)

    except IndexError:
        message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)

INFO_HANDLER = DisableAbleCommandHandler("info", info, pass_args=True)
dispatcher.add_handler(INFO_HANDLER)
__handlers__=[INFO_HANDLER]
