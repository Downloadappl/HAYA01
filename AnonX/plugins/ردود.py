import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config

dev = (config.OWNER_ID)


txt = [

            "دوٌمُ ٱڷضٍـحڪهْهْ ♥️😻",


             "ضٍـحڪڹٱ مُعُٱٱڪ🙄🙄",
            

            "ضٍـحڪڹٱ مُعُٱٱڪ🙄🙄",
            
            
            "۾ـآ ڣي ڜي يڞحـڪ يبـآڕد 😒😒",
            
            
            "ࢪبـي يـدوٍ۾ آلڞـحـڪـهہ يآﭰلبـي🥺🔥",
            
            
             "ضحكه بدون نيهه🙂😒",
            
            
 
            
            

        ]
txt1 = [

            "**دوومم ياامطوورييي♥️😻**",


             "**مطوري الغالي محلاها ضحكتك**",
            

            "**ضحكني معاك يا حبي المطور الاساسي🥺🔥**",
            
            
          
            
 
            
            

        ]

        
        


@app.on_message(command(["ههه","😂😂","😂😂😂😂😂","😂🤣","ههههههههههههههههههه","😂😂😂😂😂😂"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
      b = random.choice(txt1)


      await message.reply(


        f"{b}")
