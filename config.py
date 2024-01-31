from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="frontend_prd/templates")
proxies = {
    "http": "http://127.0.0.1:10809",
    "https": "http://127.0.0.1:10809"
}
