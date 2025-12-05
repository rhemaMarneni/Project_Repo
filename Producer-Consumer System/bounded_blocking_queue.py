import threading
from collections import deque
from typing import Deque, Generic, TypeVar

T = TypeVar("T")


class BoundedBlockingQueue(Generic[T]):
    """
    A bounded blocking queue that supports:
    - put: blocks when the queue is full
    - get: blocks when the queue is empty

    Uses a Condition object for wait/notify thread synchronization.
    """

    def __init__(self, capacity: int) -> None:
        # we want to ensure that the holding capacity of queue is positive to run any operation on it
        if capacity < 0:
            raise ValueError("capacity must be positive to operate on queue, exiting...")
        # forbid deadlocks
        if capacity == 0:
            raise ValueError("Capacity is 0, queue will be stuck in a deadlock, exiting...")

        self._capacity = capacity
        self._queue: Deque[T] = deque()
        self._condition = threading.Condition()

    def put(self, item: T) -> None:
        """
        Producer puts an item into the queue.
        Blocked as long as the queue is full (i.e., when maximum capacity is reached)
        """
        with self._condition:
            # While queue is full, wait for space
            while len(self._queue) >= self._capacity:
                print(f"Queue is full, Producer is waiting for space. Current size: {self.size()}")
                self._condition.wait()

            self._queue.append(item)
            # Wake up any consumer waiting on empty
            self._condition.notify_all()

    def get(self) -> T:
        """
        Consumer removes and returns an item from the queue.
        Blocked as long as the queue is empty (i.e., when no items are in the queue)
        """
        with self._condition:
            # While queue is empty, wait for an item
            while not self._queue:
                print(f"Queue is empty, Consumer is waiting for an item. Current size: {self.size()}")
                self._condition.wait()

            item = self._queue.popleft()
            # Wake up any producer waiting on full
            self._condition.notify_all()
            return item

    def size(self) -> int:
        """
        Return the current number of items in the queue.
        """
        with self._condition:
            return len(self._queue)
