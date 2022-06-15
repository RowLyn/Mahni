from pyrogram import Client
import asyncio
from config import SUDO_USERS
from config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Salam, Mahnı asistanı hizmeti üçündür.\n\n ❗️ kurallar:\n - Söhbete icaze yoxdur.\n - Melumat ve Emrlerim Üçün grub söhbetinde **/melumat** yazarsız. (Asistan söhbetine melumat yazmayın.) Mahnı emrlerini öyrene bilersiniz. \n - İstenilmeyen posta icaze verilmir \n\n 🚨 **Asistan Grubunuza Qatılmırsa >> DEVETLE QATILMA ÖZELLİYİ VE SES İDARE ETME YETKİSİ VERİB ADMİN EDİN. <<**\n\n ⚠️ DİQQET: Burda bir mesaj gönderirsinizse bu. Adminin mesajınızı göreceyi anlamına gelir.\n - Şexsi melumatlarınızı burada paylaşmayın. (Mahnı Botunu  Gizli Grublara almayın.) 🏆 Melumat  üçün [Qurucu 🐊](https://t.me/Rowlyn) 🇦🇿\n",
            )
            return
 
    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("PM İcaze Açığdır")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("PM İcazr Açığ Deyil")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("** Asistan Yazışması artığ uğurludur.**")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Texmini olarağ PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Bu cür PM")
        return
    message.continue_propagation()
