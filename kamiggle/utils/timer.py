import time

from contextlib import contextmanager


@contextmanager
def timer(name):
    """
    how to use
    ---
    with timer("wait"):
        time.sleep(2.p)
    """
    t0 = time.time()
    yield
    print(f"[{name}] done in {time.time() - t0:.0f} s")
