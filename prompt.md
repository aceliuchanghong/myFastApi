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