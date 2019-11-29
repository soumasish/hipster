import unittest

from hipster.max_heap import MaxHeap


class TestMaxHeap(unittest.TestCase):

    def test_push(self):
        max_heap = MaxHeap()
        max_heap.push(13)
        self.assertEqual(len(max_heap), 1)

    def test_peek(self):
        max_heap = MaxHeap()
        max_heap.push(13)
        max_heap.push(17)
        max_heap.push(9)
        self.assertEqual(max_heap.peek(), 17)

    def test_pop(self):
        max_heap = MaxHeap()
        max_heap.push(13)
        max_heap.push(9)
        max_heap.push(17)
        self.assertEqual(max_heap.pop(), 17)

    def test_remove(self):
        max_heap = MaxHeap()
        max_heap.push(13)
        max_heap.push(9)
        max_heap.push(17)
        max_heap.remove(13)
        max_heap.pop()
        self.assertEqual(max_heap.pop(), 9)

    def test_clear(self):
        max_heap = MaxHeap()
        max_heap.push(13)
        max_heap.push(9)
        max_heap.clear()
        self.assertEqual(len(max_heap), 0)

