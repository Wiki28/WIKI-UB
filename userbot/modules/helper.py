""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, wiki_cmd


@wiki_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await edit_or_reply(
        event,
        f"**Hai {me.first_name} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"✣ **Wiki Group :** [Wiki Group](t.me/WikiTapiGroup)\n"
        f"✣ **Wiki Channel :** [Wiki Channel](t.me/WikiTapiChannel)\n"
        f"✣ **Owner Repo :** [Wiki W](t.me/Hanya_W)\n"
        f"✣ **Repo :** [Man-Userbot](https://github.com/mrismanaziz/Man-Userbot)\n",
    )


@wiki_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Wiki-Userbot:** [KLIK DISINI](https://telegra.ph/List-Variabel-Heroku-untuk-Wiki-Userbot-02-03)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk Man-Userbot.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository Man-Userbot.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String Man-Userbot.\
    "
    }
)
