import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
import random
@app.on_message(
    command(["","","السورس","", ""])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4c0e63af8a410d9a53fa0.jpg",
        caption=f"""
 [𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙎𝙋𝘼𝙍𝙆](https://t.me/ZZZ7iZ)
 —————————————
 [𝙃 𝘼 𝙈 𝘿 | 🇮🇶](https://t.me/IIIlIIv)
 
 [𝙋𝙏𝙊 𝙎𝙊𝙐𝙍𝘾𝙀](https://t.me/du2sbot)
  
 [⍟𓏺𝙒𝞝𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼](https://t.me/HL_BG)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙃 𝘼 𝙈 𝘿 | 🇮🇶", url=f"https://t.me/IIIlIIv"), 
                ],[
                    InlineKeyboardButton(
                        "𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙎𝙋𝘼𝙍𝙆", url=f"t.me/ZZZ7iZ"),
                ],

            ]

        ),

    )

@app.on_message(command([f"غنيلي", "", "غ", "{BOT_USERNAME} غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/iV_P_Nl/{rl}"
    await client.send_voice(message.chat.id,url,caption="` ⌔︙ تـم اختيـار الاغـنـية لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["",""]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="`💕 ¦ تـم اختيـار الصوره لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

                        


