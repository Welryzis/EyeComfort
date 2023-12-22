import pywebio
from .focus import FocusManager
from pywebio.output import *

focus_manager = FocusManager()


@pywebio.config(title="EyeComfort", theme="dark")
def main_menu():
    clear()

    put_table([
        ["Eye", "Comfort"],

        [put_button("Start", focus_manager.start, disabled=focus_manager.running),
         put_button("Stop", focus_manager.stop, disabled=not focus_manager.running)],

        ["Focus time", put_table([
            [f"{focus_manager.focus_time}m", put_button("Change", focus_manager.change_time)],
        ])],
    ])
