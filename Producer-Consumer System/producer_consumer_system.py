from typing import Any, Iterable, List

from bounded_blocking_queue import BoundedBlockingQueue
from consumer import Consumer
from producer import Producer


class ProducerConsumerSystem:
    """
    System class that ties together the producer, consumer, and bounded blocking queue
    """

    def __init__(self, source: Iterable[Any], capacity: int = 5, producer_delay: float = 0.0, consumer_delay: float = 0.0) -> None:
        self._source_data: List[Any] = list(source) # source data
        self._destination_data: List[Any] = [] # destination data
        self._queue = BoundedBlockingQueue[Any](capacity=capacity) # bounded blocking queue (shared queue that consumer and producer use)
        self._sentinel = object() # sentinel object which marks the end of input stream

        # producer and consumer threads creation
        self._producer = Producer(source=self._source_data, queue=self._queue, sentinel=self._sentinel, delay_seconds=producer_delay)
        self._consumer = Consumer(queue=self._queue, destination=self._destination_data, sentinel=self._sentinel, delay_seconds=consumer_delay)

    def run(self) -> None:
        """
        Start producer and consumer threads and wait for them to finish.
        """
        self._producer.start()
        self._consumer.start()

        self._producer.join()
        self._consumer.join()

    def queue_size(self) -> int:
        """
        Convenience method for current queue size (mostly for debugging).
        """
        return self._queue.size()

