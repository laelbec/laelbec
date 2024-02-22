import doctest
import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5


def roll_one_die() -> int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    # this line MUST be uncommented when submitting to PrairieLearn
    #die = random.randint(MIN_ROLL, MAX_ROLL)

    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # this line MUST be commented out when submitting to PrairieLearn
    die = int(input('enter a simulated dice roll\n'))

    return die


def get_sequence(start: int, inc: int, maximum: int) -> str:
    """returns a string with the elements of an arithmetic sequence
    based on given integers
    """
    sequence = ''
    current_value = start
    
    while current_value <= maximum:
        sequence += str(current_value)
        current_value += inc
        if current_value <= maximum:
            sequence += ','
    return sequence
        
def digit_sum(n: int) -> int:
    """returns the sum of each digit in given integer
    """
    total=0
    n_abs = abs(n)
    while n_abs //10 != 0:
        add = n_abs%10
        n_abs = n_abs //10
        total+= add
    if n_abs //10 ==0:
        add = n_abs%10
        total+=add
    return total

def sum_factors(n: int) -> int:
    """returns the sum of all factors of n
    Precondition: n>0
    """
    total = 0
    for count in range(1, n):
        if n % count == 0:
            total += count
    return total

def is_perfect(n: int) -> bool:
    """determines whether or not n is a perfect number
    Precondition: n>0
    """
    factor_sum = sum_factors(n)
    if n == 0:
        boolean = False
    else:
        boolean = factor_sum == n
    return boolean
    
def n_perfect_numbers(n: int) -> str:
    """returns a string containting the first n perfect numbers
    """
    perfect_count  = 1
    num = 1
    string = ''
    if n == 0:
        string = ''
    else:
        while perfect_count <= n:
            if is_perfect(num) == True:
                perfect_count += 1
                string += str(num) 
                if perfect_count < (n+1):
                    string += ','
            num += 1
        
    return string

def take_turn(name: str, current_pt: int, round_num: int) -> int:
    """repeatedly simulates the roll of three dice, calculates the roll
    score and adds the roll score to the players current point. The function
    will continue to do this until the player has a roll score that is worth 0
    or the player has accrued at least 21 total points. Returns updated points
    """
    print('Player', name, 'is taking a turn in round', round_num)
    print('Three dice rolled: ', end='')
    die_1 = roll_one_die()
    print(die_1, end=', ')
    die_2 = roll_one_die()
    print(die_2, end=', ')
    die_3 = roll_one_die()
    print(die_3)
    if die_1 == round_num and die_2 == round_num and die_3 == round_num:
        scored = 21
    elif die_1 == die_2 and die_1 == die_3:
        scored = 5
    elif die_1 == round_num and die_2 != round_num and die_3 != round_num:
        scored = 1
    elif die_2 == round_num and die_1 != round_num and die_3!= round_num:
        scored = 1
    elif die_3 == round_num and die_1 != round_num and die_2 != round_num:
        scored = 1
    elif die_1 == round_num and die_2 == round_num or die_3 == round_num:
        scored = 2
    else:
        scored = 0
    
    if scored == 1:
        score_str = 'point'
    else:
        score_str = 'points'
    print('scored:', scored, score_str)
    
    current_pt += scored
    print('Total points:', current_pt)

    while current_pt<21 and scored != 0:
        print('Three dice rolled: ', end='')
        die_1 = roll_one_die()
        print(die_1, end=', ')
        die_2 = roll_one_die()
        print(die_2, end=', ')
        die_3 = roll_one_die()
        print(die_3)
        if die_1 == round_num and die_2 == round_num and die_3 == round_num:
            scored = 21
        elif die_1 == die_2 and die_1 == die_3:
            scored = 5
        elif die_1 == round_num and die_2 != round_num and die_3 != round_num:
            scored = 1
        elif die_2 == round_num and die_1 != round_num and die_3!= round_num:
            scored = 1
        elif die_3 == round_num and die_1 != round_num and die_2 != round_num:
            scored = 1
        elif die_1 == round_num and die_2 == round_num or die_3 == round_num:
            scored = 2
        else:
            scored = 0
        
        if scored == 1:
            score_str = 'point'
        else:
            score_str = 'points'
        print('scored:', scored, score_str)
        
        current_pt += scored
        print('Total points:', current_pt)
        
    return current_pt

def play_round(p1: int, p2: int, round_num: int) -> str:
    """simulates a round of the game alternating turns starting with p1 until
    either p1 or pt reaches 21 points
    Precondition: round_num is between 1 and 6 inclusive
    """
    p2_pt = 0
    p1_pt = take_turn(p1, 0, round_num)
    if p1_pt<21:
        p2_pt = take_turn(p2, 0, round_num)
    if p2_pt<21: 
        while p1_pt < 21 and p2_pt < 21:
            p1_pt = take_turn(p1, p1_pt, round_num)
            if p1_pt < 21:
                p2_pt = take_turn(p2, p2_pt, round_num)
    if p1_pt < p2_pt:
        winner = p2
    else: 
        winner = p1
    print('the winner of this round is:', winner)
    print(p1, 'has', p1_pt, 'points and', p2, 'has', p2_pt, 'points')
    return winner
    