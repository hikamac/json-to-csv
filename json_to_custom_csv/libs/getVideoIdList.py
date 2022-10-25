from optparse import Values
from googleapiclient.discovery import build
import json
import sys

args = sys.argv

DEVELOPER_KEY = "AIzaSyCJMadn3RLVL7ax3OhohhxIAmbVCBnef1U"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_video_id_list(channel_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    nextPageToken = None
    nextPageTokenTmp = None
    videos = {}
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
        
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                values = []
                values.append(search_result["snippet"]["publishedAt"])
                values.append(search_result["snippet"]["title"])
                videos[search_result["id"]["videoId"]] = values
                
        # if ENV == 'dev':
        #     break
        # elif ENV == 'prod':
        #     try:
        #             nextPageToken = search_response["nextPageToken"]
        #     except:
        #         break
        try:
            nextPageToken = search_response["nextPageToken"]
        except:
            break
    print("Videos:\n", "\n".join(videos), "\n")
    return(videos)

channel_id = args[1]
print("channel_id\n",channel_id, "\n")
get_video_id_list(channel_id)