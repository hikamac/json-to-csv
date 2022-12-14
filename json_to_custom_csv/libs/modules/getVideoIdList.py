from optparse import Values
from googleapiclient.discovery import build
import json

DEVELOPER_KEY = "AIzaSyCJMadn3RLVL7ax3OhohhxIAmbVCBnef1U"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# return Value
# {
#     "exampleVideoId1": [
#         {
#             "title": "exampleTitle1",
#             "published_at": "2022-11-03T10:20:40Z",
#             "thumbnail": "https://example1.jpg"
#         }
#     ],
#     "exampleVideoId2": [
#         {
#             "title": "exampleTitle2",
#             "published_at": "2022-08-07T12:00:00Z",
#             "thumbnail": "https://example2.jpg"
#         }
#     ],
#     ...
# }

def get_video_id_list(channel_id):
    nextPageToken = None
    nextPageTokenTmp = None
    videos = {}
    count = 0
    while True:
        if nextPageToken != None:
            nextPageTokenTmp = nextPageToken

        search_response = youtube.search().list(
            part = "id,snippet",
            channelId = channel_id,
            maxResults = 50,
            order = "date",
            pageToken = nextPageTokenTmp
            ).execute()
        # print(search_response)
        
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                values = []
                values.append({"title":search_result["snippet"]["title"],
                               "published_at": search_result["snippet"]["publishedAt"],
                               "thumbnail":search_result["snippet"]["thumbnails"]["high"]["url"]})
                videos[search_result["id"]["videoId"]] = values
                
        count += 1
        try:
            nextPageToken = search_response["nextPageToken"]
        except:
            break
    # print("Videos:\n", "\n".join(videos), "\n")
    return(videos)

def convert_dict_to_json(dictionary_data, filename):
    with open("export\\json\\{filename}.json".format(filename=filename), "w", encoding="UTF-8") as f:
            json.dump(dictionary_data, f, ensure_ascii=False, indent=4)
