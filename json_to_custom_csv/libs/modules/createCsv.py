from datetime import datetime
import csv
import os

def convert_str_to_iso_date(strDate):
    isoDate = datetime.fromisoformat(strDate)
    return isoDate

def make_datepath(date):
    _date = date
    if type(date) == str:
        _date = convert_str_to_iso_date(date)
    datePath = _date.strftime('%Y\\%m')
    return datePath

def make_complete_path(channelName, datePath, videoTitle):
    path = "\\export\\csv\\"
    path = path + channelName + "\\"
    path = path + datePath + "\\"
    path = path + videoTitle + ".csv"
    return path

def extract_chat_properties(chat):
    chatList = []
    for message in chat:
        comment = {"message_id": message["message_id"], "time_text": message["time_text"], "message": message["message"], "action_type": message["action_type"]}

        if "emotes" in message:
            emo = message["emotes"][0]["id"]
            name = message["emotes"][0]["name"]
            replacedMassage = message["message"].replace(name, emo)
            comment["message"] = replacedMassage

        chatList.append(comment)

    return chatList

def create_csv(chatList, path):
    os.makedirs(path, exist_ok=True)
    try:
        with open(path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames = chatList.keys())
            writer.writeheader()
            writer.writerow(chatList)
    except:
        os.rmdir(path)
    return