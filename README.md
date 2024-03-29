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

cd myFastApi/

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
git clone https://github.com/aceliuchanghong/myFastApi.git
cd myFastApi/
# 只需要安装docker就好了
sudo docker build -t myfastapi_sisconsavior .
sudo docker run -d --name myFastApi_start -p 80:80 myfastapi_sisconsavior
# docker rmi myfastapi_sisconsavior
# http://9zhouwei.com/
```
<details>
<summary>docker 上传docker hub</summary>

    docker login
    # 输入账号密码 然后查看
    docker images
    # 修改新的标签名
    docker tag myfastapi_sisconsavior aceliuchanghong/myfastapi_sisconsavior:V1.0
    # 查看获取容器/镜像的元数据
    docker inspect aceliuchanghong/myfastapi_sisconsavior
    # 命令将镜像上传到docker hub的仓库
    docker push aceliuchanghong/myfastapi_sisconsavior:V1.0
    # 拉取
    docker pull aceliuchanghong/myfastapi_sisconsavior:V1.0
    # 开始执行
    docker run -d --name myFastApi_start -p 80:80 aceliuchanghong/myfastapi_sisconsavior:V1.0
</details>

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
