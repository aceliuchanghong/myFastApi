初始化:
使用的后端是fastapi,前端bootstrap+jinja2,已经引入了
```
<script src="{{ url_for('static', path='/others_js/jquery-3.7.1.min.js') }}"></script>
<!-- Popper.JS -->
<script src="{{ url_for('static', path='/others_js/popper.min.js') }}"></script>
<!-- Bootstrap JS -->
<script src="{{ url_for('static', path='/others_js/bootstrap.bundle.min.js') }}"></script>
```
请尽量使用已有的脚本完成以下任务


这个是之前我参考的别人的项目的项目结构,使用FastApi+bootstrap+jquery+jinja2+sqlite开发,并且将md文件嵌入fastapi
```示例
def openfile(filename):
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    data = {
        "text": html
    }
    return data
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})
```
```
myFastApi/
|
├── main.py
├── requirements.txt
├── backend/
│   ├── api/
│   ├── app/
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── test_routes.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── library/
│   │   └── helpers.py
│   └── pages/
│       ├── FAQ.md
│       ├── about.md
│       ├── about_us.md
│       ├── accordion.md
│       ├── contact.md
│       ├── crawl_url.md
│       ├── deal_images.md
│       ├── home.md
└── frontend/
    ├── static/
    │   ├── css/
    │   │   ├── mystyle.css
    │   │   └── style3.css
    │   ├── others_css/
    │   │   └── bootstrap.min.css
    │   └── others_js/
    │       ├── bootstrap.bundle.min.js
    │       ├── jquery.min.js
    └── templates/
        ├── 404.html
        ├── base.html
        ├── error.html
        ├── info.html
        ├── login.html
        ├── logout.html
        ├── page.html
        ├── task.html
```
我现在也需要设计一个类似的项目,开发,帮我参考以上结构优化项目backend的设计,帮我设想一下backend的目录层次
