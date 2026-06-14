import random
from typing import Generator

actions: list[str] = [
    "run", "eat", "sleep", "grab", "move", "climb", "swim", "release"
]

players: list[str] = [
    "alice", "bob", "charlie", "dylan"
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list[tuple[str, str]]) -> Generator[
        tuple[str, str], None, None]:
    while events:
        index = random.randint(0, len(events) - 1)
        event = events[index]
        del events[index]
        yield event


def ft_data_stream() -> None:
    gen = gen_event()
    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")
    events = [next(gen) for i in range(10)]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


ft_data_stream()
