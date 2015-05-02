# Whos doesn't like watching HD movies.But it is so tiring waiting for new torrents to be downloaded manually with 
#finding new ones weekly .No such hassels now as this scrapper will download all yearly YIFY HD movies 
#for you at once.Just change year in url to change yearly download
#GPL Licence Developed by Chirag Matkar
import requests;
from bs4 import BeautifulSoup
import urllib
import os

def download_torrent(url):
    fname = os.getcwd() + '/' + url.split('title=')[-1] + '.torrent'
    # http://stackoverflow.com/a/14114741/1302018
    try:
        r = requests.get(url, stream=True)
        with open(fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
    except requests.exceptions.RequestException as e:
        print('\n' + OutColors.LR + str(e))
        sys.exit(1)
 
    return fname
	
	
cont = requests.get("https://kickass.to/usearch/yify%20720p%202014")
soup = BeautifulSoup(cont.content)
href = [a.get('href') for a in soup.find_all('a', {'title':'Download torrent file'})]

#for x in range(2,15):
#	cont = requests.get("https://kickass.to/usearch/yify%20720p%202014/"+str(x))
#	soup = BeautifulSoup(cont.content)
#	href.extend([a.get('href') for a in soup.find_all('a', {'title':'Download torrent file'})])


for x in href:	
	fname = download_torrent(x)
