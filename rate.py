import requests
from bs4 import BeautifulSoup
import csv


HOST = "https://www.google.com/"
URL = "https://www.google.com/search?q=dollar+to+ruble&oq=dollat+t&aqs=chrome.1.69i57j0l7.2911j0j4&sourceid=chrome&ie=UTF-8"
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

def get_html(url, params=''):
    r=requests.get(url, headers=HEADERS, params=params)
    print(r)
