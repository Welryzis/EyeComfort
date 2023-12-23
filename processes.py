import time
from multiprocessing import Process
from tgbot import send_message


class TimerManager:
    def __init__(self):
        self.processes = []

    @staticmethod
    def timer(s):
        time.sleep(s * 60)
        send_message()

    def create_timer(self, sec: int):
        process = Process(target=TimerManager.timer, args=(sec,), name="timer", daemon=True)
        process.start()
        self.processes.append(process)
        return True

    def check_timer(self):
        for process in self.processes:
            process: Process
            if process.name == "timer":
                return process.is_alive()
        return False

    def stop_timer(self):
        for process in self.processes:
            process: Process
            if process.name == "timer" and process.is_alive():
                process.terminate()
