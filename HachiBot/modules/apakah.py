import random
from HachiBot.events import register
from HachiBot import telethn

APAKAH_STRING = ["iya",
    "tidak",
    "mungkin",
    "bisa jadi",
    "anda benar sekali",
    "anda salah besar",
    "au deh",
    "sapa tau bener",
    "sapa tau salah",
    "bener bet anj",
    "awoakekwawsek",
    "y",
    "g",
    "🤔",
    "👍",
    "👎",
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
