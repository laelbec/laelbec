import doctest
IN_MI = 63360
IN_YD = 36
IN_FT = 12
FIRST_PURCHASE = 10
FREQUENT_BUYER = 2

def check_funds(balance: float, purchase: float):
    """prints if any credit card balance after a purchase
    Precondition: purchase is not negative
    >>> check_funds(20, 10)
    you will have $10.00 left after this purchase
    >>> check_funds(-10, 20)
    you have a negative balance
    >>> check_funds(10, 20)
    you are short $10.00
    """
    if balance < 0:
        print('you have a negative balance')
    elif balance >= purchase:
        remain = balance - purchase
        print(f'you will have ${remain:.2f} left after this purchase')
    else:
        short = balance - purchase
        print(f'you are short ${abs(short):.2f}')

def print_biggest(num1: float, num2: float, num3: float):
    """prints the largest of three given numbers
    >>> print_biggest(1, 2, 3)
    3
    >>> print_biggest(3, 2, 1)
    3
    >>> print_biggest(1, 3, 2)
    3
    >>> print_biggest(1, 1, 2)
    2
    >>> print_biggest(1, 2, 1)
    2
    >>> print_biggest(2, 1, 1)
    2
    >>> print_biggest(1, 1, 1)
    1
    """
    if num1>=num2 and num1>=num3:
        print(num1)
    elif num2>=num1 and num2>=num3:
        print(num2)
    else:
        print(num3)
    
def convert_inches(inches: float):
    """converts given inches into miles, yards, and feet, prints in order from
    largest (miles) to smallest (inches)
    >>> convert_inches(63409)
    1 mi, 1 yd, 1 ft, 1 in
    >>> convert_inches(63360)
    1 mi, 0 yd, 0 ft, 0 in
    >>> convert_inches(36)
    0 mi, 1 yd, 0 ft, 0 in
    >>> convert_inches(12)
    0 mi, 0 yd, 1 ft, 0 in
    >>> convert_inches(1)
    0 mi, 0 yd, 0 ft, 1 in
    """
    if inches >= IN_MI:
        mi = inches // IN_MI
    else:
        mi = 0
    mi_remainder = inches % IN_MI
    if mi_remainder >= IN_YD:
        yd = mi_remainder // IN_YD
    else:
        yd = 0
    yd_remainder = mi_remainder % IN_YD
    if yd_remainder >= IN_FT:
        ft = yd_remainder // IN_FT
    else:
        ft = 0
    ft_remainder = yd_remainder % IN_FT
    print(mi, 'mi,', yd, 'yd,', ft, 'ft,', ft_remainder, 'in')
    
def is_multiple_of(n1: int, n2: int):
    """determines if first agrument is a multiple of the second
    >>> is_multiple_of(9, 3)
    9 is a multiple of 3
    >>> is_multiple_of(10, 3)
    10 is not a multiple of 3
    >>> is_multiple_of(3, 3)
    3 is a multiple of 3
    >>> is_multiple_of(0, 3)
    0 is a multiple of 3
    >>> is_multiple_of(3, 0)
    3 is not a multiple of 0
    """
    if n1 == 0:
        print(n1, 'is a multiple of', n2)
    elif n2 == 0:
        print(n1, 'is not a multiple of', n2)
    elif n1 % n2 == 0:
        print(n1, 'is a multiple of', n2)
    else:
        print(n1, 'is not a multiple of', n2)
    
def display_charges(purchase: float, tax_rate: float, membership: bool, 
                    discount: str, country: str):
    """calculates the final bill for an online shipping site
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
    if discount == 'FIRST_PURCHASE':
        final_price = purchase - FIRST_PURCHASE
    elif discount == 'FREQUENT_BUYER' and membership == True:
        final_price = purchase - FREQUENT_BUYER
    else:
        final_price = purchase
    if final_price < 0:
        final_price = 0
    if membership == True or country == 'Canada':
        shipping = 0
    else:
        shipping = purchase * .1
    tax = final_price * (tax_rate/100)
    total_charge = final_price + tax + shipping
    print(f'price: $ {final_price:.2f}')
    print(f'tax: $ {tax:.2f}')
    print(f'shipping: $ {shipping:.2f}')
    print(f'total charge: $ {total_charge:.2f}')