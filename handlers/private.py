from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/nN5D6nR5ZKEgLmLa6",
  caption=(f"""**Salam {message.from_user.mention} 🎧\nMen {bot}!\nSesli söhbetlerde mahnı oxuda bilen botam. Ban yetkisiz, Sesi idare etme yetkisi verib, Asistanı gruba elave edin.\n\nDesign By  [RowlynBots 🎰](https://t.me/NemesisChat).**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😴 ❰ Grubuna elave et ❱ ✝️", url=f"https://t.me/nemesismusicrobot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎥 Asistan", url="https://t.me/NemesisMusicAsistan"
                    ),
                    InlineKeyboardButton(
                        "💬 Söhbet", url="https://t.me/NemesisChat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💎 Emrler" , callback_data= "cbmelumat"
                    ),
                    InlineKeyboardButton(
                        "Resmi Kanal 🇦🇿", url=f"https://t.me/RowlynBots"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["melumat", f"melumat@{BOT_USERNAME}"]))
async def melumat(_, message: Message):
      await message.reply_text(" ❗ Önemli:\n Botun İşləməsi Üçün Bu üç yetkini bota verin:\n- Mesaj silme yetkisi,\n- Bağlantı ile devet etme yetkisi,\n- Sesli söhbeti idare etme yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "❤️ Hamı üçün emrler", callback_data="emr")
                 ],[                     
                     InlineKeyboardButton(
                         "🖤 Admin üçün emrler", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Ana menyu🌃", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "⚙ Quraşdırıcı", url="https://t.me/Rowlyn")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbmelumat"))
async def cbmelumat(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Önemli:\nBotun İşləməsi Üçün Bu üç yetki Lazımdır:\n- Mesaj silme yetkisi,\n- Bağlantı ile devet etme yetkisi,\n- Sesli söhbeti idare etme yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨Hamı üçün Emrler", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "🔥Admin Emrleri",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🌃Ana Menyu", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "⚙ Quraşdırıcı", url="https://t.me/Rowlyn")
        
     ]]
     ))
     


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun herkes üçün emr menyusu 😝\n\n ▶️ /çal - mahnı oxudmağ üçün youtube link'ine veya mahnı dosyasına cavab vererek işled\n ▶️ /çal <mahnı adı> - istediyiniz mahnını oxudun\n 🤙🏼 \n 🎵 /vmahnı <mahnı adı> - istediyiniz mahnıları tam süretli şekilde tapın\n 🎵 /vaxtar istediyiniz videoları süretli şekilde tapın\n 🔍 /axtar <query> - youtube'da melumatları gösteren videoları axtarmağ\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Quraşdırıcı", url="https://t.me/Rowlyn")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbmelumat")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminler üçün emr menyusu 💸\n\n ▶️ /davam - mahnını oxudmağa davam et\n ⏸️ /dayandır - oxuyan musiqini müveqqeti dayandırmağ üçün\n 🔄 /keç- Oxunan Musiqini Keçer.\n ⏹ /bitirmek - mahnı oxudmağı dayandır\n 🔼 /ver botun sadece admin üçün işledile bilen  emrlerini işledmesi üçün istifadeçiye yetki ver\n 🔽 /al botun admin emrlerini istifade ede bilen istifadeçinin yetkisini al\n\n ⚪ /asal - Mahnı asistanı grubunuza qatılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Quraşdırıcı", url="https://t.me/Rowlyn")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbmelumat")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {query.from_user.mention} 🎵\nMen {bot}!\nSesli söhbetlerde mahnı oxuda bilen botam. Ban yetkisiz, Sesi idare etme yetkisi verib, Asistanı gruba elave et.\n\nDesign By [RowlynBots 😝](https://t.me/NemesisChat).**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✝️ ❰ Grubuna Elave Et ❱ ✝️", url=f"https://t.me/nemesismusicrobot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎥 Asistan", url="https://t.me/nemesismusicasistan"
                    ),
                    InlineKeyboardButton(
                        "💬 Söhbet", url="https://t.me/Nemesischat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡ Emrler" , callback_data= "cbmelumat"
                    ),
                    InlineKeyboardButton(
                        "Resmi Kanal 🇦🇿", url=f"https://t.me/RowlynBots"
                    )
                ]
                
           ]
        ),
    )
