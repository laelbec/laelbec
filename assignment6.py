import doctest

def get_powers(num_lst: list[float], power: float) -> list:
    """returns a new list with all elements of given list raised
    to given power
    >>> get_powers([], 2)
    []
    >>> get_powers([1, 2, 3], 2)
    [1, 4, 9]
    >>> get_powers([-2, 0, 5], 3)
    [-8, 0, 125]
    """
    result=[]
    for num in num_lst:
        raised = (num)**power
        result.append(raised)
    return result

def concatenate(str_lst: list[str]) -> str:
    """returns a single string containing all values from given list
    seperated by a single space
    >>> concatenate([])
    ''
    >>> concatenate(['good', 'bye'])
    'good bye'
    >>> concatenate(['what', 'is', 'up?'])
    'what is up?'
    """
    result = ''
    num_strings = 0
    for string in str_lst:
        result += string
        num_strings += 1
        if num_strings < len(str_lst):
            result += ' '
    return result

def contains_multiple(int_lst: list[int], num) -> bool:
    """determines if an element from given list is a multiple of given num
    >>> contains_multiple([], 2)
    False
    >>> contains_multiple([0, 12, 23, 31], 5)
    True
    >>> contains_multiple([1, 4, 7, 9, 14], 3)
    True
    >>> contains_multiple([1, 3, 5], 2)
    False
    """
    num_elements = len(int_lst)
    index = 0
    while index < num_elements and is_multiple_of(int_lst[index], num) == False:
        index+=1
    return index != num_elements


def is_multiple_of(n1: int, n2: int) -> bool:
    """determines and returns whether or not n1 is a multiple of n2
    >>> is_multiple_of(9, 3)
    True
    >>> is_multiple_of(10, 3)
    False
    >>> is_multiple_of(3, 3)
    True
    >>> is_multiple_of(0, 3)
    True
    >>> is_multiple_of(3, 0)
    False
    >>> is_multiple_of(0, 0)
    True
    """
    if n1 == 0:
        boolean = True
    elif n2 == 0:
        boolean = False
    elif n1 % n2 == 0:
        boolean = True
    else:
        boolean = False
    return boolean

def get_long_enough(str_lst: list[str], threshold: int) -> list:
    """returns a list of all elements from given list that 
    are >= given threshold
    >>> get_long_enough([''], 2)
    []
    >>> get_long_enough(['a', 'ab', 'abc', 'abcde'], 3)
    ['abc', 'abcde']
    """
    result = []
    for string in str_lst:
        if len(string) >= threshold:
            result.append(string)
    return result

def all_multiples(int_lst: list[int], num: int) -> bool:
    """determines whether all elements of the list are multiples of given num
    >>> all_multiples([], 2)
    True
    >>> all_multiples([0, 0, 0, 0], 0)
    True
    >>> all_multiples([1, 2, 0, 5], 0)
    False
    >>> all_multiples([1, 2, 3, 4], 2)
    False
    >>> all_multiples([3, 6, 9, 12], 3)
    True
    """
    length = len(int_lst)
    position = 0
    if int_lst == []:
        return True
    elif num != 0:
        for values in int_lst:
            if values % num == 0:
                position+=1
        return position ==length        
    else:
        while position < length and int_lst[position] == num:
            position+=1
        return position == length


def getting_shorter(str_lst: list[str]) -> bool:
    """determines whether the elements are in order of strictly 
    decreasing lengths
    >>> getting_shorter([])
    True
    >>> getting_shorter(['hello', 'hey', 'h'])
    True
    >>> getting_shorter(['h', 'hello', 'hey'])
    False
    
    """
    if str_lst == []:
        return True
    num_elements = len(str_lst)
    index = 1
    prev = len(str_lst[0])
    
    while (index < num_elements and prev > len(str_lst[index])):
        prev = len(str_lst[index])
        index += 1
    return index == num_elements
        