import requests
from bs4 import *
import config as cg
from pymessenger.bot import Bot
from fb_tools import *
token = cg.token
url = cg.url
btns = []
bot = Bot(token)
def search(text="",sender=""):
    bot.send_text_message(sender,cg.search)
    temp = []
    req = requests.get(url,params=cg.param(text))
    results = req.json()['items']
    if req.status_code == 200:
        try : 
            for i in range(len(results)):
                btns = {}
                video_id = results[i]['id']['videoId']
                btns = [add_btn("ｄｏｗｎｌｏａｄ 📥","postback","",f"$DO{video_id}")]
                btns.append(add_btn("ａｕｄｉｏ 🎧","postback","",f"$AU{video_id}"))
                video_title = results[i]['snippet']['title']
                video_description = results[i]['snippet']['description'] 
                thumbnail_url =results[i]['snippet']['thumbnails']['high']['url']
                temp.append(new_attach_img(thumbnail_url,video_title+video_title+video_title,video_description,btns))
            rep = send_msg(token,temp,sender)
        except : 
            bot.send_text_message(sender,results)
    else: 
        bot.send_text_message(sender,cg.error)
def upload_vid(vid_url="",sender="",type_vid="video"):
    links = []
    vid_url = vid_url
    num = 0
    #try:
    html_txt = requests.get("https://videograbber.cc/download?url=https://youtu.be/" + vid_url )
    soup = BeautifulSoup(html_txt.content,"html.parser")
    data = soup.find('table')
    for link in data.find_all("a"):
            links.append(link.get("href"))
    for a in range(len(links)):
        req = requests.get(links[a])
        size = int(req.headers.get('Content-Length', 0))
        tall = 26000000
        if tall >= size :
            video_url = links[a]
            break
        else:
            num += 1
    if num == len(links):
        bot.send_text_message(sender,cg.error_vid)
    else: 
        reqer = send_attach(token,sender,type_vid,video_url)
        if "error" in str(reqer):
            bot.send_text_message(sender,cg.error)
        elif "recipient" in str(reqer):
            bot.send_text_message(sender,cg.end_down)
        else: 
            bot.send_text_message(sender,cg.error)
    #except :
   #     bot.send_text_message(sender,cg.error)