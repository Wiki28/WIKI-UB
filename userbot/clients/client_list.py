# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, WIKI2, WIKI3, WIKI4, WIKI5):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if WIKI2 is not None:
            id2 = await WIKI2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if WIKI3 is not None:
            id3 = await WIKI3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if WIKI4 is not None:
            id4 = await WIKI4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if WIKI5 is not None:
            id5 = await WIKI5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        WIKI_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        WIKI_USER = client.first_name
    man_mention = f"[{WIKI_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, WIKI_USER, wiki_mention
