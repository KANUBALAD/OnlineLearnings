import cProfile

def linear_search(list_num, target_val):
    """
    Perform a linear search on a list to find the index of the target value.

    Parameters:
    list_num (list): A list of elements.
    target_val (any): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.

    Examples:
    >>> linear_search([1,4, 5, 6, 2, 9, 3, 7, 8,  10], 3)
    6
    >>> linear_search([5, 2, 4, 3, 1], 6)
    -1
    >>> linear_search([], 1)
    -1
    """
    for index_num, num in enumerate(list_num):
        if num ==target_val:
            return index_num
       
    return -1
  
if __name__ == "__main__":
    import doctest
    doctest.testmod()


