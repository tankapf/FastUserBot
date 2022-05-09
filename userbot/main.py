# Copyright (C) 2022 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

#FastUserBot




import importlib
from importlib import import_module
from sqlite3 import connect
import os
import requests
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import GetMessagesRequest
from . import BRAIN_CHECKER, LOGS, bot, PLUGIN_CHANNEL_ID, CMD_HELP, LANGUAGE, FAST_VERSION, PATTERNS
from .modules import ALL_MODULES
import userbot.modules.sql_helper.mesaj_sql as MSJ_SQL
import userbot.modules.sql_helper.qaleriya_sql as QALERIYA_SQL
from pySmartDL import SmartDL
from telethon.tl import functions

from random import choice
import chromedriver_autoinstaller
from json import loads, JSONDecodeError
import re
import userbot.cmdhelp

DIZCILIK_STR = [
    "😎Stickeri fırladıram😎..",
    "⚡Sticker paketə əlavə edilir⚡...",
    "♥Bu sticker artıq mənimdir!♥",
    "📩⛓Bunu stickerlərimə əlavə etməliy... ",
    "⛓Sticker həps edilir...",
    "▪▫Mən bir sticker oğrusuyam stickerin məndədi▫▪ ;D!",
    "🖇Nə gözəl stickerdi bu!🖇"
]

AFKSTR = [
    "💫İndi vacib işimlərim var, gələndə yazacam🖤..",
    "🥲Birazdan gələcəm amma gəlməsəm...\nDarıxma😕",
    "😡Ay xaam yeri get..\nistirahət elirəm:)",
    "Sahibim hal-hazırda AFK dı!",
    "🎈həyatdakı ən yaxşı şeyləri gözləməyə dəyər…\nGələcəm.🎈",
    "Bəli❓",
    "▪▫Sahibim gəlir gözlə▫▪.",
    "Hal-hazırda sahibim burada deyil❗.",
    "💠Salam, uzaq mesajıma xoş gəldiniz💠, sizə necə kömək edə bilərəm?",
    "Mən sahibimin xüsusi botuyam!, sizdə bot istəyirsizsə: ⚜ @TheFastUserBot ⚜ qur.",
    "Hal hazırda burdan çoox uzaqdayam.\nQışqırsan bəlkə eşitdim.",
    "ℹBu tərəfə gedirəm\n🔜",
    "ℹBu tərəfə gedirəm\n🔙",
    "♻Mesajınızı Sahibim ə göndərirəm....",
    "✖Sahibim burda deyil mənə yazmağı kəs artıq.✖",
    "Sahibim burada deyil..\nqayıdanda sizinlə əlaqə saxlayacaqdır✅",
    "📴Sahibim burda deyil📴 Telefona baxmağa vaxdı yoxdur.",
    "😬Belə gözəl bir gündə niyə məni narahat edirsən⚠❔",
    "😴Çox heyif ki sahibim burada deyil..😴.",
    "Hal hazırda burdayam amma mesajını görməzdən gələcəm :)",
]

UNAPPROVED_MSG = ("`Hey,` {mention}`! Bu bir bot. Narahat olma.\n\n`"
                  "`Sahibim sənə PM atma icazəsi verməyib. `"
                  "`Zəhmət olmasa sahibimin aktiv olmağını gözləyin, o adətən PM'ləri qəbul edir.\n\n`"
                  "`Bildiyim qədəri ilə o dəlilərə PM atma icazəsi vermir.`\n@TheFastUserBot `Quraraq sənində belə bir botun ola bilər :)`")

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()
INVALID_PH = '\nXETA: Yazılan telefon nömresi keçersizdir' \
             '\n  Meslehet: Ölke kodundan isdifade etmekle nömreni yazın' \
             '\n       Telefon nömrenizi yeniden yoxlayın.'

for i in ALL_ROWS:
    BRAIN_CHECKER.append(i[0])
connect("learning-data-root.check").close()

def extractCommands(file):
    FileRead = open(file, 'r').read()
    
    if '/' in file:
        file = file.split('/')[-1]

    Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", FileRead)
    Komutlar = []

    if re.search(r'CmdHelp\(.*\)', FileRead):
        pass
    else:
        dosyaAdi = file.replace('.py', '')
        CmdHelp = userbot.cmdhelp.CmdHelp(dosyaAdi, False)

        # Komandaları alırıq #
        for Command in Pattern:
            Command = Command[1]
            if Command == '' or len(Command) <= 1:
                continue
            Komut = re.findall("(^.*[a-zA-Z0-9şğüöçı]\w)", Command)
            if (len(Komut) >= 1) and (not Komut[0] == ''):
                Komut = Komut[0]
                if Komut[0] == '^':
                    KomutStr = Komut[1:]
                    if KomutStr[0] == '.':
                        KomutStr = KomutStr[1:]
                    Komutlar.append(KomutStr)
                else:
                    if Command[0] == '^':
                        KomutStr = Command[1:]
                        if KomutStr[0] == '.':
                            KomutStr = KomutStr[1:]
                        else:
                            KomutStr = Command
                        Komutlar.append(KomutStr)

            # FAST
            Fastpy = re.search('\"\"\"FastPY(.*)\"\"\"', FileRead, re.DOTALL)
            if not Fastpy == None:
                Fastpy = Fastpy.group(0)
                for Satir in Fastpy.splitlines():
                    if (not '"""' in Satir) and (':' in Satir):
                        Satir = Satir.split(':')
                        Isim = Satir[0]
                        Deger = Satir[1][1:]
                                
                        if Isim == 'INFO':
                            CmdHelp.add_info(Deger)
                        elif Isim == 'WARN':
                            CmdHelp.add_warning(Deger)
                        else:
                            CmdHelp.set_file_info(Isim, Deger)
            for Komut in Komutlar:
                # if re.search('\[(\w*)\]', Komut):
                    # Komut = re.sub('(?<=\[.)[A-Za-z0-9_]*\]', '', Komut).replace('[', '')
                CmdHelp.add_command(Komut, None, 'Bu plugin xaricden yüklenmişdir. Her hansı bir açıqlama yoxdur.')
            CmdHelp.add()

try:
    bot.start()
    idim = bot.get_me().id
    fastbl = requests.get('https://raw.githubusercontent.com/FastUserBot/FastUserBot/main/fastblacklist.json').json()
    if idim in fastbl:
        bot.disconnect()

    # ChromeDriver'ı Ayarlayaq #
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    
    # Qaleriya üçün deyerler
    QALERIYA = {}

    # PLUGIN MESAJLARINI AYARLAYAQ
    PLUGIN_MESAJLAR = {}
    ORJ_PLUGIN_MESAJLAR = {"alive": "`ꜰᴀꜱᴛ ᴜꜱᴇʀʙᴏᴛ İşləyir 🔋`\n\n👤 `Mənim Sahibim:` {mention}\n\n🐍 `Python:`{python}\n\n♻️ `Telethon:`{telethon}\n\n `ꜰᴀꜱᴛ ᴜꜱᴇʀʙᴏᴛ Versiyası:` {fast}\n\n🎴 `Vəziyyət: Stabil`\n\n`Dəstək qrupumuza` [🇦🇿 Kömək 🇦🇿](https://t.me/TheFastSup)", "afk": f"`{str(choice(AFKSTR))}`", "kickme": "`Bye Bye Mən getdim :)`", "pm": UNAPPROVED_MSG, "dızcı": str(choice(DIZCILIK_STR)), "ban": "{mention}`, banlandı!`", "mute": "{mention}`, səssizləşdirildi!`", "approve": "{mention} `mənə mesaj yazmağın üçün icazə verildi`", "disapprove": "{mention} `artıq mənə yaza bilməssən!`", "block": "{mention}`Bloklandın!🥰`", "restart": "`🇦🇿𝙁𝘼𝙎𝙏 𝙐𝙎𝙀𝙍𝘽𝙊𝙏🇦🇿 Yenidən Başladılır...`"}

    PLUGIN_MESAJLAR_TURLER = ["alive", "afk", "kickme", "pm", "dızcı", "ban", "mute", "approve", "disapprove", "block", "restart"]
    for mesaj in PLUGIN_MESAJLAR_TURLER:
        dmsj = MSJ_SQL.getir_mesaj(mesaj)
        if dmsj == False:
            PLUGIN_MESAJLAR[mesaj] = ORJ_PLUGIN_MESAJLAR[mesaj]
        else:
            if dmsj.startswith("MEDYA_"):
                medya = int(dmsj.split("MEDYA_")[1])
                medya = bot.get_messages(PLUGIN_CHANNEL_ID, ids=medya)

                PLUGIN_MESAJLAR[mesaj] = medya
            else:
                PLUGIN_MESAJLAR[mesaj] = dmsj
    if not PLUGIN_CHANNEL_ID == None:
        LOGS.info("`Pluginler Yüklenir...`")
        try:
            KanalId = bot.get_entity(PLUGIN_CHANNEL_ID)
        except:
            KanalId = "me"

        for plugin in bot.iter_messages(KanalId, filter=InputMessagesFilterDocument):
            if plugin.file.name and (len(plugin.file.name.split('.')) > 1) \
                and plugin.file.name.split('.')[-1] == 'py':
                Split = plugin.file.name.split('.')

                if not os.path.exists("./userbot/modules/" + plugin.file.name):
                    dosya = bot.download_media(plugin, "./userbot/modules/")
                else:
                    LOGS.info("Bu Plugin Onsuzda Yüklənib " + plugin.file.name)
                    extractCommands('./userbot/modules/' + plugin.file.name)
                    dosya = plugin.file.name
                    continue 
                
                try:
                    spec = importlib.util.spec_from_file_location("userbot.modules." + Split[0], dosya)
                    mod = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(mod)
                except Exception as e:
                    LOGS.info(f"`Yükləmə Uğursuz! Plugin xətalıdır.\n\nXəta: {e}`")

                    try:
                        plugin.delete()
                    except:
                        pass

                    if os.path.exists("./userbot/modules/" + plugin.file.name):
                        os.remove("./userbot/modules/" + plugin.file.name)
                    continue
                extractCommands('./userbot/modules/' + plugin.file.name)
    else:
        bot.send_message("me", f"`Zehmet olmasa pluginlerin qalıcı olması üçün PLUGIN_CHANNEL_ID'i ayarlayın.`")
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

async def FotoDegistir (foto):
    FOTOURL = QALERIYA_SQL.TUM_QALERIYA[foto].foto
    r = requests.get(FOTOURL)

    with open(str(foto) + ".jpg", 'wb') as f:
        f.write(r.content)    
    file = await bot.upload_file(str(foto) + ".jpg")
    try:
        await bot(functions.photos.UploadProfilePhotoRequest(
            file
        ))
        return True
    except:
        return False

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("Botunuz işleyir! Hansısa söhbete  .alive yazaraq Test ede bilersiz!."
          " Kömeye ehtiyacınız varsa, destek qrupuna gelin: t.me/FastSupp")
LOGS.info(f"Bot versiyası: FAST {FAST_VERSION}")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
