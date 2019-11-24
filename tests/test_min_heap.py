import unittest

from hipster.heap import MinHeap


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


if __name__ == '__main__':
    unittest.main()
