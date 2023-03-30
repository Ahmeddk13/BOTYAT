import requests
import json 

#attach with image

def new_attach_img(image="",title="",subtitle="",btns=[]):

	       lists = {}

	       if  str(btns) == '[]':

	           if subtitle == "":

	               lists = {'title':title,'image_url':image,'default_action': {'type': 'web_url','url': image}}

	           else:

	               lists = {'title':title,'image_url':image,'subtitle':subtitle,'default_action': {'type': 'web_url','url': image}}	                   

	       else:

	           if subtitle == "":

	               lists = {'title':title,'image_url':image,'default_action': {'type': 'web_url','url': image },'buttons':btns}

	           else:

	               lists = {'title':title,'image_url':image,'subtitle':subtitle,'default_action': {'type': 'web_url','url': image},'buttons':btns}

	       return lists    

#attach without image

def new_attach(title="",subtitle="",btns=[]):

	       lists = {}

	       if  str(btns) == '[]':

	           if subtitle == "":

	               lists = {'title':title,'default_action': {'type': 'web_url','url': "https://www.facebook.com/Mr12PAIN"}}

	           else:

	               lists = {'title':title,'subtitle':subtitle,'default_action': {'type': 'web_url','url': "https://www.facebook.com/Mr12PAIN",'webview_height_ratio':'tall'}}	                   

	       else:

	           if subtitle == "":

	               lists = {'title':title,'default_action': {'type': 'web_url','url': "https://www.facebook.com/Mr12PAIN",'webview_height_ratio':'tall'},'buttons':btns}
	               
	           else:

	               lists = {'title':title,'subtitle':subtitle,'default_action': {'type': 'web_url','url': "https://www.facebook.com/Mr12PAIN",'webview_height_ratio':'tall'},'buttons':btns}

	       return lists

def add_btn(title="",type="postback",url="",id_ac="test"):

    btns = {}

    if type == "web_url":

        btns = {'title':title,"type":type,"url":url}

    else:

        btns = {'title':title,"type":type,"payload":id_ac}
    return btns

def send_msg(token="",data=[],senderid=""):
    sync_data = {'recipient':{'id': senderid},'message': {'attachment': {'type': 'template','payload': {'template_type': 'generic','elements': data}}}}

    url='https://graph.facebook.com/v16.0/me/messages?access_token=' + token
    response = requests.post(url, json=sync_data).json()
    return response

def send_attach(token="",senderid="",type_vid="video",url=""):
    headers = {'Content-Type': 'application/json'}
    data = {'recipient':{'id': senderid},'message': {'attachment': {'type': type_vid,'payload':{'url':url,"is_reusable": True}}}}
    response = requests.post(
    'https://graph.facebook.com/v16.0/me/messages?access_token=' + token,
    headers=headers,
    data=json.dumps(data))
    return response.content
#print(add_btn("ahmed"))