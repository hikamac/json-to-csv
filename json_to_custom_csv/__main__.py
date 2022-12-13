from libs import createCsvFromChId
from libs.modules import getVideoIdList
from libs.modules import exeChatDownloader
from libs.modules import createCsv

def main():
    createCsvFromChId.create_csvs_from_channel_id("UCWhv732tk4DAQ7X32qHKrfA", "Marpril")

if __name__ == "__main__":
    main()