import re
from chat_downloader import ChatDownloader
from datetime import datetime

def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)

def convert_str_to_iso_date(strDate):
    isoDate = datetime.fromisoformat(strDate)
    return isoDate

def make_path_from_date(date, videoTitle):
    _date = date
    if type(date) == str:
        _date = convert_str_to_iso_date(date)
    datePath = _date.strftime('%Y\\%m')
    return "\\export\\csv\\{datePath}\\{videoTitle}".format(datePath=datePath, videoTitle=videoTitle)

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