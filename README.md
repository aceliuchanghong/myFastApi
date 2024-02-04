### myFastApi

### install

<details>
<summary>开发使用</summary>

    pip list --format=freeze > requirements.txt
    
    pip install easy-media-utils --proxy=127.0.0.1:10809
    
    pip install -r requirements.txt --proxy=127.0.0.1:10809
    
    域名只需要修改godaddy里面的A对应的就可以了
</details>


git clone https://github.com/aceliuchanghong/myFastApi.git

conda create -n myfastapi2 python=3.9.6

conda activate myfastapi2

pip install -r requirements.txt

### ffmpeg

前往官网,下载对应版本的文件,解压放在本地文件并且配置环境变量,确保可以访问到

```
sudo apt update && sudo apt upgrade
sudo apt install ffmpeg
ffmpeg -version
```

### docker install

```
# 之后执行的
cd myFastApi
docker build -t myfastapi_sisconsavior .
docker run -d --name myFastApi_start -p 80:80 myfastapi_sisconsavior
# docker rmi myfastapi_sisconsavior
# 
```

### project

```stucture
myFastApi/
|
├── Dockerfile
├── LICENSE
├── README.md
├── config.py
├── main.py
├── requirements.txt
├── backend_prd/
│   ├── api/
│   │   ├── models/
│   │   │   ├── audio.py
│   │   │   ├── image.py
│   │   │   ├── others.py
│   │   │   ├── user.py
│   │   │   ├── video.py
│   │   │   └── webpage.py
│   │   ├── routes/
│   │   │   ├── audio.py
│   │   │   ├── auth.py
│   │   │   ├── image.py
│   │   │   ├── start.py
│   │   │   ├── video.py
│   │   │   └── webpage.py
│   │   └── schemas/
│   │       └── sql_details.py
│   └── core/
│       ├── audio_processor.py
│       ├── database.py
│       ├── exception_handlers.py
│       ├── image_processor.py
│       ├── security.py
│       ├── site_basic.db
│       └── video_processor.py
└── utils/
    ├── path_valid.py
    └── url_valid.py
```
