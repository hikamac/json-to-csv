from libs.modules import createCsv
from libs.modules import getVideoIdList
from libs.modules import exeChatDownloader

def create_csvs_from_channel_id(channelId, filename):
    videoIdList = getVideoIdList.get_video_id_list(channelId)
    # videoIdList = getVideoIdList.convert_dict_to_json(videoIdList, filename)
    for id in videoIdList.keys():
        # download chat
        chat = exeChatDownloader.exe_oss_chat_downloader(id)
        if chat is None:
            continue
        chatList = createCsv.extract_chat_properties(chat)

        # create csv file path
        data = videoIdList[id][0]
        videoTitle = exeChatDownloader.get_valid_filename(data['title'])
        publishedAt = data['published_at']
        thumbnail = data['thumbnail']
        datepath = createCsv.make_datepath(publishedAt)
        path = createCsv.make_complete_path(filename, datepath)
        createCsv.create_csv(chatList, path, videoTitle)
        print(videoTitle + "complete")
    return