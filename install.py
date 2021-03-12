import requests
import os
import shutil
from constants import chromedriverPath

# Constants
chromedriverUrl = 'https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip'
chromedriverFile = 'chromedriver.zip'

def downloadFile(url, name):
    r = requests.get(url, allow_redirects=True)
    open(name, 'wb').write(r.content)

def downloadChromedriver():
    downloadFile(chromedriverUrl, chromedriverFile)
    shutil.unpack_archive(chromedriverFile, chromedriverPath)

if __name__ == '__main__':
    downloadChromedriver()