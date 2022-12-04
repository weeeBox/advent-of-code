from heapq import heappush, heappop


class PriorityQueue(object):
    def __init__(self, items=tuple(), ismin=True):
        self._ismin = ismin
        self._items = []
        for item in map(self._make_item, items):
            self.push(item)

    def push(self, value):
        heappush(self._items, self._make_item(value))

    def pop(self):
        return self._pop(self._items)

    @property
    def items(self) -> tuple:
        temp = self._items[:]
        res = []
        while temp:
            res.append(self._pop(temp))

        return tuple(res)

    @staticmethod
    def _pop(items):
        return heappop(items).value

    def _make_item(self, value):
        return _HeapItem(value=value, ismin=self._ismin)

    def __bool__(self):
        return len(self) > 0

    def __len__(self):
        return len(self._items)


class _HeapItem(object):
    def __init__(self, value, ismin=True):
        self._value = value
        self._ismin = ismin

    @property
    def value(self):
        return self._value

    def __lt__(self, other):
        return self.value < other.value if self._ismin else self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)
