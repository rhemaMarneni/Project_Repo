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

## Terminal Output:
```
Scenario 1
Producing item ---- 0
Consumed item ---- 0
Producing item ---- 1
Consumed item ---- 1
Producing item ---- 2
Consumed item ---- 2
Producing item ---- 3
Producing item ---- 4
Consumed item ---- 3
Producing item ---- 5
Consumed item ---- 4
Producing item ---- 6
Producing item ---- 7
Consumed item ---- 5
Producing item ---- 8
Consumed item ---- 6
Producing item ---- 9
Producer finished, sending sentinel
Queue is full, Producer is waiting for space. Current size: 3
Consumed item ---- 7
Consumed item ---- 8
Consumed item ---- 9
Consumer received sentinel, stopping

Scenario 2
Producing item ---- 0
Queue is empty, Consumer is waiting for an item. Current size: 0
Consumed item ---- 0
Producing item ---- 1
Producing item ---- 2
Consumed item ---- 1
Producing item ---- 3
Producing item ---- 4
Consumed item ---- 2
Producing item ---- 5
Producing item ---- 6
Consumed item ---- 3
Producing item ---- 7
Producing item ---- 8
Producing item ---- 9
Queue is full, Producer is waiting for space. Current size: 5
Consumed item ---- 4
Producer finished, sending sentinel
Queue is full, Producer is waiting for space. Current size: 5
Consumed item ---- 5
Consumed item ---- 6
Consumed item ---- 7
Consumed item ---- 8
Consumed item ---- 9
Consumer received sentinel, stopping
```

## Testing

To run all unit tests:
```bash
python3 -m pytest tests/ -v
```
