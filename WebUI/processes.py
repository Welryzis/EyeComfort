from multiprocessing import Process
from .utils import timer


class TimerManager:
    def __init__(self):
        self.processes = []

    def create_timer(self, sec: int):
        process = Process(target=timer, args=(sec,), name="timer", daemon=True)
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
