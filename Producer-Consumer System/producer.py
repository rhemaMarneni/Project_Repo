import threading
import time
from typing import Any, Iterable

from bounded_blocking_queue import BoundedBlockingQueue


class Producer(threading.Thread):
    """
    Producer thread class.
    """

    def __init__(self, source: Iterable[Any], queue: BoundedBlockingQueue[Any], sentinel: Any, delay_seconds: float = 0.0) -> None:
        super().__init__(name="ProducerThread")
        self._source = source
        self._queue = queue
        self._sentinel = sentinel
        self._delay_seconds = delay_seconds

    #run the producer thread
    def run(self) -> None:
        """
        Producer thread reads items from the source iterable and places them into the shared queue,
        until it encounters the sentinel, which signals stop.
        """
        for item in self._source:
            print(f"Producing item ---- {item}")
            self._queue.put(item)
            if self._delay_seconds > 0:
                time.sleep(self._delay_seconds)

        # Indicate that production has finished
        print("Producer finished, sending sentinel")
        self._queue.put(self._sentinel)

