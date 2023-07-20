t asyncio
import os
from config import OWNER_ID
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from asyncio import gather
from pyrogram.errors import FloodWait
from pyrogram.enums import ParseMode, ChatMemberStatus



@app.on_message(command(["المالك"]) & filters.group)
async def gak_owne(client: Client, message: Message):
      if len(message.command) >= 2:
         return 
      else:
            chat_id = message.chat.id
          
            async for member in client.get_chat_members(chat_id):
               if member.status == ChatMemberStatus.OWNER:
                 id = member.user.id
                 key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
                 m = await client.get_chat(id)
                 if m.photo:
                       photo = await app.download_media(m.photo.big_file_id)
                       return await message.reply_photo(photo, caption=f"**✧ ¦معلومات مالك القروب \n\n ✧ ¦ اسمه ← {m.first_name} \n ✧ ¦ معرفه ← @{m.username} \n ✧ ¦ البايو ← {m.bio}**",reply_markup=key)
                 else:
                    return await message.reply("• " + member.user.mention)
                    
                    
   

   
@app.on_message(command(["اسمي", "شنو اسمي"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f""" اسمك : {message.from_user.mention()}""") 

        

array = []
@app.on_message(command(["صيحهم", "تاك","تاك للكل"]) & ~filters.private)
async def nummmm(client: app, message):
  if message.chat.id in array:
     return await message.reply_text(f"**تم بدأ التاك الجماعي \n\n بواسطة ← ✧ ¦{message.from_user.mention}**")

  dev = (OWNER_ID)
  haya = (5012406813,5012406813)
  get = await client.get_chat_member(message.chat.id, message.from_user.id)
  if message.from_user.id in haya:
         rotba= "مبرمج السورس" 
  elif message.from_user.id in dev:
         rotba = "مطور اساسي" 
  elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
  elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"     
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in  [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply(f"**انت لست مشرفا يا {message.from_user.mention}**")
    return
  await message.reply_text(f"**تم بدأ التاق الجماعي \n\n بواسطة ← {rotba}✧ ¦{message.from_user.mention} \n\n للايقاف اكتب وقف منشن او خلاص**")
  i = 0
  txt = ""
  zz = message.text
  if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
  try:
   zz = zz.replace("@all","").replace("تاك","").replace("صيح بيهم","")
  except:
    pass
  array.append(message.chat.id)
  async for x in client.get_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f" {x.user.mention} ،"
       if i == 5:
        try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
        except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
        except Exception:
              array.remove(message.chat.id)
  array.remove(message.chat.id)


@app.on_message(command(["وكف التاك", "/cancel","كافي"]))
async def stop(client, message):
  dev = (OWNER_ID)
  haya = (6275847466,6195765774)
  get = await client.get_chat_member(message.chat.id, message.from_user.id)
  if get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
  elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
  elif message.from_user.id in haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوࢪس" 
  elif message.from_user.id in dev:
         rotba = "مطور اساسي"           
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in  [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply(f"**انت لست مشرفا يا {message.from_user.mention}**")
    return
  if message.chat.id not in array:
     await message.reply(f"**التاك متوقف فالاصل \n\n يا {message.from_user.mention}**")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply(f"**تم ايقاف التاك الجماعي \n\n بواسطة ← {rotba}✧ ¦{message.from_user.mention}**")
    return


