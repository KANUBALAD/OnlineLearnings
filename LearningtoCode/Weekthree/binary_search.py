import cProfile


def binary_search(list_num, target_val):
    """
    Perform a binary search on a sorted list to find the index of the target value.

    Parameters:
    list_num (list[int]): A sorted list of integers.
    target_val (int): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.

    Examples:
    >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    2
    >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
    0
    >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    9
    >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)
    -1
    >>> binary_search([], 1)
    -1
    """
    left_side_list = 0
    right_side_list = len(list_num) - 1
    
    while left_side_list <= right_side_list:
        mid = (left_side_list + right_side_list) // 2
        if list_num[mid] < target_val:
            left_side_list = mid + 1
        elif list_num[mid] > target_val:
            right_side_list = mid - 1
        else:
            return mid
    return -1
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    
    
    