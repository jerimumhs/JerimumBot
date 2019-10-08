import time
import logging
from functools import partial, wraps


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


class ThrottleDecorator(object):
    _last_run = 0

    def __init__(self, func, interval, shared):
        self.func = func
        self.interval = interval
        self.shared = shared
        self._last_run = 0

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self.func
        return partial(self, obj)

    def __call__(self, *args, **kwargs):
        now = time.time()

        if now - self.last_run > self.interval:
            self.last_run = now
            return self.func(*args, **kwargs)

        logging.info(f"O comando sofreu throttle. Faltam {self.last_run + self.interval - now} seconds")

    @property
    def last_run(self):
        if self.shared:
            return self.__class__._last_run
        return self._last_run

    @last_run.setter
    def last_run(self, now):
        if self.shared:
            self.__class__._last_run = now
        else:
            self._last_run = now


def throttle(interval=300, shared=True):
    def apply_decorator(func):
        decorator = ThrottleDecorator(func=func, interval=interval, shared=shared)
        return wraps(func)(decorator)
    return apply_decorator
