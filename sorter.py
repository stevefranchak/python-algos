"""Implementation of various array sorting algorithms"""

def bubble_sort(array):
    """My bubble sort implementation"""
    swapped = True
    while swapped:
        swapped = False
        for idx in range(len(array) - 1):
            if array[idx] > array[idx + 1]:
                swapped = True
                array[idx + 1], array[idx] = array[idx], array[idx + 1]
    return array

def selection_sort(array):
    """My selection sort implementation"""
    for idx in range(len(array) - 1):
        lowest_idx = idx
        for search_idx in range(idx + 1, len(array)):
            if array[search_idx] < array[lowest_idx]:
                lowest_idx = search_idx
        array[lowest_idx], array[idx] = array[idx], array[lowest_idx]
    return array

def insertion_sort(array):
    """My insertion sort implementation"""
    for idx in range(1, len(array)):
        value_to_insert = array[idx]
        for search_idx in reversed(range(idx)):
            if array[search_idx] > value_to_insert:
                array[search_idx + 1] = array[search_idx]
            else:
                search_idx += 1
                break
        # search_idx will never be undefined due to the outer for loop's condition
        # The outer for loop is only entered if len(array) > 1, and thus
        #  range(idx) in the inner for loop will always yield at least 1 element
        # pylint: disable=W0631
        array[search_idx] = value_to_insert
    return array
