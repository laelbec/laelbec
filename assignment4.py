import doctest

def get_factors(n: int) -> str:
    """returns a string containing all factors of n from smallest to biggest
    Precondition: n>0
    >>> get_factors(20)
    '1,2,4,5,10,20'
    >>> get_factors(12)
    '1,2,3,4,6,12'
    """
    total=''
    for count in range(1, n+1):
        factors = n % count
        if factors == 0:
            total+= str(count)
            if count< n:
                total+=','
    return total

def get_range_of_factors(start: int, end: int) -> str:
    """returns a string containing rows with the factors from start to 
    end not inclusive
    Precondition: n>0
    >>> get_range_of_factors(10, 13)
    '1,2,5,10\\n1,11\\n1,2,3,4,6,12\\n'
    >>> get_range_of_factors(6,13)
    '1,2,3,6\\n1,7\\n1,2,4,8\\n1,3,9\\n1,2,5,10\\n1,11\\n1,2,3,4,6,12\\n'
    """
    total=''
    for count in range(start, end):
        factors = get_factors(count)
        total += factors + str('\n')  
    return total

def sum_fibonacci_sequence(n: int) -> int:
    """returns the sum of the first n values in the Fibonacci sequence
    Precondition: n>0
    >>> sum_fibonacci_sequence(0)
    0
    >>> sum_fibonacci_sequence(1)
    0
    >>> sum_fibonacci_sequence(2)
    1
    >>> sum_fibonacci_sequence(7)
    20
    """
    if n == 0 or n == 1:
        return 0
    else:
        previous = 0
        current = 1
        fib_sequence = 1
        for count in range(0, n-2):
            total = current + previous
            fib_sequence += total
            previous = current
            current = total
        return fib_sequence
    
def print_tail(n: int) -> None:
    start = '// '
    end = ' \\\\'
    mid = ' /\\ ' * n
    tail = start + mid + end
    print(tail)
    
def print_booster(n: int) -> None:
    for row in range(n):
        dot_num = n - row
        dot = '.' * dot_num
        hat = '/\\' + '/\\'*row
        top_pattern = 2 *(dot+hat+dot)
        print('|'+top_pattern+'|')
    
    base_top = '|/\\/\\' + '/\\/\\' * n +'|'
    print(base_top)
    
    base_bottom = '|\\/\\/' +'\\/\\/'*n + '|'
    print(base_bottom)
    
    for row in range(n):
        dot = '.'+'.'*row
        hat_num = n -row
        hat = '\\/' * hat_num
        bottom_pattern = 2 *(dot+hat+dot)
        print('|'+bottom_pattern+'|')
    end = '+=*=*' + '=*' * (2*n) +'+'
    print(end)

def print_instrument_unit(n: int) -> None:
    first = '||~#' + '~#' * (2*n) + '||'
    last = '+=*=*' + '=*' * (2*n) +'+'
    print(first)
    print(first)
    print(last)
    
def print_lem_adapter(n: int) -> None:
    first = ' //' + ' %' * (2*n) + '\\\\'
    second = '// %' + ' %' * (2*n) + '\\\\'
    last = '+=*=*' + '=*' * (2*n) +'+'
    print(first)
    print(second)
    print(last)
def print_space_craft(n: int) -> None:   
    if n == 0:
        print('  ++')
    else:
        num_slash = 0
        for row in range(2*n, 0, -1):
            start_space =' ' * (row+2)
            fslash = '/' * num_slash
            bslash = '\\'* num_slash
            num_slash+=1
            pattern = start_space+fslash+'**'+bslash
            print(pattern)
        end = '  +' + '=*' * (2*n) +'+'
        print(end)
        
            
def print_rocket_ship(size: int, booster: int) -> None:
    space_craft = print_space_craft(size)
    lem_adapter = print_lem_adapter(size)
    instrument = print_instrument_unit(size)
    for row in range(booster):
        boost = print_booster(size)
    tail = print_tail(size)