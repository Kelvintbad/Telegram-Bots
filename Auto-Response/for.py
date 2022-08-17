import json 
import requests
from time import sleep

TOKEN = "5369935751:AAHj5uad9kRHlEVshZYs7YMJON--FmaOUhc" # Telegram bot API access token
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates?offset=" + str(prev_uid)
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text_and_time(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    last_update_id = updates["result"][last_update]["update_id"]
    if "message" in updates["result"][last_update]:
        if "text" in updates["result"][last_update]["message"]:
            text = updates["result"][last_update]["message"]["text"].lower()
        else:
            text = ""
        time = updates["result"][last_update]["message"]["date"]
        chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    else:
        text = ""
        time = 0
        chat_id = 0
    #print(updates)
    return (text, chat_id, time, last_update_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

	
def dontdoshit():
	return
	

response_map = {
	"Hi": "Hi",
	"Hello": "Hello, how are you doing",
	"info": "This bot was created by @kelvinnyo",
	"about":"customise the response map to add choice of reply"
}

prev_uid = 0
prev_uid = get_last_chat_id_and_text_and_time(get_updates())[3]
while True:
	text, chat, time, uid = get_last_chat_id_and_text_and_time(get_updates())

	if uid == prev_uid:
		dontdoshit()
	else:
		for q, a in response_map.items():
			if q in text:
				send_message(a, chat)
		prev_uid = uid
	sleep(1)
