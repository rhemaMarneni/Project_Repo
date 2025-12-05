import unittest
import time
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from producer_consumer_system import ProducerConsumerSystem


class TestProducerConsumerSystem(unittest.TestCase):
    """Test cases for ProducerConsumerSystem"""

    def test_system_initialization(self):
        """Test system initialization"""
        source = [1, 2, 3, 4, 5]
        system = ProducerConsumerSystem(source=source, capacity=5, producer_delay=0.0, consumer_delay=0.0)

        self.assertEqual(list(system._source_data), source)
        self.assertEqual(list(system._destination_data), [])
        self.assertEqual(system.queue_size(), 0)

    def test_system_runs_and_processes_items(self):
        """Test that system processes all items correctly"""
        source = [1, 2, 3, 4, 5]
        system = ProducerConsumerSystem(source=source, capacity=5, producer_delay=0.0, consumer_delay=0.0)

        system.run()

        # All items should be consumed
        destination = list(system._destination_data)
        self.assertEqual(set(destination), set(source))
        self.assertEqual(len(destination), len(source))
        self.assertEqual(system.queue_size(), 0)

    def test_system_with_empty_source(self):
        """Test system with empty source"""
        source = []
        system = ProducerConsumerSystem(source=source, capacity=5, producer_delay=0.0, consumer_delay=0.0)

        system.run()

        self.assertEqual(list(system._destination_data), [])
        self.assertEqual(system.queue_size(), 0)

    def test_system_with_single_item(self):
        """Test system with single item"""
        source = [42]
        system = ProducerConsumerSystem(source=source, capacity=1, producer_delay=0.0, consumer_delay=0.0)

        system.run()

        self.assertEqual(list(system._destination_data), [42])
        self.assertEqual(system.queue_size(), 0)

    def test_system_with_delays(self):
        """Test system with producer and consumer delays"""
        source = [1, 2, 3]
        system = ProducerConsumerSystem(source=source, capacity=5, producer_delay=0.05, consumer_delay=0.05)

        start_time = time.time()
        system.run()
        elapsed = time.time() - start_time

        # Should take some time due to delays
        self.assertGreater(elapsed, 0.1)
        self.assertEqual(set(system._destination_data), set(source))

    def test_system_with_small_capacity(self):
        """Test system with small capacity (producer will block)"""
        source = list(range(10))
        system = ProducerConsumerSystem(source=source, capacity=2, producer_delay=0.0, consumer_delay=0.0)

        system.run()

        destination = list(system._destination_data)
        self.assertEqual(set(destination), set(source))
        self.assertEqual(len(destination), len(source))

    def test_system_with_different_types(self):
        """Test system with different data types"""
        source = ["hello", "world", 42, [1, 2, 3], None]
        system = ProducerConsumerSystem(source=source, capacity=10, producer_delay=0.0, consumer_delay=0.0)

        system.run()

        destination = list(system._destination_data)
        # Can't use set() because lists are unhashable, so compare lengths and items
        self.assertEqual(len(destination), len(source))
        # Check that all items are present (order may vary)
        for item in source:
            self.assertIn(item, destination)
        for item in destination:
            self.assertIn(item, source)

    def test_queue_size_after_completion(self):
        """Test that queue_size is 0 after system completes"""
        source = [1, 2, 3, 4, 5]
        system = ProducerConsumerSystem(source=source, capacity=5, producer_delay=0.0, consumer_delay=0.0)

        system.run()

        self.assertEqual(system.queue_size(), 0)

    def test_system_preserves_all_items(self):
        """Test that system doesn't lose any items"""
        source = list(range(50))
        system = ProducerConsumerSystem(source=source, capacity=5, producer_delay=0.01, consumer_delay=0.01)

        system.run()

        destination = list(system._destination_data)
        self.assertEqual(len(destination), len(source))
        self.assertEqual(set(destination), set(source))

    def test_system_with_fast_producer_slow_consumer(self):
        """Test system where producer is faster than consumer"""
        source = list(range(10))
        system = ProducerConsumerSystem(source=source, capacity=3, producer_delay=0.01, consumer_delay=0.1)

        system.run()

        destination = list(system._destination_data)
        self.assertEqual(set(destination), set(source))
        self.assertEqual(len(destination), len(source))

    def test_system_with_slow_producer_fast_consumer(self):
        """Test system where consumer is faster than producer"""
        source = list(range(10))
        system = ProducerConsumerSystem(source=source, capacity=5, producer_delay=0.1, consumer_delay=0.01)

        system.run()

        destination = list(system._destination_data)
        self.assertEqual(set(destination), set(source))
        self.assertEqual(len(destination), len(source))

    def test_system_with_iterable_not_list(self):
        """Test system with iterable that's not a list"""
        source = range(10)  # range is an iterable
        system = ProducerConsumerSystem(source=source, capacity=5, producer_delay=0.0, consumer_delay=0.0)

        system.run()

        destination = list(system._destination_data)
        self.assertEqual(set(destination), set(range(10)))
        self.assertEqual(len(destination), 10)


if __name__ == "__main__":
    unittest.main()

