from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only
from config import SUDO_USERS 
import asyncio

@Client.on_message(filters.group & filters.command(["asal", "asistan"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Meni Evvelce Admin Et</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "AsistanUserbot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Senin İsteyin Üçün Geldim🤍")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asistan Onsuzda Bu Grubda Var 🍷</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>✨ Flood Wait Xetası ✨\n User {user.first_name} Asistan üçün heddinden artığ qatılma istekleri olduğundan grubunuza qatıla bilmedi! Asistanın grubda yasağlanmadığından emin olun."
            "\n\n Yada Asistan Hesabını Gruba Özün Elave et </b>",
        )
        return
    await message.reply_text(
            "<b>Asistan onsuzda bu grubdadır 🍷</b>",
        )
    
@USER.on_message(filters.group & filters.command(["çıx", "asistanby"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>İstifadeçi grubunuzdan çıxa bilmedi!."
            "\n\nOnu Özün Çıxara bilersen</b>",
        )
        return
 
@USER.on_message(filters.group & filters.command(["çıx"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>İstifadeçi grubunuzdan Çıxa Bilmedi! Ses gözlemiş ola biler."
            "\n\nAmma Meni Grubunuzdan El İlede Ata Bilersen</b>",
        )
        return


@Client.on_message(filters.command(["rowlyn"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left = 0
        failed = 0
        lol = await message.reply("Bütün Grublardan ayrılıram...")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left + 1
                await lol.edit(
                    f"Ayrılıram... Left: {left} chats. Failed: {failed} chats."
                )
            except:
                failed = failed + 1
                await lol.edit(
                    f"Ayrılıram... Left: {left} chats. Failed: {failed} chats."
                )
            await asyncio.sleep(0.7)
        await client.send_message(
            message.chat.id, f"Left {left} chats. Failed {failed} chats."
        )
 
 
