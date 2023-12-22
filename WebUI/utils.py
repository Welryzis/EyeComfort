from pywebio.session import run_js
import time
from .tgbot import send_message


def timer(s):
    time.sleep(s)
    send_message()


def update():
    run_js('window.location.reload()')
