import unittest

from hipster.min_heap import MinHeap


class TestHeap(unittest.TestCase):

    def test_push(self):
        min_heap = MinHeap()
        min_heap.push(12)
        self.assertEqual(len(min_heap), 1)

    def test_peek(self):
        min_heap = MinHeap()
        min_heap.push(15)
        min_heap.push(11)
        self.assertEqual(min_heap.peek(), 11)

    def test_pop(self):
        min_heap = MinHeap()
        min_heap.push(12)
        min_heap.push(15)
        min_heap.push(11)
        self.assertEqual(min_heap.pop(), 11)
        self.assertEqual(min_heap.pop(), 12)
        self.assertEqual(min_heap.pop(), 15)

    def test_remove(self):
        min_heap = MinHeap()
        min_heap.push(13)
        min_heap.push(9)
        min_heap.push(17)
        min_heap.remove(13)
        min_heap.pop()
        self.assertEqual(min_heap.pop(), 17)

    def test_clear(self):
        min_heap = MinHeap()
        min_heap.push(13)
        min_heap.push(9)
        min_heap.clear()
        self.assertEqual(len(min_heap), 0)


if __name__ == '__main__':
    unittest.main()
