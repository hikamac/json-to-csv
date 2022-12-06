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

def make_complete_path(channelName, datePath):
    path = "export\\csv\\"
    path = path + channelName + "\\"
    path = path + datePath + "\\"
    return path

def extract_chat_properties(chat):
    chatList = []
    for message in chat:
        comment = {"id": message["message_id"], "time": " " + message["time_text"], "type": message["action_type"], "message": message["message"]}

        if "emotes" in message:
            emo = message["emotes"][0]["id"]
            name = message["emotes"][0]["name"]
            replacedMassage = message["message"].replace(name, emo)
            comment["message"] = replacedMassage

        chatList.append(comment)

    return chatList

def create_csv(chatList, path, videoTitle):
    os.makedirs(path, exist_ok=True)
    os.chmod(path, mode=0x777)
    path = path + videoTitle + ".csv"
    try:
        with open(path, 'w', encoding='utf_8_sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames = ["id", "time", "type", "message"])
            writer.writeheader()
            writer.writerows(chatList)
    except Exception as e:
        print(e)
        os.rmdir(path)
    return

def test_create_file():
    try:
        with open("export\\csv\\test.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames = ["id", "text"])
            writer.writeheader()
            writer.writerow({"id": 1, "text": "this is first message"})
            writer.writerow({"id": 2, "text": "this is second message"})
    except Exception as e:
        print(e)
    return
def test_create_folder():
    os.makedirs("export\\csv\\test\\test.csv", exist_ok=True)
    return
def test_create_folder_with_arg(path):
    os.makedirs("export\\csv\\{path}\\test.csv".format(path=path), exist_ok=True)