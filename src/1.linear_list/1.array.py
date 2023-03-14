class PArray(object):
    """模拟数组"""

    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position: int) -> object:
        return self._data[position]

    def __setitem__(self, index: int, value: object) -> None:
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    def insert(self, index: int, value: object) -> None:
        if len(self) >= self._capacity:
            return None
        else:
            return self._data.insert(index, value)

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def printAll(self):
        for item in self:
            print(item)


def test_pArray() -> None:
    array = PArray(5)
    array.insert(1, 3)
    array.insert(2, 3)
    assert len(array) == 2
    assert array.find(1) == 3


test_pArray()
