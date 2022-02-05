# Credits: @mrconfused
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import inspect
import re
from pathlib import Path

from telethon import events

from userbot import (
    BL_CHAT,
    CMD_HANDLER,
    CMD_LIST,
    LOAD_PLUG,
    WIKI2,
    WIKI3,
    WIKI4,
    WIKI5,
    SUDO_HANDLER,
    SUDO_USERS,
    bot,
    tgbot,
)


def wiki_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if pattern is not None:
        global wiki_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            wiki_reg = sudo_reg = re.compile(pattern)
        else:
            wiki_ = "\\" + CMD_HANDLER
            sudo_ = "\\" + SUDO_HANDLER
            wiki_reg = re.compile(wiki_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = wiki_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (wiki_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern)
                    .replace("$", "")
                    .replace("\\", "")
                    .replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})

    def decorator(func):
        if bot:
            if not disable_edited:
                bot.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=wiki_reg)
                )
            bot.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=wiki_reg)
            )
        if bot:
            if allow_sudo:
                if not disable_edited:
                    bot.add_event_handler(
                        func,
                        events.MessageEdited(
                            **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                        ),
                    )
                bot.add_event_handler(
                    func,
                    events.NewMessage(
                        **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                    ),
                )
        if WIKI2:
            if not disable_edited:
                WIKI2.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=wiki_reg)
                )
            WIKI2.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=wiki_reg)
            )
        if WIKI3:
            if not disable_edited:
                WIKI3.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=wiki_reg)
                )
            WIKI3.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=wiki_reg)
            )
        if WIKI4:
            if not disable_edited:
                WIKI4.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=wiki_reg)
                )
            WIKI4.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=wiki_reg)
            )
        if WIKI5:
            if not disable_edited:
                WIKI5.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=wikip_reg)
                )
            WIKI511.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=wiki_reg)
            )
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


def wiki_handler(
    **args,
):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if WIKI2:
            WIKI2.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if WIKI3:
            WIKI3.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if WIKI4:
            WIKI4.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if WIKI5:
            WIKI5.add_event_handler(func, events.NewMessage(**args, incoming=True))
        return func

    return decorator


def asst_cmd(**args):
    pattern = args.get("pattern", None)
    r_pattern = r"^[/!]"
    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern
    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def chataction(**args):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.ChatAction(**args))
        if WIKI2:
            WIKI2.add_event_handler(func, events.ChatAction(**args))
        if WIKI3:
            WIKI3.add_event_handler(func, events.ChatAction(**args))
        if WIKI4:
            WIKI4.add_event_handler(func, events.ChatAction(**args))
        if WIKI5:
            WIKI5.add_event_handler(func, events.ChatAction(**args))
        return func

    return decorator


def callback(**args):
    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator
