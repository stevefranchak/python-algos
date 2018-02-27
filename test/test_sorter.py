"""Tests for the sorting algorithms implemented in sorter"""

import os
import sys
import pytest
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sorter import bubble_sort, selection_sort, insertion_sort

@pytest.mark.parametrize("func", [
    bubble_sort,
    selection_sort,
    insertion_sort
])
@pytest.mark.parametrize("array_to_sort,expected_sorted_array", [
    ([], []),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([2, 1], [1, 2]),
    ([8, 3, 4, 2], [2, 3, 4, 8]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([65, 11, 92, 14, 8, 777, 21, 11, 786], [8, 11, 11, 14, 21, 65, 92, 777, 786])
])
def test_sorter_functions(func, array_to_sort, expected_sorted_array):
    """Test each sorting algorithm implementation against the same set
    of test parameters"""
    assert func(array_to_sort) == expected_sorted_array
