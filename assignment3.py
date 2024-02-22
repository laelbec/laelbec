import doctest
FIRST_PURCHASE = 10
FREQUENT_BUYER = 2
SHIPPING_RATE = .10
def get_biggest(int1: int, int2: int, int3: int) -> int:
    """returns biggest of three given values
    >>> get_biggest(0, 0, 0)
    0
    >>> get_biggest(0, 0, 1)
    1
    >>> get_biggest(0, 1, 0)
    1
    >>> get_biggest(1, 0, 0)
    1
    >>> get_biggest(1, 1, 0)
    1
    >>> get_biggest(1, 0, 1)
    1
    >>> get_biggest(0, 1, 1)
    1
    >>> get_biggest(1, 2, 3)
    3
    >>> get_biggest(1, 3, 2)
    3
    >>> get_biggest(3, 2, 1)
    3
    """
    if int1 >= int2 and int1 >= int3:
        return int1
    elif int2 >= int1 and int2 >= int3:
        return int2
    else:
        return int3
    
def get_smallest(int1: int, int2: int, int3: int) -> int:
    """returns smallest of three given values
    >>> get_smallest(0, 0, 0)
    0
    >>> get_smallest(0, 0, 1)
    0
    >>> get_smallest(0, 1, 0)
    0
    >>> get_smallest(1, 0, 0)
    0
    >>> get_smallest(1, 1, 0)
    0
    >>> get_smallest(1, 0, 1)
    0
    >>> get_smallest(0, 1, 1)
    0
    >>> get_smallest(1, 2, 3)
    1
    >>> get_smallest(2, 1, 3)
    1
    >>> get_smallest(3, 2, 1)
    1
    """
    if int1 <= int2 and int1<= int3:
        return int1
    elif int2 <= int1 and int2 <= int3:
        return int2
    else:
        return int3
    
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
    
def is_biggest_multiple_of_smallest(n1: int, n2:int, n3:int) -> bool:
    """determines whether the biggest of the three values is a multiple of
    the smallest of the three values
    >>> is_biggest_multiple_of_smallest(0, 0, 0)
    True
    >>> is_biggest_multiple_of_smallest(9, 3, 4)
    True
    >>> is_biggest_multiple_of_smallest(3, 9, 4)
    True
    >>> is_biggest_multiple_of_smallest(4, 3, 9)
    True
    >>> is_biggest_multiple_of_smallest(9, 3, 2)
    False
    >>> is_biggest_multiple_of_smallest(3, 9, 2)
    False
    >>> is_biggest_multiple_of_smallest(3, 2, 9)
    False
    """
    biggest = get_biggest(n1, n2, n3)
    smallest = get_smallest(n1, n2, n3)
    biggest_multiple_of_smallest = is_multiple_of (biggest, smallest)
    return biggest_multiple_of_smallest
    
    
def get_discount(discount: str, membership: bool) -> int:
    """returns the amount of the discount to be applied
    >>> get_discount('FIRST_PURCHASE', True)
    10
    >>> get_discount('FIRST_PURCHASE', False)
    10
    >>> get_discount('FREQUENT_BUYER', True)
    2
    >>> get_discount('FREQUENT_BUYER', False)
    0
    >>> get_discount('NO_DISCOUNT', True)
    0
    >>> get_discount('NO_DISCOUNT', False)
    0
    >>> get_discount('invalid', True)
    0
    >>> get_discount('invalid', False)
    0
    """
    if discount == 'FIRST_PURCHASE':
        discount_to_be = FIRST_PURCHASE
    elif discount == 'FREQUENT_BUYER' and membership == True:
        discount_to_be = FREQUENT_BUYER
    else:
        discount_to_be = 0
    return discount_to_be
    
def get_discounted_price(discount: str, price: float, membership: bool)->float:
    """determines discount amount and calculates and returns the new price
    Precondition: price >= 0
    >>> get_discounted_price('FIRST_PURCHASE', 20, True)
    10
    >>> get_discounted_price('FIRST_PURCHASE', 20, False)
    10
    >>> get_discounted_price('FIRST_PURCHASE', 0, True)
    0
    >>> get_discounted_price('FIRST_PURCHASE', 0, False)
    0
    >>> get_discounted_price('FREQUENT_BUYER', 20, True)
    18
    >>> get_discounted_price('FREQUENT_BUYER', 20, False)
    20
    >>> get_discounted_price('FREQUENT_BUYER', 0, True)
    0
    >>> get_discounted_price('FREQUENT_BUYER', 0, False)
    0
    >>> get_discounted_price('NO_DISCOUNT', 20, True)
    20
    >>> get_discounted_price('NO_DISCOUNT', 20, False)
    20
    >>> get_discounted_price('invalid', 20, True)
    20
    >>> get_discounted_price('invalid', 20, False)
    20
    """
    discount_value = get_discount(discount, membership)
    discounted_price = price - discount_value
    if discounted_price < 0:
        discounted_price = 0
    return discounted_price

def get_shipping(membership: bool, country: str, price: float) -> float:
    """determines and returns the shipping charge
    Precondition: price >= 0
    >>> get_shipping(True, 'Canada', 20)
    0.0
    >>> get_shipping(True, 'Mexico', 20)
    0.0
    >>> get_shipping(False, 'Canada', 20)
    0.0
    >>> get_shipping(False, 'Mexico', 20)
    2.0
    """
    if membership == True or country == 'Canada':
        shipping = 0.0
    else:
        shipping = price * SHIPPING_RATE
    return shipping
    
def display_charges(price: float, tax: float, membership: bool, discount: str,
                    country: str)-> None:
    """calculates and prints the final bill for an onine shipping site
    calculates the final bill for an online shipping site
    Precondition: numeric values are positive
    >>> display_charges(22.0, 8, False, 'FIRST_PURCHASE', 'Mexico')
    price: $ 12.00
    tax: $ 0.96
    shipping: $ 2.20
    total charge: $ 15.16
    >>> display_charges(10, 5, True, 'FREQUENT_BUYER', 'Mexico')
    price: $ 8.00
    tax: $ 0.40
    shipping: $ 0.00
    total charge: $ 8.40
    >>> display_charges(10, 5, False, 'FREQUENT_BUYER', 'Mexico')
    price: $ 10.00
    tax: $ 0.50
    shipping: $ 1.00
    total charge: $ 11.50
    >>> display_charges(10, 5, True, 'FIRST_PURCHASE', 'Mexico')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    >>> display_charges(15, 5, True, 'FIRST_PURCHASE', 'Mexico')
    price: $ 5.00
    tax: $ 0.25
    shipping: $ 0.00
    total charge: $ 5.25
    >>> display_charges(10, 5, False, 'NO_DISCOUNT', 'Canada')
    price: $ 10.00
    tax: $ 0.50
    shipping: $ 0.00
    total charge: $ 10.50
    >>> display_charges(10, 5, False, 'invalid', 'Canada')
    price: $ 10.00
    tax: $ 0.50
    shipping: $ 0.00
    total charge: $ 10.50
    >>> display_charges(5, 5, False, 'FIRST_PURCHASE', 'Mexico')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.50
    total charge: $ 0.50
    >>> display_charges(0, 5, False, 'FIRST_PURCHASE', 'Mexico')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    """
    final_price = get_discounted_price(discount, price, membership)
    tax_on_purchase = final_price * (tax/100)
    shipping = get_shipping(membership, country, price)
    total_charge = final_price + tax_on_purchase + shipping
    print(f'price: $ {final_price:.2f}')
    print(f'tax: $ {tax_on_purchase:.2f}')
    print(f'shipping: $ {shipping:.2f}')
    print(f'total charge: $ {total_charge:.2f}')