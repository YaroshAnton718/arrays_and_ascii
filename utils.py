def first_arr():
    """
    Calculates the elements of the first array according the formula: 74 - i

    Returns:
        list[int]: list of 10 numbers, formed by the formula (74 - i)
    """
    first_array = []
    for i in range(10):
        a = 74 - i
        first_array.append(a)

    return first_array

def second_arr():
    """
    Calculates the elements of the second array according the formula: 65 + 2 * i

    Returns:
        list[int]: list of 10 numbers, formed by the formula (65 + 2 * i)
    """
    second_array = []
    for i in range(10):
        a = 65 + 2 * i
        second_array.append(a)

    return second_array

def third_arr():
    """
    Unites the elements of first and second arrays.
    Removes the elements, that are more or equal 67.

    Returns:
        list[int]: list of numbers, that are less 67
    """
    third_array = first_arr() + second_arr()

    i = 0
    while i < len(third_array):
        if third_array[i] >= 67:
            third_array.pop(i)
            i -= 1
        i += 1

    return third_array

def ascii_to_symbol():
    """
    Translates the elements of third array into symbols by ASCII codes.

    Returns:
        str: a string formed by ASCII codes of the third array elements
    """
    return ''.join(chr(i) for i in third_arr())