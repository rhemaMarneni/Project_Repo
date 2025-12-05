# Producer-Consumer System

A thread-safe producer-consumer implementation using a bounded blocking queue in Python. using concurrent programming.

- **Producer threads** read items from a source and place them into a shared queue
- **Consumer threads** remove items from the queue and store them in a destination
- **BoundedBlockingQueue** on which thread-safe operations are performed (blocking behavior when the queue is full or empty)


## What I Implemented

### BoundedBlockingQueue

A generic, thread-safe queue with a fixed capacity:
- `put(item)`: Adds an item to the queue, blocks if queue is full
- `get()`: Removes and returns an item, blocks if queue is empty
- `size()`: Returns the current number of items in the queue

### Producer

A thread that reads items from a source iterable and places them into the queue:
- Automatically sends a sentinel value when all items are produced
- Supports configurable delay between items

### Consumer

A thread that continuously reads items from the queue:
- Stops when it encounters the sentinel value
- Stores consumed items in a destination list
- Supports configurable delay between items

### ProducerConsumerSystem

High-level class that orchestrates the producer-consumer pattern:
- Manages source data, destination data, and the shared queue
- Creates and coordinates producer and consumer threads
- Provides a simple `run()` method to execute the system

## Installation

Uses only Python standard library: `threading` for thread management, `collections.deque` for queue implementation, and`typing` for type hints

Python 3.7 was used.

### Custom Scenarios

You can create custom scenarios by adjusting:
- **Capacity**: Controls queue size (affects when producer/consumer block)
- **Producer delay**: Time between producing items
- **Consumer delay**: Time between consuming items

Example scenarios:
- **Fast producer, slow consumer**: Producer fills queue, then blocks
- **Slow producer, fast consumer**: Consumer waits for items

## Testing

To run all unit tests:
```bash
python3 -m pytest tests/ -v
```
