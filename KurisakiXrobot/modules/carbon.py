from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from KurosakiXrobot import SHASA_PHOTO, SUPPORT_CHAT, pbot
from KurosakiXrobot.utils.carbon import make_carbon
from KurosakiXrobot.utils.errors import capture_err


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


@pbot.on_message(filters.command("alive"))
async def alive(_, message):
    await message.reply_photo(
        photo=SHASA_PHOTO,
        caption=f"""⚡ **Hᴇʏ I Aᴍ Nᴇᴢᴜᴋᴏ** 

**✨ Created By : [Itachi Kun](t.me/Millionaire_Kambe)**
**🐍 Python Version :** `{y()}`
**📃 Ptb Version :** `{o}`
**💫 Telethon Version :** `{s}`
**💥 Pyrogram Version :** `{z}`

**Create your own with click button bellow.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT_CHAT}"),
                    InlineKeyboardButton("Updates", url="https://t.me/IchigoXupdates"),
                ]
            ]
        ),
    )
