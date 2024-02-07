gpt提示语句:
使用的后端是fastapi,前端bootstrap+jinja2,已经引入了
```
<script src="{{ url_for('static', path='/others_js/jquery.min.js') }}"></script>
<!-- Popper.JS -->
<script src="{{ url_for('static', path='/others_js/popper.min.js') }}"></script>
<!-- Bootstrap JS -->
<script src="{{ url_for('static', path='/others_js/bootstrap.bundle.min.js') }}"></script>
```

请尽量使用已有的脚本完成以下任务,如果解决方案够完美，我可以支付10$小费。
```structure
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
任务模板
```https://jszoo.com/detail/32#heading-5
name: Docker Image CI/CD # workflow名称，可以随意改
on: # workflow的事件钩子，告知程序说明时候出发自动部署
  push:
    branches: [ master ] # 在master分支有push操作的时候自动部署
jobs:
  build: # 打包并上传docker镜像
    runs-on: ubuntu-latest # 依赖的环境      
    steps:
      - uses: actions/checkout@v2
      - name: Build Image
      # ${{ secrets.DOCKER_REPOSITORY }}是读取之前在Secret创建的名为DOCKER_REPOSITORY的值
        run: docker build -t ${{ secrets.DOCKER_REPOSITORY }}:latest ./ # 打包并docker镜像，版本为latest
      - name: Login to Registry # 登录阿里云镜像服务器
        run: docker login --username=${{ secrets.DOCKER_USERNAME }} --password ${{ secrets.DOCKER_PASSWORD }} registry.cn-hangzhou.aliyuncs.com
      - name: Push Image # 推送镜像，设置版本为latest
        run: docker push ${{ secrets.DOCKER_REPOSITORY }}:latest
  pull-docker: # docker部署
    needs: [build]
    name: Pull Docker
    runs-on: ubuntu-latest
    steps:
      - name: Deploy
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.HOST }} # 服务器ip
          username: ${{ secrets.HOST_USERNAME }} # 服务器登录用户名
          password: ${{ secrets.HOST_PASSWORD }} # 服务器登录密码
          port: ${{ secrets.HOST_PORT }} # 服务器ssh端口
          script: |
              # 停止旧版容器
            docker stop $(docker ps --filter ancestor=${{ secrets.DOCKER_REPOSITORY }} -q)
            # 删除旧版容器
            docker rm -f $(docker ps -a --filter ancestor=${{ secrets.DOCKER_REPOSITORY }}:latest -q)
            # 删除旧版镜像
            docker rmi -f $(docker images ${{ secrets.DOCKER_REPOSITORY }}:latest -q)
            # 登录阿里云镜像服务器
            docker login --username=${{ secrets.DOCKER_USERNAME }} --password ${{ secrets.DOCKER_PASSWORD }} registry.cn-hangzhou.aliyuncs.com
            # 拉取最新latest版本镜像
            docker pull ${{ secrets.DOCKER_REPOSITORY }}:latest
            # 运行最新latest版本镜像
            docker run -d -p 8000:4000 ${{ secrets.DOCKER_REPOSITORY }}:latest
```