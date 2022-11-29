import re
from chat_downloader import ChatDownloader

def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)

def exe_oss_chat_downloader(videoId):
    downloader = ChatDownloader()
    youtube_url = "https://www.youtube.com/watch?v="
    target_url = youtube_url + videoId
    try:
        chat = downloader.get_chat(target_url)
        return chat
    except:
        print("this video id is invalid")

def convert_chat_to_json(chat, filename):
    return