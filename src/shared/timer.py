import time


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        self._start_time = time.perf_counter()

    def end(self, precision=4, title=None):
        if self._start_time is None:
            raise Exception("Timer.start() needs to be called before Timer.end()")
        if title is None:
            print(f"{time.perf_counter() -  self._start_time:0.{precision}f}s")
        else:
            print(f"{title}: {time.perf_counter() - self._start_time:0.{precision}f}s")
