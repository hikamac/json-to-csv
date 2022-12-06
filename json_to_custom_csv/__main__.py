from libs.modules import getVideoIdList
from libs.modules import exeChatDownloader
from libs.modules import createCsv

def main():
    videoId = "Ve6X2WQ5G24"
    chat = exeChatDownloader.exe_oss_chat_downloader(videoId)
    chatList = createCsv.extract_chat_properties(chat)
    datepath = createCsv.make_datepath("2020-02-03T11:50:22Z")
    path = createCsv.make_complete_path("Marpril", datepath)
    createCsv.create_csv(chatList, path, "立花の原始的ポケモン実況 #03")
    return

def create_csvs_from_channel_id(channelId):
    channelId = 'UCWhv732tk4DAQ7X32qHKrfA'
    # filename = 'marprilvideoids'
    videoIdList = getVideoIdList.get_video_id_list(channelId)
    # videoIdList = getVideoIdList.convert_dict_to_json(videoIdList, filename)
    for id in videoIdList.keys():
        data = videoIdList[id][0]
        videoTitle = exeChatDownloader.get_valid_filename(data['title'])
        publishedAt = data['published_at']
        thumbnail = data['thumbnail']
        path = exeChatDownloader.make_path_from_date(publishedAt, videoTitle)
        print(path)
        # chat = exeChatDownloader.exe_oss_chat_downloader(id)
        # exeChatDownloader.convert_chat_to_json(chat, videoTitle)
    return

if __name__ == "__main__":
    main()