git clone https://github.com/ytdl-org/youtube-dl.git youtube-dl

cd youtube-dl/

(sudo apt install make
sudo apt install zip)
make youtube-dl
youtube-dl -h

sudo cp youtube-dl /usr/local/bin/


youtube-dl -o "/home/aceliuchanghong/youtube-dl/data/00.mkv" https://www.youtube.com/watch?v=OIBODIPC_8Y&ab_channel=Ayase%2FYOASOBI
youtube-dl https://twitter.com/CatsIX/status/1750594548072431833?s=20
```text
from __future__ import unicode_literals
import youtube_dl    
class MyLogger(object):    
    def debug(self, msg):        
        pass    
    def warning(self, msg):        
        pass    
    def error(self, msg):        
        print(msg)

def my_hook(d):    
    if d['status'] == 'finished':
        pass

ydl_opts = {        
    'format':'bestvideo[height<=480]+bestaudio/best[height<=480]',
     'outtmpl': filename,        
    # 'outtmpl': 'c:/images/%(id)s%(ext)s',        
    # 'cookiefile':'fbcookie.txt',        
    'postprocessors': [{                        
    'key': 'FFmpegVideoConvertor',                        
    'preferedformat': 'mp4'                        
    }],        
'logger': MyLogger(),        
'progress_hooks': [my_hook],    
}    
with youtube_dl.YoutubeDL(ydl_opts) as ydl:        
    ydl.download([url])
```