import unittest
import threading
import time
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from bounded_blocking_queue import BoundedBlockingQueue
from producer import Producer


class TestProducer(unittest.TestCase):
    """Test cases for Producer"""

    def test_producer_runs_and_puts_items(self):
        """Test that producer puts all items from source into queue"""
        queue = BoundedBlockingQueue[int](capacity=10)
        sentinel = object()
        source = [1, 2, 3, 4, 5]

        producer = Producer(source=source, queue=queue, sentinel=sentinel, delay_seconds=0.0)
        producer.start()
        producer.join(timeout=2.0)

        # Should have all items plus sentinel
        self.assertEqual(queue.size(), 6)

        # Verify items are in queue (order may vary due to threading, but all should be there)
        items = []
        for _ in range(5):
            item = queue.get()
            self.assertNotEqual(item, sentinel)
            items.append(item)

        self.assertEqual(set(items), set(source))

        # Last item should be sentinel
        self.assertEqual(queue.get(), sentinel)

    def test_producer_sends_sentinel_at_end(self):
        """Test that producer sends sentinel after all items"""
        queue = BoundedBlockingQueue[int](capacity=10)
        sentinel = object()
        source = [10, 20, 30]

        producer = Producer(source=source, queue=queue, sentinel=sentinel, delay_seconds=0.0)
        producer.start()
        producer.join(timeout=2.0)

        # Get all items including sentinel
        items = []
        for _ in range(4):  # 3 items + 1 sentinel
            items.append(queue.get())

        # Last item should be sentinel
        self.assertEqual(items[-1], sentinel)
        # First 3 should not be sentinel
        for item in items[:-1]:
            self.assertNotEqual(item, sentinel)

    def test_producer_with_delay(self):
        """Test producer with delay between items"""
        queue = BoundedBlockingQueue[int](capacity=10)
        sentinel = object()
        source = [1, 2]

        start_time = time.time()
        producer = Producer(source=source, queue=queue, sentinel=sentinel, delay_seconds=0.1)
        producer.start()
        producer.join(timeout=2.0)
        elapsed = time.time() - start_time

        # Should take at least 0.2 seconds (2 items * 0.1 delay)
        self.assertGreaterEqual(elapsed, 0.2)
        self.assertEqual(queue.size(), 3)  # 2 items + sentinel

    def test_producer_with_empty_source(self):
        """Test producer with empty source"""
        queue = BoundedBlockingQueue[int](capacity=5)
        sentinel = object()
        source = []

        producer = Producer(source=source, queue=queue, sentinel=sentinel, delay_seconds=0.0)
        producer.start()
        producer.join(timeout=1.0)

        # Should only have sentinel
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.get(), sentinel)

    def test_producer_blocks_when_queue_full(self):
        """Test that producer blocks when queue is full"""
        queue = BoundedBlockingQueue[int](capacity=2)
        sentinel = object()
        source = [1, 2, 3, 4, 5]  # More items than capacity

        producer = Producer(source=source, queue=queue, sentinel=sentinel, delay_seconds=0.0)
        producer.start()

        # Give producer time to fill queue
        time.sleep(0.1)

        # Queue should be at capacity (producer should be blocked)
        self.assertEqual(queue.size(), 2)

        # Consume items to allow producer to continue
        for _ in range(5):
            queue.get()

        # Also get the sentinel
        queue.get()

        producer.join(timeout=3.0)
        self.assertFalse(producer.is_alive(), "Producer thread did not complete")


if __name__ == "__main__":
    unittest.main()

