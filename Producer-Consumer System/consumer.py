import threading
import time
from typing import Any, List

from bounded_blocking_queue import BoundedBlockingQueue


class Consumer(threading.Thread):
    """
    Consumer thread class.
    """

    def __init__(self, queue: BoundedBlockingQueue[Any], destination: List[Any], sentinel: Any, delay_seconds: float = 0.0) -> None:
        super().__init__(name="ConsumerThread")
        self._queue = queue
        self._destination = destination
        self._sentinel = sentinel
        self._delay_seconds = delay_seconds

    # run the consumer thread
    def run(self) -> None:
        """
        Consumer thread reads items from the shared queue and stores them in the destination list,
        until it encounters the sentinel, which signals stop.
        """
        while True:
            item = self._queue.get()

            # Sentinel means no more real data
            if item == self._sentinel:
                print("Consumer received sentinel, stopping")
                break

            print(f"Consumed item ---- {item}")
            self._destination.append(item)

            if self._delay_seconds > 0:
                time.sleep(self._delay_seconds)

