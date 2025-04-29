# Don't Remove Credit Tg - @learnmaterobot

import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    await m.reply_text(f"<b>ð‡ðžð¥ð¥ð¨ ðƒðžðšð«  ðŸ‘‹! {m.from_user.mention} \n\n âž  ðˆ ðšð¦ ðš ð“ðžð±ð­ ðƒð¨ð°ð§ð¥ð¨ðšððžð« ðð¨ð­ ðŒðšððž By â™¥ï¸ **@irymes** \n\n âž  ð‚ðšð§ ð„ð±ð­ð«ðšðœð­ ð•ð¢ððžð¨ð¬ & ðððŸ ð…ð«ð¨ð¦ ð˜ð¨ð®ð« ð“ðžð±ð­ ð…ð¢ð¥ðž ðšð§ð ð”ð©ð¥ð¨ðšð ð­ð¨ ð“ðžð¥ðžð ð«ðšð¦ \n\n âž  ð”ð¬ðž /as ð‚ð¨ð¦ð¦ðšð§ð ð“ð¨ ðƒð¨ð°ð§ð¥ð¨ðšð ð…ð«ð¨ð¦ ð“ð—ð“ ð…ð¢ð¥e..\n\n âž  ð”ð¬ðž /stop ð“ð¨ ð¬ð­ð¨ð© ð€ð§ð² ðŽð§ð ð¨ð¢ð§ð  ð“ðšð¬ð¤ \n\n âž  ðŒðšððž ðð²:- @irymes  </b>")

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**ðŸ‡¸ðŸ‡¹ðŸ‡´ðŸ‡µðŸ‡µðŸ‡ªðŸ‡©**ðŸš¦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["as"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('ðŸ—£ð—¦ð—˜ð—¡ð—— ð— ð—˜ ð—§ð—«ð—§ ð—™ð—œð—Ÿð—˜ âš¡ï¸')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**ð•‹á´á´›á´€ÊŸ ÊŸÉªÉ´á´‹ð•¤ Ò“á´á´œÉ´á´… á´€Ê€á´‡ðŸ”—ðŸ”—** **{len(links)}**\n\n**ð•Šá´‡É´á´… ð”½Ê€á´á´ á´¡Êœá´‡Ê€á´‡ Êá´á´œ á´¡á´€É´á´› á´›á´ á´…á´á´¡É´ÊŸá´á´€á´… ÉªÉ´Éªá´›Éªá´€ÊŸ Éªð•¤** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**ðð¨ð° ðð¥ðžðšð¬ðž ð’ðžð§ð ðŒðž ð˜ð¨ð®ð« ððšð­ðœð¡ ððšð¦ðž\n\nð—˜ð—´ Â» `LAKSHYA BANGLA HS (3RD-4TH SEM ) 2026`**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("*ðŸ“¸ ð—˜ð—»ð˜ð—²ð—¿ ð—¥ð—²ð˜€ð—¼ð—¹ð˜‚ð˜ð—¶ð—¼ð—» ðŸ“¸**\nâž¤ `144`\nâž¤ `240`\nâž¤ `360`\nâž¤ `480`\nâž¤ `720`\nâž¤ `1080`")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("ðŸ“¥ ð„ð—ð“ð‘ð€ð‚ð“ð„ðƒ ðð˜ âž¤\n\nð—˜ð—´ Â» `@irymes`")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"ï¸ âªâ¬â®â®â®"
    if raw_text3 == 'Robin':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("Now send the Thumb url/nEg Â» https://i.ibb.co/T6cnYmm/image.jpg \n Or if don't want thumbnail send = no")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDY1MDI4MDguMTYsImRhdGEiOnsiX2lkIjoiNjIzZjJmNTM3ZjUxOTcwMzM0YjhjZTk3IiwidXNlcm5hbWUiOiI5NDI5NzQ5NDE0IiwiZmlyc3ROYW1lIjoiaGFyZXNoIiwibGFzdE5hbWUiOiJLdW1hciIsIm9yZ2FuaXphdGlvbiI6eyJfaWQiOiI1ZWIzOTNlZTk1ZmFiNzQ2OGE3OWQxODkiLCJ3ZWJzaXRlIjoicGh5c2ljc3dhbGxhaC5jb20iLCJuYW1lIjoiUGh5c2ljc3dhbGxhaCJ9LCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwidHlwZSI6IlVTRVIifSwiaWF0IjoxNzQ1ODk4MDA4fQ.9XcbL_57MuGyecUY08qbHnzwdtlCp96pCpGQfsQSahM'}).json()['url']

            elif "d1d34p8vz63oiq" in url or "sec1.pw.live" in url:
                pw_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDY1MDI4MDguMTYsImRhdGEiOnsiX2lkIjoiNjIzZjJmNTM3ZjUxOTcwMzM0YjhjZTk3IiwidXNlcm5hbWUiOiI5NDI5NzQ5NDE0IiwiZmlyc3ROYW1lIjoiaGFyZXNoIiwibGFzdE5hbWUiOiJLdW1hciIsIm9yZ2FuaXphdGlvbiI6eyJfaWQiOiI1ZWIzOTNlZTk1ZmFiNzQ2OGE3OWQxODkiLCJ3ZWJzaXRlIjoicGh5c2ljc3dhbGxhaC5jb20iLCJuYW1lIjoiUGh5c2ljc3dhbGxhaCJ9LCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwidHlwZSI6IlVTRVIifSwiaWF0IjoxNzQ1ODk4MDA4fQ.9XcbL_57MuGyecUY08qbHnzwdtlCp96pCpGQfsQSahM"
                url = f"https://anonymouspwplayer-b99f57957198.herokuapp.com/pw?url={url}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDY1MDI4MDguMTYsImRhdGEiOnsiX2lkIjoiNjIzZjJmNTM3ZjUxOTcwMzM0YjhjZTk3IiwidXNlcm5hbWUiOiI5NDI5NzQ5NDE0IiwiZmlyc3ROYW1lIjoiaGFyZXNoIiwibGFzdE5hbWUiOiJLdW1hciIsIm9yZ2FuaXphdGlvbiI6eyJfaWQiOiI1ZWIzOTNlZTk1ZmFiNzQ2OGE3OWQxODkiLCJ3ZWJzaXRlIjoicGh5c2ljc3dhbGxhaC5jb20iLCJuYW1lIjoiUGh5c2ljc3dhbGxhaCJ9LCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwidHlwZSI6IlVTRVIifSwiaWF0IjoxNzQ1ODk4MDA4fQ.9XcbL_57MuGyecUY08qbHnzwdtlCp96pCpGQfsQSahM"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**[ðŸ“½ï¸] Vid_ID:** {str(count).zfill(3)}.** {ð—»ð—®ð—ºð—²ðŸ­}.mkv \n\n**ðŸ“šðð€ð“ð‚ð‡ ð—¡ð—”ð— ð—˜ âž¤**  **{raw_text0}**\n\nðŸ“¥ ð—˜ð—«ð—§ð—¥ð—”ð—–ð—§ð—˜ð—— ð—•ð—¬ ** âž¤**ã€Ž{raw_text3}ã€**\n\nâ”â”â”â”â”â”â”â”âœ¦@PRAYAS_WBJEEâ¤ï¸âœ¦â”â”â”â”â”â”â”â”'
                cc1 = f'**[ðŸ“] Pdf_ID:** {str(count).zfill(3)}. {ð—»ð—®ð—ºð—²ðŸ­} .mkv \n\n**ðŸ“šðð€ð“ð‚ð‡ ð—¡ð—”ð— ð—˜ âž¤**  **{raw_text0}**\n\nðŸ“¥ ð—˜ð—«ð—§ð—¥ð—”ð—–ð—§ð—˜ð—— ð—•ð—¬ ** âž¤**ã€Ž{raw_text3}ã€**\n\nâ”â”â”â”â”â”â”â”âœ¦@PRAYAS_WBJEEâ¤ï¸âœ¦â”â”â”â”â”â”â”â”'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**â¥¥ ðŸ‡©ðŸ‡´ðŸ‡¼ðŸ‡³ðŸ‡±ðŸ‡´ðŸ‡¦ðŸ‡©ðŸ‡®ðŸ‡³ðŸ‡¬â¬‡ï¸â¬‡ï¸... Â»**\n\n**ðŸ“Name Â»** `{name}\nâ„Quality Â» {raw_text2}`\n\n**ðŸ”—URL Â»** `{url}`"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading Interupted **\n{str(e)}\n**Name** Â» {name}\n**Link** Â» `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**ðŸ”°ðƒðŽðð„ ALSO JOIN @PRAYAS_WBJEE**")


bot.run()

    
