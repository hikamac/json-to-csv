from bs4 import BeautifulSoup
from retry import retry
import ast
import glob
import re
import requests
import sys

def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)

@retry(EOFError, tries=15, delay=10)
def youtubeChatReplayCrawler(video_id):
    youtube_url = "https://www.youtube.com/watch?v="
    
    filename = "C:/python3/json_to_custom_csv/export/json/liveChatLog{video_id}.json".format(video_id=video_id)
    converted_file = "C:/python3/json_to_custom_csv/export/csv/liveChatLog{video_id}.csv".format(video_id=video_id)
    target_url = youtube_url + video_id
    dict_str = ""
    next_url = ""
    comment_data = []
    session = requests.Session()
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    
    if glob.glob(filename):
        print("Already Exists json file")
        return
    elif glob.glob(converted_file):
        print("Already Exists csv file")
        return
    
    html = session.get(target_url)
    soup = BeautifulSoup(html.text, 'html.parser')
    
    title = soup.find_all('title')[0].text.replace(' - YouTube', '')
    title = get_valid_filename(title)
    
    # RE_EMOJI = re.compile('[U00010000-\U0010ffff]', flags=re.UNICODE)
    
    for iframe in soup.find_all('iframe'):
        if("live_chat_replay" in iframe["src"]):
            next_url = iframe["src"]
    if not next_url:
        eof_err_str = "Couldn't find live_chat_replay iframe. Maybe try running again?"
        print(eof_err_str)
        raise EOFError(eof_err_str)
        return(None)

    while(1):
        try:
            html = session.get(next_url, headers=headers)
            soup = BeautifulSoup(html.text, 'lxml')
            
            for script in soup.find_all('script'):
                script_text = str(script)
                if 'utInitialData' in script_text:
                    dict_str = ''.join(script_text.split(" = ")[1:])
            
            dict_str = dict_str.replace("false", "False").replace("true", "True")
            dict_str = re.sub(r'};.*\n.+<\/script>', '}', dict_str)
            
            dict_str = dict_str.rstrip("  \n;")
            dict_str = RE_EMOJI.sub(r'', dict_str)
            
            dics = ast.literal_eval(dict_str)
            
            continue_url = dics["continuationContents"]["liveChatContinuation"]["continuation"][0]["liveChatReplayContinuationData"]["continuation"]
            print("Found another live chat continuation")
            print(continue_url)
            next_url = "https://www.youtube.com/live_chat_replay?continuation{continue_url}".format(continue_url=continue_url)
            
            for samp in dics["continuationContents"]["liveChatContinuation"]["actions"][1:]:
                comment_data.append(str(samp) + "\n")
                
        except requests.ConnectionError:
            print("Connection Error")
            continue
        except requests.HTTPError:
            print("HTTP Error")
            break
        except requests.Timeout:
            print("Timeout")
            continue
        except requests.exceptions.RequestException as e:
            print(e)
            break
        except KeyError as e:
            error = str(e)
            if 'liveChatReplayContinuationData' in error:
                print('Hit last live chat segment, finishing job.')
            else:
                print("KeyError")
                print(e)
            break
        except KeyboardInterrupt:
            break
        except Exception:
            print("Unexpected error:" + str(sys.exc_info()[0]))
            
    with open(filename, mode='W', encoding='utf-8') as f:
        f.writelines(comment_data)
        
    print('Comment data saved to ' + filename)
    return(filename)