import asyncio
##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]

import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import Client
from config import OWNER_ID, MUSIC_BOT_NAME
from pyrogram import filters
##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]
txt = [

            f"عندي اسم اسمي {MUSIC_BOT_NAME}",


             f"انت البوت يلي راسك مربع اسمي {MUSIC_BOT_NAME}",
            

            f"هہذآ آڛـﻤــي {MUSIC_BOT_NAME}",
            
            
            f"اسمي {MUSIC_BOT_NAME}",
            
            
           
            
            
             "ﺷِﻧڻ تـبـي🙂😒",
            
            
 
            
            

        ]
txt1 = [

            f"**؏ـيوٍڼ 😻🫶 يا مطوريي البوت**",


            f"**ﻧ؏ـم يامطوري الغالي**",
            

            f"**ااحلى من يعيط بوت 😻🫶**",
            
            f"**نعٓم يـﺣـبـعـﻣـر{MUSIC_BOT_NAME}**",
           
            
            
 
            
            

        ]



##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]    


@app.on_message(command(["بوت"]))


async def cutt(client: Client, message: Message):
     dev = (OWNER_ID)
     if message.from_user.id in dev:


         b = random.choice(txt1)


         await message.reply(


         f"{b}")
     else:
         a = random.choice(txt)


         await message.reply(
##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]

         f"{a}")
       
##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]     
