import time
import psutil
import os


class MyProcess:

    def __init__(self, name):
        self.name = name

    def get_pid_by_name(self, name):
        self.name = name
        for proc in psutil.process_iter():
            if proc.name() == name:
                return proc.pid

    def kill_proc_by_id(self, name):
        self.name = name
        pid = self.get_pid_by_name(name)
        for proc in psutil.process_iter():
            if proc.pid == pid:
                proc.kill()

    def check_if_proc_running(self, name):
        self.name = name
        pid = self.get_pid_by_name(name)
        for proc in psutil.process_iter():
            if proc.pid == pid and proc.status() == "running":
                return True
        return False

    def start_process_by_name(self, name):
        self.name = name
        os.system("start %s" % name)

    def get_performance(self, name):
        self.name = name
        for proc in psutil.process_iter():
            if proc.name() == name:
                return proc.memory_percent()

