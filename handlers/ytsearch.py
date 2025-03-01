# Size linkler halinde arar. 
import logging

from pyrogram.types import Message
from search_engine_parser import GoogleSearch
from youtube_search import YoutubeSearch

from pyrogram import Client as app, filters

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)

@app.on_message(pyrogram.filters.command(["ytaxtar"]))
async def ytaxtar(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("Mene senedçi adı ya da Mahnı adı verin!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("Axtarıram...⚡")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"Musiqi Adı - {results[i]['title']}\n"
            text += f"Musiqi Müddəti - {results[i]['duration']}\n"
            text += f"Baxış Sayı - {results[i]['views']}\n"
            text += f"Kanal - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
