# utils/fetch_kokkai.py
import requests
from bs4 import BeautifulSoup

def get_speech_by_name(name, max_count=100):
    base_url = "https://kokkai.ndl.go.jp/api/speech"
    params = {
        "speaker": name,
        "recordPacking": "xml",
        "maximumRecords": str(max_count)
    }
    response = requests.get(base_url, params=params)
    print(f"Fetching speeches for: {name} with params: {params}")
    

    speeches = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "xml")
        #print(soup)
        for speech in soup.find_all("speech"):
            print()
            speechtext  =speech.text
            if speechtext:
                speeches.append(speechtext)
    return speeches