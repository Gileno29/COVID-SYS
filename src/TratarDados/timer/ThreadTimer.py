
from Timer import Timer
import time


class Th(Thread):
    s = Timer()

    def __init__(self):
        Thread.__init__(self)
        self.s.get_dados_service()
        time.sleep(5)

    def run(self):
        self.start()
