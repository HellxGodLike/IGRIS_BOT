import requests
url = "https://iamai.p.rapidapi.com/ask"
from SaitamaRobot import telethn, OWNER_ID
from SaitamaRobot.events import register
from telethon import events
from telethon import types
from telethon.tl import functions
import asyncio, os

@register(pattern="Igris (.*)")
async def hmm(event):
  test = event.pattern_match.group(1)
   test = test.replace('Jessica', 'Igris')
    test = test.replace('Jessica', 'Igris')
  r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
  k = f"({r})"
  new_string = k.replace("(", "{")
  lol = new_string.replace(")","}")
  payload = lol
  headers = {
    'content-type': "application/json",
    'x-forwarded-for': "<user's ip>",
    'x-rapidapi-key': "33b8b1a671msh1c579ad878d8881p173811jsn6e5d3337e4fc",
    'x-rapidapi-host': "iamai.p.rapidapi.com"
    }

  response = requests.request("POST", url, data=payload, headers=headers)
  lodu = response.json()
  result = (lodu['message']['text'])
  
  if "no no" in result:
   pro = "I am fairly young and I was made by @HeLLxGodLike"
   try:
      async with telethn.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(pro)
   except CFError as e:
           print(e)
  elif "ann" in result:
   pro = "My name is Igris"
   try:
      async with telethn.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(pro)
   except CFError as e:
           print(e)
  else:
    try:
      async with telethn.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(result)
    except CFError as e:
           print(e)
        
        
    test = test.replace('Jessica', 'Igris')
    test = test.replace('Jessica', 'Igris')
  r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
  k = f"({r})"
  new_string = k.replace("(", "{")
  lol = new_string.replace(")","}")
  payload = lol
  headers = {
      'content-type': "application/json",
      'x-forwarded-for': "<user's ip>",
      'x-rapidapi-key': "33b8b1a671msh1c579ad878d8881p173811jsn6e5d3337e4fc",
      'x-rapidapi-host': "iamai.p.rapidapi.com"
      }
 
  response = requests.request("POST", url, data=payload, headers=headers)
  lodu = response.json()
  result = (lodu['message']['text'])
  pro = result
  pro = pro.replace('Thergiakis Eftichios','Necromander Hellx')
  pro = pro.replace('Jessica','Igris')
  if "Out of all ninja turtle" in result:
   pro = "Sorry! looks I missed that. I'm at your service ask anthing sir?"
  if "ann" in result:
   pro = "My name is Jarvis"
  if not "en" in lan and not lan == "":
    pro = translator.translate(pro, lang_tgt=lan[0])
  try:
    await daisyx.send_chat_action(message.chat.id, "typing")
    await message.reply_text(pro)
  except CFError as e:
         print(e)

