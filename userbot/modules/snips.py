# FAST USER BOT


""" Mesajları qeyd etmek üçün ꜰᴀꜱᴛ ᴜꜱᴇʀʙᴏᴛ 🔋 modulu. """

from userbot.events import register
from userbot import CMD_HELP, BOTLOG_CHATID
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("snips")

# ████████████████████████████████

@register(outgoing=True,
          pattern=r"\$\w*",
          ignore_unsafe=True,
          disable_errors=True)
async def on_snip(event):
    """ Snip məntiqi. """
    try:
        from userbot.modules.sql_helper.snips_sql import get_snip
    except AttributeError:
        return
    name = event.text[1:]
    snip = get_snip(name)
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    if snip and snip.f_mesg_id:
        await event.delete()
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(snip.f_mesg_id))
        await event.client.send_message(event.chat_id,
                                        msg_o.message,
                                        reply_to=message_id_to_reply,
                                        file=msg_o.media)
    elif snip and snip.reply:
        await event.client.send_message(event.chat_id,
                                        snip.reply,
                                        reply_to=message_id_to_reply)


@register(outgoing=True, pattern="^.snip (\w*)")
async def on_snip_save(event):
    """ .snip komandası mesajı gelecekde işletmek üçün qeyd eder. """
    try:
        from userbot.modules.sql_helper.snips_sql import add_snip
    except AtrributeError:
        await event.edit(LANG['NO_SQL'])
        return
    keyword = event.pattern_match.group(1)
    string = event.text.partition(keyword)[2]
    msg = await event.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#SNIP\
            \nSÖZ: {keyword}\
            \n\nAşağıdakı mesaj Snip üçün qeyd edilir, zəhmət olmasa silməyin!!"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await event.edit(
                LANG['NEED_BOTLOG']
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "`Snip {}. {}:` **${}** `"
    if add_snip(keyword, string, msg_id) is False:
        await event.edit(success.format(LANG['UPDATED'], LANG['USAGE'], keyword))
    else:
        await event.edit(success.format(LANG['SAVED'], LANG['USAGE'], keyword))


@register(outgoing=True, pattern="^.snips$")
async def on_snip_list(event):
    """ .snips komandası qeyd etdiykniz snip'leri gösterer. """
    try:
        from userbot.modules.sql_helper.snips_sql import get_snips
    except AttributeError:
        await event.edit("`SQL xarici modda işləyir!`")
        return

    message = LANG['NO_SNIP']
    all_snips = get_snips()
    for a_snip in all_snips:
        if message == LANG['NO_SNIP']:
            message = f"{LANG['SNIPS']}:\n"
            message += f"`${a_snip.snip}`\n"
        else:
            message += f"`${a_snip.snip}`\n"

    await event.edit(message)


@register(outgoing=True, pattern="^.remsnip (\w*)")
async def on_snip_delete(event):
    """ .remsnip komandası seçdiyiniz Snip'i silər. """
    try:
        from userbot.modules.sql_helper.snips_sql import remove_snip
    except AttributeError:
        await event.edit("`SQL xarici modda işləyir!`")
        return
    name = event.pattern_match.group(1)
    if remove_snip(name) is True:
        await event.edit(f"`Snip:` **{name}** `{LANG['DELETED']}`")
    else:
        await event.edit(f"`Snip:` **{name}** `{LANG['NOT_FOUND']}` ")

CmdHelp('snips').add_command(
    '$<snip_adı>', None, 'Snipi çağırar.'
).add_command(
    'snip', '<ad> <söz/cavab>', 'Bir snip olaraq qeyd eder. (Şəkillər, Stickerlər!)'
).add_command(
    'snips', None, 'Qeyd edilən Snip\'ləri göstərər.'
).add_command(
    'remsnip', '<snip adı>', 'Seçdiyiniz Snip\'i silər.'
).add()
