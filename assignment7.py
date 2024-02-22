import doctest
#represents a valid date in the calender as y/m/d
Date = tuple[int, int, int]
#represents Netflix show information as show type, title, list of directors,
#list of show actors, and the Date show was added
# all str != ''
NetflixInfo = tuple[str, str, list[str], list[str], Date]
POWER = 1
DAY_LST = 0
MONTH = 1
YEAR_LST = 2
YEAR_TUP = 0
DAY_TUP = 2
YEAR2000 = 2000
SHOW = 1
ACTOR = 3
NETFLIX_DATE = 4

def raise_to_power(list1: list[int], list2: list[int]) -> None:
    """raises every element in first list to the power of value
    at corresponding position in the second list
    >>> list1 = [1, 2, 3]
    >>> list2=[2, 4, 0]
    >>> raise_to_power(list1, list2)
    >>> list1
    [1, 16, 1]
    >>> list2
    [2, 4, 0]
    
    >>> list1 = [1, 2, 3]
    >>> list2=[2, 4]
    >>> raise_to_power(list1, list2)
    >>> list1
    [1, 16, 3]
    >>> list2
    [2, 4]
    
    >>> list1 = [1, 2, 3]
    >>> list2=[2, 4, 0, 2]
    >>> raise_to_power(list1, list2)
    >>> list1
    [1, 16, 1]
    >>> list2
    [2, 4, 0, 2]
    
    >>> list1 = []
    >>> list2=[2, 4, 0]
    >>> raise_to_power(list1, list2)
    >>> list1
    []
    >>> list2
    [2, 4, 0]
    
    >>> list1 = [1, 2, 3]
    >>> list2=[]
    >>> raise_to_power(list1, list2)
    >>> list1
    [1, 2, 3]
    >>> list2
    []
    """
    list1_len = len(list1)
    list2_len = len(list2)
    min_len = min(list1_len, list2_len)
    for index in range(min_len):
        list1[index] **= list2[index]
        if list1_len > min_len:
            list1[index] **= POWER

  
        
def create_date(date: str) -> Date:
    """takes given string and returns a date tuple
    Precondition: date is formatted 'day-month-year' where day is a 2 digit
    int, month is the firth 3 letter of valid month with first letter 
    uppercased, year is a 2 digit int representing a year in the 2000s
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    >>> create_date('14-Feb-16')
    (2016, 2, 14)
    >>> create_date('27-Mar-09')
    (2009, 3, 27)
    >>> create_date('6-Apr-00')
    (2000, 4, 6)
    >>> create_date('2-May-07')
    (2007, 5, 2)
    >>> create_date('21-Jun-20')
    (2020, 6, 21)
    >>> create_date('14-Jul-04')
    (2004, 7, 14)
    >>> create_date('30-Aug-14')
    (2014, 8, 30)
    >>> create_date('24-Sep-04')
    (2004, 9, 24)
    >>> create_date('20-Oct-04')
    (2004, 10, 20)
    >>> create_date('11-Nov-11')
    (2011, 11, 11)
    >>> create_date('24-Dec-19')
    (2019, 12, 24)
    """
    date_list = date.split('-')
    month = month_int(date_list[MONTH])
    year = YEAR2000 + int(date_list[YEAR_LST])
    date_tuple = (year, month, int(date_list[DAY_LST]))
    return date_tuple

def month_int(month: str) -> int:
    """returns the integer version of given month
    Precondition: month is first three letters of month, 
    first letter capitalized
    >>> month_int('Jan')
    1
    >>> month_int('Feb')
    2
    >>> month_int('Mar')
    3
    >>> month_int('Apr')
    4
    >>> month_int('May')
    5
    >>> month_int('Jun')
    6
    >>> month_int('Jul')
    7
    >>> month_int('Aug')
    8
    >>> month_int('Sep')
    9
    >>> month_int('Oct')
    10
    >>> month_int('Nov')
    11
    >>> month_int('Dec')
    12
    """
    if month == 'Jan':
        month_int = 1
    elif month == 'Feb':
        month_int = 2
    elif month == 'Mar':
        month_int = 3
    elif month == 'Apr':
        month_int = 4
    elif month == 'May':
        month_int = 5
    elif month == 'Jun':
        month_int = 6
    elif month == 'Jul':
        month_int = 7
    elif month == 'Aug':
        month_int = 8
    elif month == 'Sep':
        month_int = 9
    elif month == 'Oct':
        month_int = 10
    elif month == 'Nov':
        month_int = 11
    else:
        month_int = 12
    return month_int

def create_show(show_type: str, title: str, directors: str, actors:str,
                date: str )-> NetflixInfo:
    """creates and returns a Netflix show tuple
    >>> create_show('', '', '', '', '23-Sep-16')
    ('', '', [], [], (2016, 9, 23))
    
    >>> create_show('Movie', 'Room on the Broom', 'Max Lang:Jani Lachauer', \
    'Simon Pegg:Gillian Anderson:Rob Brydon:Martin Clunes:Sally Hawkins:David \
    Walliams:Timothy Spall', \
    '1-Jul-19') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Room on the Broom', ['Max Lang', 'Jani Lachauer'], \
    ['Simon Pegg', 'Gillian Anderson', 'Rob Brydon', 'Martin Clunes', \
    'Sally Hawkins', 'David Walliams', 'Timothy Spall'], \
    (2019, 7, 1))
    """
    if directors =='':
        lo_directors = []
    else:
        lo_directors = directors.split(':')
    
    if actors =='':
        lo_actors = []
    else:
        lo_actors = actors.split(':')
    date = create_date(date)

    netflix_info = (show_type, title, lo_directors, lo_actors, date)
    return netflix_info

def get_titles(lo_show: list[NetflixInfo]) -> list[str]:
    """returns a list of the title of shows from the list
    >>> get_titles([])
    []
    >>> loshows = [('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)),('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], (2018, 9, 21)),('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_titles(loshows)
    ["Viceroy's House", 'Superbad', 'Maniac', 'Road to Sangam']
    """
    result = []
    for tup in lo_show:
        result.append(tup[SHOW])
    return result

def is_actor_in_show(netflix_tuple:NetflixInfo, actor: str) -> bool:
    """return True if given actor is in given Netflix show tuple, else False
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), 'Justin Bieber')
    False
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), 'Michael Cera')
    True
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), 'MichaEL cerA')
    True
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), '')
    True
    """
    lo_actors = netflix_tuple[ACTOR]
    lowered_actors = []
    if actor == '':
        return True
    
    for person in lo_actors:
        low_actor = person.lower()
        lowered_actors.append(low_actor)
        
    actor_low = actor.lower()
    return actor_low in lowered_actors
    
def count_shows_before_date(lo_shows: list[NetflixInfo], date: Date) -> int:
    """returns a count of the number of shows added before the given date
    >>> loshows = [('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 2, 6)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],(2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], (2018, 9, 21)),('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2017, 4, 18))]

    >>> count_shows_before_date(loshows, (2015, 1, 1))
    0
    >>> count_shows_before_date(loshows, (2018, 10, 20))
    3
    >>> count_shows_before_date([], (2015, 1, 1))
    0
    """
    before = 0
    for tup in lo_shows:
        date_added = tup[NETFLIX_DATE]
        if date_added[YEAR_TUP] < date[YEAR_TUP]:
            before+=1
        elif (date_added[YEAR_TUP] == date[YEAR_TUP] and 
              date_added[MONTH] < date[MONTH]):
            before+=1
        elif (date_added[YEAR_TUP] == date[YEAR_TUP] and date_added[MONTH] == 
            date[MONTH] and date_added[DAY_TUP] < date[DAY_TUP]):
            before+=1
    return before

def get_shows_with_actor(lo_shows: list[NetflixInfo], 
                         actor: str) -> list[NetflixInfo]:
    """returns a list of only the Netflix show tuples that the given actor
    has acted in
    >>> loshows = [('Movie', "Viceroy's House", ['Gurinder Chadha'], \
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)), ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], (2018, 9, 21)),('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_shows_with_actor(loshows, 'Jonah Hill')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], (2018, 9, 21))]
    
    >>> get_shows_with_actor(loshows, 'jonaH hiLL')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], (2018, 9, 21))]
    
    >>> loshows = [('Movie', "Viceroy's House", ['Gurinder Chadha'], \
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)), ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1))]
    
    >>> get_shows_with_actor(loshows, '')   # doctest: +NORMALIZE_WHITESPACE
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], \
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)), ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1))]
    
    >>> get_shows_with_actor(loshows, 'Justin Bieber')
    []
    """
    result = []
    if actor == '':
        return lo_shows
    for show in lo_shows:
        if is_actor_in_show(show, actor):
            result.append(show)
    return result