from flask import Flask , request
from pymessenger.bot import Bot
import config as cg
from yts import search
from convert import convert_vid
app = Flask(__name__)

ACCESS_TOKEN = cg.token

VERIFY_TOKEN = "MrPain"

bot = Bot(ACCESS_TOKEN)

@app.route('/', methods=['GET', 'POST'])
#my function 
def webhook():
    IF_BOST_BACK = True
    data =""
    if request.method == "GET":
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return 'verification Complete| this bot by ahmed Mr Pain'
    elif request.method == "POST":
        data = request.get_json()
        sender_id = str(data['entry'][0]['messaging'][0]['sender']['id'])
        time = str(data['entry'][0]['time'])
        byload =""
        if "payload" in str(data) : 
            byload = str(data['entry'][0]['messaging'][0]['postback']['payload'])
            IF_BOST_BACK = False
        else: 
            byload = str(data['entry'][0]['messaging'][0]['message']['text'])
            IF_BOST_BACK = True
            # bot.send_text_message(sender_id,str(data))
        if IF_BOST_BACK :
            search(byload,sender_id)
        else: 
            convert_vid(byload,sender_id)
    return "200 ok"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)