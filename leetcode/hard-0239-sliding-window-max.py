from collections import Counter
import heapq


def sliding_window_v1(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    output: list[int] = []

    for i in range(n - k + 1):
        output.append(max(nums[i : i + k]))

    return output


class MaxHeap:
    def __init__(self, items: list[int] | None = None) -> None:
        if items is None:
            items = []

        self._heap: list[int] = [-i for i in items]
        heapq.heapify(self._heap)
        self._counts: Counter[int] = Counter(self._heap)

    def add(self, item: int) -> None:
        self._counts[-item] += 1
        heapq.heappush(self._heap, -item)

    def remove(self, item: int) -> None:
        if self._counts[-item] > 0:
            self._counts[-item] -= 1

    def __getitem__(self, index: int) -> int:
        while self._heap and self._counts[self._heap[0]] == 0:
            _ = heapq.heappop(self._heap)

        # keep the heap[0] api consistent in heap module
        return -self._heap[index]


def sliding_window_v2(nums: list[int], k: int) -> list[int]:
    heap: MaxHeap = MaxHeap(nums[:k])
    window: list[int] = [heap[0]]

    for i in range(k, len(nums)):
        heap.add(nums[i])
        heap.remove(nums[i - k])
        window.append(heap[0])

    return window


# sliding_window = sliding_window_v1
sliding_window = sliding_window_v2


def test():
    assert sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        3,
        3,
        5,
        5,
        6,
        7,
    ]
    assert sliding_window([1], 1) == [1]
