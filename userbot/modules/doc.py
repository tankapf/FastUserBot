#Fast User Bot
from userbot.cmdhelp import CmdHelp
from userbot.events import register
from userbot import bot
import os


@register(
    pattern=".ttf(?: |$)(.*)",
    outgoing=True,
)
async def TextToFile(e):
    ad = e.text[5:]
    yanit = await e.get_reply_message()
    if yanit.text:
        with open(ad, "w") as fayl:
            fayl.write(yanit.message)
        await e.delete()
        await bot.send_file(e.chat_id,
                            ad,
                            force_document=True)
        os.remove(ad)
        return


# --------------------------------------------------------------


@register(outgoing=True, pattern=".oxu")
@register(outgoing=True, pattern=".open")
@register(outgoing=True, pattern=".ftt")
async def FileToText(event):
    await event.delete()
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    oxu = a.read()
    a.close()
    a = await event.reply("**Fayl oxunur...**")
    if len(oxu) > 4095:
        await a.edit("**Məzmun çox böyükdür.**")
    else:
        await event.client.send_message(event.chat_id, f"```{oxu}```")
        await a.delete()
    os.remove(b)
    
    
# --------------------------------------------------------------
Help = CmdHelp('doc')
Help.add_command('ttf',
                 '<mətn\'ə cavab>',
                 'Telegram mətnini qoyduğunuz adda fayla çevirər.',
                 'ttf <mətn\'ə cavab> test.py')
Help.add_command(
    'oxu | .ftt | .open',
    '<fayl\'a cavab>',
    'Telegram faylını Telegram mətninə çevirər. (Limit 4 KiloBaytdır.)',
    "oxu <fayl'a cavab>")
Help.add()
