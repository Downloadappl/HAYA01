import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "تعاال شبيك يردونك @IIIlIIv",


             "هذا مطور مالتي @IIIlIIv",
            

             "**تع يردوك يالمطورر @IIIlIIv**",
            
           
 
            
            

        ]


        


@app.on_message(command(["المطور","مطورغثعتث","المطزينهاب"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
