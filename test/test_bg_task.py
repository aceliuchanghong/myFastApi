from time import sleep
from typing import Optional


def write_log(message: Optional[str] = "world"):
    print("hello")
    sleep(10)
    print(message)
