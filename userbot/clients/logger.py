# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from telethon.tl.functions.channels import InviteToChannelRequest

from userbot import BOT_USERNAME
from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import WIKI2, WIKI3, WIKI4, WIKI5, bot, branch

MSG_ON = """
š **WIKI-UBOT Berhasil Di Aktifkan**
āā
ā  **Userbot Version -** `{}@{}`
ā  **Ketik** `{}alive` **untuk Mengecheck Bot**
ā  **Managed By** {}
āā
"""
try:
    user = bot.get_me()
    mention = f"[{user.first_name}](tg://user?id={user.id})"
except BaseException:
    pass


async def man_userbot_on():
    try:
        if bot:
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    f"š **WIKI-UBOT Berhasil Di Aktifkan**\nāā\nā  **Userbot Version -** `{version}@{branch}`\nā  **Ketik** `{cmd}alive` **untuk Mengecheck Bot**\nāā",
                )
    except BaseException:
        pass
    try:
        if WIKI2:
            if BOTLOG_CHATID != 0:
                await WIKI2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if WIKI3:
            if BOTLOG_CHATID != 0:
                await WIKI3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if WIKI4:
            if BOTLOG_CHATID != 0:
                await WIKI4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if WIKI5:
            if BOTLOG_CHATID != 0:
                await WIKI5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
