# Copyright (C) 2021-2022 CyberUserBot
# This file is a part of < https://github.com/FaridDadashzade/CyberUserBot/ >
# Please read the GNU General Public License v3.0 in
# <https://www.github.com/FaridDadashzade/CyberUserBot/blob/master/LICENSE/>.

import asyncio
import threading

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, BLACKLIST_CHAT
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ---------------------------------- #

from userbot.language import get_value
LANG = get_value("cyberlangs")

# ---------------------------------- #

@register(outgoing=True, pattern="^.tspam")
async def tmeme(e):
    if e.chat_id in BLACKLIST_CHAT:
        return await e.edit(LANG["PROHIBITED_COMMAND"])
    message = e.text
    messageSplit = message.split(" ", 1)
    tspam = str(messageSplit[1])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()
    if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#TSPAM \n\n"
                "TSpam uğurla edildi"
                )

@register(outgoing=True, pattern="^.spam")
async def spammer(e):
    if e.chat_id in BLACKLIST_CHAT:
        return await e.edit(LANG["PROHIBITED_COMMAND"])
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit = message.split(" ", 2)
        counter = int(messageSplit[1])
        spam_message = str(messageSplit[2])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#SPAM \n\n"
                "Spam uğurla edildi"
                )
                               
@register(outgoing=True, pattern="^.bigspam")
async def bigspam(e):
    if e.chat_id in BLACKLIST_CHAT:
        return await e.edit(LANG["PROHIBITED_COMMAND"])
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit = message.split(" ", 2)
        counter = int(messageSplit[1])
        spam_message = str(messageSplit[2])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#BIGSPAM \n\n"
                "Bigspam uğurla edildi"
                )
        
        
@register(outgoing=True, pattern="^.picspam")
async def tiny_pic_spam(e):
    if e.chat_id in BLACKLIST_CHAT:
        return await e.edit(LANG["PROHIBITED_COMMAND"])
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        link = str(text[2])
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, link)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#PICSPAM \n\n"
                "PicSpam uğurla edildi"
                )


@register(outgoing=True, pattern="^.delayspam")
async def delayspammer(e):
    # CYBERUSERBOT
    if e.chat_id in BLACKLIST_CHAT:
        return await e.edit(LANG["PROHIBITED_COMMAND"])
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit= message.split(" ", 3)
        spam_delay = float(messageSplit[1])
        counter = int(messageSplit[2])
        spam_message = str(messageSplit[3])
        await e.delete()
        delaySpamEvent = threading.Event()
        for i in range(1, counter):
            await e.respond(spam_message)
            delaySpamEvent.wait(spam_delay)
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#DelaySPAM \n\n"
                "DelaySpam uğurla edildi"
                )

CmdHelp('spammer').add_command(
    'tspam', '<mətin>', 'Verilən mesajı tək tək göndərərək spam edər.'
).add_command(
    'spam', '<miqdar> <mətin>', 'Verilən miqdarda spam göndərir.'
).add_command(
    'bigspam', '<miqdar> <mətin>', 'Verilən miqdarda spam göndərir.'
).add_command(
    'picspam', '<miqdar> <link>', 'Verilən miqdarda fotolu spam göndərir.'
).add_command(
    'delayspam', '<gecikmə> <miqdar> <mətin>', 'Verilən miqdar və verilən gecikmə ilə gecikməli spam edər.'
).add_warning(
    'Məsuliyyət sizə aiddir!'
).add()
