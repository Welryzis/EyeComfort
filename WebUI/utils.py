from pywebio.session import run_js
import time
from .tgbot import send_message


def timer(s):
    time.sleep(s * 60)
    send_message()


def update():
    run_js('window.location.reload()')
