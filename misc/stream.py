from dataclasses import dataclass
from typing import Literal


@dataclass
class Event:
    type: Literal["start", "end"]
    time: int


def bucketing(events: list[Event]):
    out: list[tuple[int, int]] = []

    current: int = 0
    count: int = 0
    bucket: int = 0
    while current < len(events):
        event = events[current]
        if event.type == "start" and event.time <= bucket:
            count += 1
            current += 1
        elif event.type == "end" and event.time <= bucket:
            count -= 1
            current += 1
        else:
            out.append((bucket, count))
            bucket += 60

    out.append((bucket, count))
    print(out)
    return out


if __name__ == "__main__":
    events: list[Event] = [Event("start", 360)]
    bucketing(events)
