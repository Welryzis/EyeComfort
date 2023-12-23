from pywebio.input import *
from pywebio.output import *
from .utils import *
from processes import TimerManager


class FocusManager:
    def __init__(self):
        self.timer_manager = TimerManager()
        self.running = False
        self.focus_time: int = 25

    def change_time(self):
        with use_scope("change_focus_time", clear=True):
            self.focus_time = int(input("Enter new focus time value. (In minutes) ",
                                        type=NUMBER))
        clear("change_focus_time")
        update()

    def start(self):
        self.timer_manager.create_timer(self.focus_time)
        self.running = True
        update()

    def stop(self):
        self.timer_manager.stop_timer()
        self.running = False
        update()
