import unittest
from functions.heap_sort import sort
from numpy import random


class TestHeapSort(unittest.TestCase):
	def test_0(self):
		arr = random.randint(0, 30, 0)
		arr = sort(arr)
		self.assertTrue(is_sorted(arr))

	def test_1(self):
		arr = sort([5])
		self.assertTrue(is_sorted(arr))

	def test_large(self):
		arr = sort([])
		self.assertTrue(is_sorted(arr))


def is_sorted(arr):
	for i in range(1, len(arr)):
		if arr[i] < arr[i - 1]:
			return False
	return True
