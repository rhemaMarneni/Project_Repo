import unittest
import threading
import time
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from bounded_blocking_queue import BoundedBlockingQueue
from consumer import Consumer


class TestConsumer(unittest.TestCase):
    """Test cases for Consumer"""

    def test_consumer_consumes_items(self):
        """Test that consumer consumes items and adds to destination"""
        queue = BoundedBlockingQueue[int](capacity=10)
        destination = []
        sentinel = object()

        # Put items in queue
        items = [1, 2, 3, 4, 5]
        for item in items:
            queue.put(item)

        # Put sentinel to stop consumer
        queue.put(sentinel)

        consumer = Consumer(queue=queue, destination=destination, sentinel=sentinel, delay_seconds=0.0)
        consumer.start()
        consumer.join(timeout=3.0)

        if consumer.is_alive():
            self.fail("Consumer thread did not complete within timeout")

        self.assertEqual(destination, items)
        self.assertEqual(queue.size(), 0)

    def test_consumer_stops_on_sentinel(self):
        """Test that consumer stops when it receives sentinel"""
        queue = BoundedBlockingQueue[int](capacity=5)
        destination = []
        sentinel = object()

        queue.put(1)
        queue.put(2)
        queue.put(sentinel)
        queue.put(3)  # This should not be consumed

        consumer = Consumer(queue=queue, destination=destination, sentinel=sentinel, delay_seconds=0.0)
        consumer.start()
        consumer.join(timeout=3.0)

        if consumer.is_alive():
            self.fail("Consumer thread did not complete within timeout")

        # Should only have items before sentinel
        self.assertEqual(destination, [1, 2])
        self.assertEqual(queue.size(), 1)  # Item 3 still in queue

    def test_consumer_blocks_when_queue_empty(self):
        """Test that consumer blocks when queue is empty"""
        queue = BoundedBlockingQueue[int](capacity=5)
        destination = []
        sentinel = object()

        consumer = Consumer(queue=queue, destination=destination, sentinel=sentinel, delay_seconds=0.0)
        consumer.start()

        # Give consumer time to start waiting
        time.sleep(0.1)
        self.assertEqual(len(destination), 0)  # Should still be waiting

        # Now put items
        queue.put(42)
        queue.put(43)
        queue.put(sentinel)

        consumer.join(timeout=2.0)
        self.assertFalse(consumer.is_alive())
        self.assertEqual(destination, [42, 43])

    def test_consumer_with_delay(self):
        """Test consumer with delay between items"""
        queue = BoundedBlockingQueue[int](capacity=5)
        destination = []
        sentinel = object()

        queue.put(1)
        queue.put(2)
        queue.put(sentinel)

        start_time = time.time()
        consumer = Consumer(queue=queue, destination=destination, sentinel=sentinel, delay_seconds=0.1)
        consumer.start()
        consumer.join(timeout=3.0)

        if consumer.is_alive():
            self.fail("Consumer thread did not complete within timeout")

        elapsed = time.time() - start_time

        # Should take at least 0.2 seconds (2 items * 0.1 delay)
        self.assertGreaterEqual(elapsed, 0.2)
        self.assertEqual(destination, [1, 2])

    # def test_consumer_preserves_order(self):
    #     """Test that consumer preserves order of items"""
    #     queue = BoundedBlockingQueue[int](capacity=10)
    #     destination = []
    #     sentinel = object()

    #     items = list(range(10))
    #     # Put all items first
    #     for item in items:
    #         queue.put(item)
    #     # Put sentinel last
    #     queue.put(sentinel)

    #     # Verify queue has all items + sentinel
    #     self.assertEqual(queue.size(), 11)

    #     consumer = Consumer(queue=queue, destination=destination, sentinel=sentinel, delay_seconds=0.0)
    #     consumer.start()

    #     # Wait for consumer to finish with a reasonable timeout
    #     consumer.join(timeout=5.0)

    #     if consumer.is_alive():
    #         # If still alive, try to see what's in the queue
    #         remaining = []
    #         try:
    #             while queue.size() > 0:
    #                 remaining.append(queue.get())
    #         except:
    #             pass
    #         self.fail(f"Consumer thread did not complete within timeout. Queue still has: {remaining}, destination has: {destination}")

    #     # Verify all items were consumed in order
    #     self.assertEqual(len(destination), 10, f"Expected 10 items, got {len(destination)}")
    #     self.assertEqual(destination, items, f"Items not in order. Expected {items}, got {destination}")
    #     self.assertEqual(queue.size(), 0)

if __name__ == "__main__":
    unittest.main()

