from producer_consumer_system import ProducerConsumerSystem


if __name__ == "__main__":
    source_items = list(range(10))

    # test different scenarios with capacities and delays
    # Scenario 1
    print("Scenario 1")
    system1 = ProducerConsumerSystem(source=source_items, capacity=3, producer_delay=0.1, consumer_delay=0.15)
    system1.run()
    print()

    # Scenario 2 – "queue empty, consumer waiting"
    print("Scenario 2")
    system2 = ProducerConsumerSystem(source=source_items, capacity=5, producer_delay=0.02, consumer_delay=0.05)
    system2.run()
