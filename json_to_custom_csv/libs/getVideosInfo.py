from googleapiclient.discovery import build

# TODO: dont hard-code

DEVELOPER_KEY = "AIzaSyCJMadn3RLVL7ax3OhohhxIAmbVCBnef1U"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# https://developers.google.com/youtube/v3/code_samples/python?hl=ja#search_by_keyword
def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
    
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()
    
    videos = []
    channels = []
    playlists = []
    
def gev_videos_info():
    video = {}
    search_response = youtube.search().list(
        part = "id,snippet",
        channelId = channel.id,
        maxResults = 50,
        order = "date",
    ).execute()