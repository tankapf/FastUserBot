# 𝚎𝚕𝚌𝚓𝚗  🇯🇵 Tərəfindən yaradılmışdır.
# Partner Brend
# FastUserBot

import time

from telethon.errors import (
    BadRequestError,
)
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import (
    EditBannedRequest,
)
from telethon.tl.types import (
    ChatBannedRights,
    MessageEntityMentionName,
)

from userbot import BOTLOG_CHATID
from userbot.events import register
from userbot.cmdhelp import CmdHelp

if BOTLOG_CHATID is None:
    BOTLOG = False
else:
    BOTLOG = True
    BOTLOG_CHATID = BOTLOG_CHATID

# =================== CONSTANT ===================
NO_ADMIN = "`Admin deyiləm❌`"
NO_PERM = "`Kifayət qədər admin icazəm yoxdu❌`"
NO_SQL = "`SQL mode! aktiv deyil`"


@register(outgoing=True, pattern=r"^\.tmute(?: |$)(.*)")
async def sako(fast):
    chat = await brend.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await brend.edit(NO_ADMIN)
        return
    user, reason = await get_user_from_event(fast)
    if user:
        pass
    else:
        return
    if reason:
        reason = reason.split(" ", 1)
        hmm = len(reason)
        if hmm == 2:
            cattime = reason[0]
            reason = reason[1]
        else:
            cattime = reason[0]
            reason = None
    else:
        await fast.edit("**Vaxt bildirmədiniz❌, istifadəyə baxmaq üçün** `.fast tadmin` **yazın**")
        return
    self_user = await fast.client.get_me()
    ctime = await extract_time(fast, cattime)
    if not ctime:
        await fast.edit(
            f"**Vaxt bildirmədiniz❌, istifadəyə baxmaq üçün** `.fast tadmin` **yazın**"
        )
        return
    if user.id == self_user.id:
        await fast.edit(f"**Özümü susdura bilmərəm❌**")
        return
    try:
        await fast.client(
            EditBannedRequest(
                fast.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, send_messages=True),
            )
        )
        if reason:
            await fast.edit(
                f"**{user.first_name} Susduruldu🔇\n\nQrup💭: {fast.chat.title}\n**"
                f"**Vaxt⌚️ {cattime}\n**"
                f"**Səbəb⚠️: {reason}**"
            )
            if BOTLOG:
                await fast.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"İstifadəçi👤: [{user.first_name}](tg://user?id={user.id})\n"
                    f"Qrup💭: {fast.chat.title}(`{fast.chat_id}`)\n"
                    f"**Müddət⌚️ : {cattime}**\n"
                    f"**Səbəb⚠️ : {reason}**",
                )
        else:
            await fast.edit(
                f"**{user.first_name}Susduruldu🔇\nQrup💭: {fast.chat.title}**\n"
                f"**Vaxt⌚️ {cattime}**\n"
            )
            if BOTLOG:
                await fast.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**İstifadəçi👤 :[{user.first_name}](tg://user?id={user.id})**\n"
                    f"**Qrup💭 : {fast.chat.title}({fast.chat_id})**\n"
                    f"**Müddət⌚️ : {cattime}**",
                )
                
    except UserIdInvalidError:
        return await fast.edit("`Xətayla qarşılaşdım`")


@register(outgoing=True, pattern=r"^\.tban(?: |$)(.*)")
async def sako(fast):
    chat = await fast.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await fast.edit(NO_ADMIN)
        return
    user, reason = await get_user_from_event(fast)
    if user:
        pass
    else:
        return
    if reason:
        reason = reason.split(" ", 1)
        hmm = len(reason)
        if hmm == 2:
            cattime = reason[0]
            reason = reason[1]
        else:
            cattime = reason[0]
            reason = None
    else:
        await brend.edit("**Vaxt bildirmədiniz, istifadəyə baxmaq üçün** `.fast tadmin` **yazın**")
        return
    self_user = await fast.client.get_me()
    ctime = await extract_time(fast, cattime)
    if not ctime:
        await fast.edit(
            f"**Yanlış vaxt göstərdiniz❌.\n\ndəqiqə - m\nsaat - h\n gün - d\nhəftə - w**"
        )
        return
    if user.id == self_user.id:
        await fast.edit(f"**Özümü susdura bilmərəm❌**")
        return
    await fast.edit("`Müvəqqəti qadağan edilir....`")
    try:
        await fast.client(
            EditBannedRequest(
                fast.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, view_messages=True),
            )
        )
    except Exception:
        await fast.edit(NO_PERM)
        return
    try:
        reply = await fast.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await fast.edit(
            "`Mesaj göndərmə hüququm yoxdur ama yenə də qadağan edildi❌`"
        )
        return
    if reason:
        await fast.edit(
            f"**{user.first_name} qadağan edildi❌\n\n Qrup {fast.chat.title}**\n"
            f"**Vaxt⌚️ {cattime}**\n"
            f"**Səbəb⚠️ `{reason}**"
        )
        if BOTLOG:
            await fast.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**İstifadəçi👤 : [{user.first_name}](tg://user?id={user.id})**\n"
                f"**Qrup💭 : {fast.chat.title}({fast.chat_id})**\n"
                f"**Vaxt⌚️ :  {cattime}**\n"
                f"**Səbəb⚠️ {reason}**",
            )
    else:
        await fast.edit(
            f"{user.first_name} qadağan edildi❌\n\n Qrup💭: {fast.chat.title}\n"
            f"**Vaxt⌚️ {cattime}**\n"
        )
        if BOTLOG:
            await fast.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**İstifadəçi👤 : [{user.first_name}](tg://user?id={user.id})**\n"
                f"**Qrup💭 : {fast.chat.title}(`{fast.chat_id}`)**\n"
                f"**Vaxt⌚️ : {cattime}**",
            )


async def get_user_from_event(event):
    """İstifadəçini göstərin"""
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`İstifaəçi göstərin`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(
                    probable_user_mention_entity,
                    MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError):
            await event.edit("**istifadəçinin məlumatını əldə etmək mümkün olmadı.**")
            return None
    return user_obj, extra


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


async def extract_time(cat, time_val):
    if any(time_val.endswith(unit) for unit in ("m", "h", "d", "w")):
        unit = time_val[-1]
        time_num = time_val[:-1]
        if not time_num.isdigit():
            cat.edit("Səhv vaxt göstərildi")
            return ""
        if unit == "m":
            bantime = int(time.time() + int(time_num) * 60)
        elif unit == "h":
            bantime = int(time.time() + int(time_num) * 60 * 60)
        elif unit == "d":
            bantime = int(time.time() + int(time_num) * 24 * 60 * 60)
        elif unit == "w":
            bantime = int(time.time() + int(time_num) * 7 * 24 * 60 * 60)
        else:
            return ""
        return bantime
    cat.edit(
        "Invalid time type specified. Expected m , h , d or w but got: {}".format(
            time_val[-1]
        )
    )
    return ""

CmdHelp('tadmin').add_command(
    'tmute', '<vaxt>''<səbəb>', 'İstifadəçini müvəqqəti susdurat..'
).add_command(
    'tban', '<vaxt>''<səbəb>', 'İstifadəçini müvəqqəti olaraq ban edər'
).add_info('**⚠️dəqiqə - m\nsaat - h\n gün - d\nhəftə - ⚠️**'
).add()
