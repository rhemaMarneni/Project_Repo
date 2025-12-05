import unittest
import threading
import time
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from bounded_blocking_queue import BoundedBlockingQueue


class TestBoundedBlockingQueue(unittest.TestCase):
    """Test cases for BoundedBlockingQueue"""

    def test_init_valid_capacity(self):
        """Test initialization with valid capacity"""
        queue = BoundedBlockingQueue[int](capacity=5)
        self.assertEqual(queue.size(), 0)

    def test_init_zero_capacity_raises_error(self):
        """Test that zero capacity raises ValueError"""
        with self.assertRaises(ValueError) as context:
            BoundedBlockingQueue[int](capacity=0)
        self.assertIn("deadlock", str(context.exception).lower())

    def test_init_negative_capacity_raises_error(self):
        """Test that negative capacity raises ValueError"""
        with self.assertRaises(ValueError) as context:
            BoundedBlockingQueue[int](capacity=-1)
        self.assertIn("positive", str(context.exception).lower())

    def test_put_and_get_single_item(self):
        """Test putting and getting a single item"""
        queue = BoundedBlockingQueue[int](capacity=5)
        queue.put(42)
        self.assertEqual(queue.size(), 1)
        item = queue.get()
        self.assertEqual(item, 42)
        self.assertEqual(queue.size(), 0)

    def test_put_and_get_multiple_items(self):
        """Test putting and getting multiple items"""
        queue = BoundedBlockingQueue[int](capacity=5)
        items = [1, 2, 3, 4, 5]

        for item in items:
            queue.put(item)
        self.assertEqual(queue.size(), 5)

        retrieved = []
        for _ in range(5):
            retrieved.append(queue.get())

        self.assertEqual(retrieved, items)
        self.assertEqual(queue.size(), 0)

    def test_capacity_limit(self):
        """Test that queue respects capacity limit"""
        queue = BoundedBlockingQueue[int](capacity=3)

        queue.put(1)
        queue.put(2)
        queue.put(3)
        self.assertEqual(queue.size(), 3)

        # Try to put one more - should block, but we'll test with timeout
        def put_item():
            queue.put(4)

        thread = threading.Thread(target=put_item)
        thread.start()

        # Give it a moment, then consume one item
        time.sleep(0.1)
        self.assertEqual(queue.size(), 3)  # Still at capacity

        # Now consume one, which should allow the put to complete
        item = queue.get()
        thread.join(timeout=1.0)

        self.assertFalse(thread.is_alive())  # Thread should have completed
        self.assertEqual(queue.size(), 3)  # Should have 4 items now (1 consumed, 4 added)

    def test_get_blocks_when_empty(self):
        """Test that get blocks when queue is empty"""
        queue = BoundedBlockingQueue[int](capacity=5)
        result = []

        def get_item():
            result.append(queue.get())

        thread = threading.Thread(target=get_item)
        thread.start()

        # Give it a moment to start waiting
        time.sleep(0.1)
        self.assertEqual(len(result), 0)  # Should still be waiting

        # Now put an item, which should unblock the get
        queue.put(99)
        thread.join(timeout=1.0)

        self.assertFalse(thread.is_alive())
        self.assertEqual(result, [99])

    def test_multiple_producers_consumers(self):
        """Test queue with multiple producer and consumer threads"""
        queue = BoundedBlockingQueue[int](capacity=10)
        produced = []
        consumed = []
        lock = threading.Lock()

        def producer(start, count):
            for i in range(start, start + count):
                queue.put(i)
                with lock:
                    produced.append(i)

        def consumer(count):
            for _ in range(count):
                item = queue.get()
                with lock:
                    consumed.append(item)

        # Create multiple producers and consumers
        threads = []
        for i in range(3):
            t = threading.Thread(target=producer, args=(i * 10, 10))
            threads.append(t)
            t.start()

        for _ in range(3):
            t = threading.Thread(target=consumer, args=(10,))
            threads.append(t)
            t.start()

        # Wait for all threads with timeout
        for t in threads:
            t.join(timeout=5.0)
            if t.is_alive():
                self.fail(f"Thread {t.name} did not complete within timeout")

        # Verify all items were processed
        self.assertEqual(len(produced), 30)
        self.assertEqual(len(consumed), 30)
        self.assertEqual(queue.size(), 0)

    def test_different_types(self):
        """Test queue with different data types"""
        # Test with strings
        queue_str = BoundedBlockingQueue[str](capacity=5)
        queue_str.put("hello")
        self.assertEqual(queue_str.get(), "hello")

        # Test with lists
        queue_list = BoundedBlockingQueue[list](capacity=5)
        test_list = [1, 2, 3]
        queue_list.put(test_list)
        self.assertEqual(queue_list.get(), test_list)

        # Test with None
        queue_none = BoundedBlockingQueue[type(None)](capacity=5)
        queue_none.put(None)
        self.assertIsNone(queue_none.get())


if __name__ == "__main__":
    unittest.main()

