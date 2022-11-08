from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/nN5D6nR5ZKEgLmLa6",
  caption=(f"""**Salam {message.from_user.mention} 🇦🇿\nMən {bot}!\nSəsli Söhbətlərdə Mahnı Oxuda Bilən Botam.Ban yetkisiz,Sesi idarə etmə yetkisi verib, Asistanı gruba elave edin.\n\nHazırlandı [ʙʀᴇɴᴅ ᴍᴜsɪᴠ🎰](https://t.me/BrendSupport).**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Grubuna Əlavə Et➕", url=f"https://t.me/BrendMusicRoBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎥 Asistan", url="https://t.me/BrendMusicRoBot"
                    ),
                    InlineKeyboardButton(
                        "💬 Brend Usər Bot", url="https://t.me/BrendUserBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡ Brend Support", url="https://t.me/BrendUserBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💎 Əmrlər" , callback_data= "cbmelumat"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal 🇦🇿", url=f"https://t.me/BrendUserBot"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["melumat", f"melumat@{BOT_USERNAME}"]))
async def melumat(_, message: Message):
      await message.reply_text("Botun İşləməsi Üçün Bu Üç Yetkini Bota Verin:\n- Mesaj silme yetkisi,\n- Bağlantı ile devet etme yetkisi,\n- Sesli söhbeti idare etme yetkisi.", 
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
    await query.edit_message_text("Botun İşləməsi Üçün Bu üç yetki Lazımdır:\n- Mesaj silme yetkisi,\n- Bağlantı ile devet etme yetkisi,\n- Sesli söhbeti idare etme yetkisi.", 
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
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun herkes üçün emr menyusu 🔸\n\n ▶️ /play - mahnı oxudmağ üçün youtube link'ine veya mahnı dosyasına cavab vererek işled\n ▶️\n 🎵 /song <mahnı adı> - istediyiniz mahnıları tam süretli şekilde tapın\n 🎵 /videoaxtar istediyiniz videoları süretli şekilde tapın\n 🔍 /axtar <query> - youtube'da melumatları gösteren videoları axtarmağ\n\n</b>""",
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
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminler üçün emr menyusu 💸\n\n ▶️ /davam - mahnını oxudmağa davam et\n ⏸️ /dayandir - oxuyan musiqini müveqqeti dayandırmağ üçün\n 🔄 /kec- Oxunan Musiqini Keçer.\n ⏹ /bitirmek - mahnı oxudmağı dayandır\n 🔼 /ver botun sadece admin üçün işledile bilen  emrlerini işledmesi üçün istifadeçiye yetki ver\n 🔽 /al botun admin emrlerini istifade ede bilen istifadeçinin yetkisini al\n\n ⚪ /asal - Mahnı asistanı grubunuza qatılır.\n\n</b>""",
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
    await query.edit_message_text(f"""**Salam {query.from_user.mention} 🎵\nMən {bot}!\nSəsli Söhbətlərdə Mahnı Oxuda Bilən Botam. Ban yetkisiz, Sesi idare etme yetkisi verib, Asistanı gruba elave et.\n\nHazırlandı [ʙʀᴇɴᴅ ᴍᴜsɪᴄ🎙️](https://t.me/BrendSupport).**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Grubuna Əlavə Et➕", url=f"https://t.me/BrendMusicRoBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎥 Asistan", url="https://t.me/BrendMusicRoBotAsistan"
                    ),
                    InlineKeyboardButton(
                        "💬 Söhbət Grubu", url="https://t.me/BrendSohbet"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡ Emrler" , callback_data= "cbmelumat"
                    ),
                    InlineKeyboardButton(
                        "Resmi Kanal 🇦🇿", url=f"https://t.me/BrendUserBot"
                    )
                ]
                
           ]
        ),
    )
