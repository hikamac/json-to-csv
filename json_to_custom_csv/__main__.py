import libs.chatReplayCrawl

def main():
    videoId = '8UpGEKRU4D4'
    print('Video')
    filename = libs.chatReplayCrawl.youtubeChatReplayCrawler(video_id=videoId)
    print(filename)

if __name__ == "__main__":
    main()