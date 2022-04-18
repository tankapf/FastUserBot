# FAST USER BOT #


from random import randint
from asyncio import sleep
from os import execl
import sys
import io
import sys
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("misc")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.resend")
async def resend(event):
    await event.delete()
    m = await event.get_reply_message()
    if not m:
        event.edit(LANG['REPLY_TO_FILE'])
        return
    await event.respond(m)

@register(outgoing=True, pattern="^.random")
async def randomise(items):
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            LANG['NEED_MUCH_DATA_FOR_RANDOM']
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit(f"**{LANG['QUERY']}: **\n`" + items.text[8:] + f"`\n**{LANG['RESULT']}: **\n`" +
                     itemo[index] + "`")


@register(outgoing=True, pattern="^.sleep( [0-9]+)?$")
async def sleepybot(time):
    """ .sleep komandası ꜰᴀꜱᴛ ᴜꜱᴇʀʙᴏᴛ 🔋'u yatızdırar :) """
    if " " not in time.pattern_match.group(1):
        await time.reply(LANG['SLEEP_DESC'])
    else:
        counter = int(time.pattern_match.group(1))
        await time.edit(LANG['SLEEPING'])
        await sleep(2)
        if BOTLOG:
            await time.client.send_message(
                BOTLOG_CHATID,
                "Botu" + str(counter) + "saniyə yatızdırdın.",
            )
        await sleep(counter)
        await time.edit(LANG['GOODMORNIN_YALL'])


@register(outgoing=True, pattern="^.shutdown$")
async def shutdown(event):
    """ .shutdown komandası botu söndrər :( """
    await event.client.send_file(event.chat_id, 'https://www.winhistory.de/more/winstart/mp3/winxpshutdown.mp3', caption=LANG['GOODBYE_MFRS'], voice_note=True)
    await event.delete()

    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n"
                                        "Bot söndürüldü.")
    try:
        await bot.disconnect()
    except:
        pass


@register(outgoing=True, pattern="^.restart$")
async def restart(event):
    await event.edit(LANG['RESTARTING'])
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n"
                                        "Bot yenidən başladıldı.")

    try:
        await bot.disconnect()
    except:
        pass

    execl(sys.executable, sys.executable, *sys.argv)


@register(outgoing=True, pattern="^.support$")
async def bot_support(wannahelp):
    """ .support komandası support qrupunun linkini verer. """
    await wannahelp.edit(LANG['SUPPORT_GROUP'])


@register(outgoing=True, pattern="^.creator$")
async def creator(e):
    await e.edit(LANG['CREATOR'])


@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    await e.edit(LANG['CREATOR'])


# Copyright (c) Gegham Zakaryan | 2019
@register(outgoing=True, pattern="^.repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(' ', 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(wannasee):
    """ .repo komandası Repomuzun linkini verər. """
    await wannasee.edit(LANG['REPO'])

@register(outgoing=True, pattern="^.raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit(
            "`Həll edilmiş mesajlar üçün UserBot loglarını yoxlayın!`")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Həll Olunan Mesaj`")

CmdHelp('misc').add_command(
    'random', '<əşya1> <əşya2>', 'Yazdığınız əşyalardan random birini seçər', 'random ꜰᴀꜱᴛ ᴜꜱᴇʀʙᴏᴛ 🔋 Əla İşləyir'
).add_command(
    'sleep', '<vaxt>', 'ShreedUserBot\'u yazdığınız saniyə qədər yatızdırar', 'sleep 20'
).add_command(
    'shutdown', None, 'Botu Söndürər.'
).add_command(
    'repo', None, 'ShreedUserBot\'un GitHub reposunun linki.'
).add_command(
    'readme', None, 'ShreedUserBot\'un GitHub\'dakı README.md faylının linki.'
).add_command(
    'creator', None, 'Bu botu kim hazırlayıb?'
).add_command(
    'repeat', '<rəqəm> <mətn>', 'Bir mətni müəyyən sayda təkrar edər. Spam komandası ilə qarışdırma.'
).add_command(
    'restart', None, 'Botu yenidən başladar.'
).add_command(
    'resend', None, 'Bir medianı yenidən göndərər.'
).add_command(
    'resend', None, 'Bir medianı yenidən göndərər.'
).add_command(
    'raw', '<cavab>', 'Cavab verilən mesaj haqqında məlumat verər.'
).add()
