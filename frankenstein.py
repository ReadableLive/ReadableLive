from requests import get
from bs4 import BeautifulSoup
import os
import reimport pyttsx3

def read_book(book):
    url = 'https://www.gutenberg.org/files/84/84-h/84-h.htm'
    headers = {'User-Agent': 'ReadableLive'} # Some websites don't accept the pyhon-requests default user-agent
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    book = soup.get_text()
    book = re.sub(r"[\n\r]", ' ', book).strip()
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 125)
    speaker.say(book)
    speaker.runAndWait()
    speaker.stop()