from yts import upload_vid
from pymessenger.bot import Bot
import config as cg


bot = Bot(cg.token)

def convert_vid(data="",sender=""): 
    if not data in cg.load_db():
        cg.save_db(data)
        if "$DO" in data: 
            result = data.replace("$DO","")
            bot.send_text_message(sender,cg.start_down)
            upload_vid(result,sender,"video")
        elif "$AU" in data: 
            result = data.replace("$AU","")
            bot.send_text_message(sender,cg.start_down)
            upload_vid(result,sender,"audio")
        else: 
            bot.send_text_message(sender,cg.error)