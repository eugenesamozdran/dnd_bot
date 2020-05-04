import json 
import requests
import time
import urllib
import db_fetcher as fetch

TOKEN = "my_bot_token"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url) # response object which contains a server’s response to an HTTP request
    content = response.content.decode("utf8") # content of the response in bytes is decoded using utf-8 encoding
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content) # parsing json content into Python dict
    return js

def get_updates(offset=None): # get messages sent to bot. offset helps to filter older and unnecessary messages
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url) 
    return js

def get_last_chat_id_and_text(updates): # function for receiving message text and chat id from deserialized json content
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def get_last_update_id(updates): # keeping track of update ids
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def send_message(text, chat_id, reply_markup=None): # sending messages to user
    text = urllib.parse.quote_plus(text) # helps to pass special characters in messages
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)

def handle_update(update):
    text = update["message"]["text"]
    chat = update["message"]["chat"]["id"]
    if text == "/start":
        send_message("Welcome to DND conditions list. Type the name of the condition starting with '/' to access the necessary info.", chat)
    elif text.startswith("/"):
        condition = ''.join(e for e in text if e.isalnum())
        if condition in fetch.get_pkey():
            message = fetch.get_value(condition)
            send_message(message, chat)
        else:
            send_message("Please use valid condition description starting with '/'", chat)

def handle_updates(updates):
    for update in updates["result"]:
        handle_update(update)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
