import doctest

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000
DAY_LST = 0
YEAR_LST = 2
FIRST = 0
ONE_TUP = 1
APPEARENCES = 1
ACTOR = 0
# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR,
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2

# represents a Netflix show as (show type, title, directors, cast, date added)
#  where none of the strings are empty strings
NetflixShow = tuple[str, str, list[str], list[str], Date]
TYPE      = 0
TITLE     = 1
DIRECTORS = 2
CAST      = 3
DATE      = 4

# column numbers of data within input csv file
INPUT_TYPE      = 1
INPUT_TITLE     = 2
INPUT_DIRECTORS = 3
INPUT_CAST      = 4
INPUT_DATE      = 6

def read_file(filename: str) -> list[NetflixShow]:
    """ Reads file at filename into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns

    >>> read_file('0lines_data.csv')
    []
    
    >>> read_file('9lines_data.csv')
    [('Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], \
(2019, 11, 15)), ('Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', \
'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', \
'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], (2018, 9, 6)), \
('Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', \
'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], \
['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', \
'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', \
'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', \
'Nattapong Chartpong'], (2018, 9, 5)), \
('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', \
'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', \
'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', \
'Kathleen Barr'], (2018, 10, 5)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), \
('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29)), \
('Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], \
['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', \
'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', \
'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], (2018, 9, 5)), \
('Movie', 'Long Shot', ['Jacob LaMendola'], [], (2017, 9, 29)), \
('TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], (2018, 10, 12))]
    """
    # TODO: complete this method according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    
    lo_netflix = []
    file_handle = open(filename, 'r')
    header = file_handle.readline()
    line = file_handle.readline()
    
    while line != '':
        line_list = line.split(',')
        show_tup = create_show(line_list[INPUT_TYPE], line_list[INPUT_TITLE], \
                               line_list[INPUT_DIRECTORS], \
                               line_list[INPUT_CAST], line_list[INPUT_DATE])
        lo_netflix.append(show_tup)
        line = file_handle.readline()
    
    file_handle.close()
    
    return lo_netflix


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
    year = START_YEAR + int(date_list[YEAR_LST])
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
                date: str )-> NetflixShow:
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

def get_oldest_titles(show_data: list[NetflixShow]) -> list[str]:
    """ Returns a list of the titles of NetflixShows in show_data
    with the oldest added date

    >>> shows_unique_dates = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett',\
    'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> shows_duplicate_oldest_date = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina',\
    'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2017, 9, 29)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> get_oldest_titles([])
    []
    >>> get_oldest_titles(shows_unique_dates)
    ['Out of Thin Air']
    >>> get_oldest_titles(shows_duplicate_oldest_date)
    ['Super Monsters Save Halloween', 'Out of Thin Air']
    """
    # TODO: complete this function according to the documentation
    
    if show_data == []:
        return []
    
    lo_dates = []
    for tup in show_data:
        date = tup[DATE]
        lo_dates.append(date)
        
    oldest = oldest_date(lo_dates)
    
    oldest_titles = []
    for tup in show_data:
        if tup[DATE] == oldest:
            oldest_titles.append(tup[TITLE])
    return oldest_titles
    
def oldest_date(lo_date: list[Date]) -> Date:
    """returns the oldest Date from given list
    Precondition: lo_date != []
    >>> dates = [(2004, 10, 20)]
    >>> oldest_date(dates)
    (2004, 10, 20)
    
    >>> dates = [(2019, 4, 5), (2017, 9, 2), (2009, 4, 8), (2022, 3, 9)]
    >>> oldest_date(dates)
    (2009, 4, 8)
    
    >>> dates = [(2019, 4, 5), (2017, 9, 2), (2009, 4, 8), (2009, 3, 9)]
    >>> oldest_date(dates)
    (2009, 3, 9)
    
    >>> dates = [(2019, 4, 5), (2017, 9, 2), (2009, 4, 8), (2009, 4, 9)]
    >>> oldest_date(dates)
    (2009, 4, 8)
    
    >>> dates = [(2019, 4, 5), (2017, 9, 2), (2009, 4, 8), (2009, 4, 8)]
    >>> oldest_date(dates)
    (2009, 4, 8)
    """
    num_elements = len(lo_date)
    if num_elements == ONE_TUP:
        return lo_date[FIRST]
    
    smallest = lo_date[FIRST]
    for index in range(1, num_elements):
        compare = lo_date[index]
        if compare[YEAR] < smallest[YEAR]:
            smallest = compare
        elif (compare[YEAR] == smallest[YEAR] and 
              compare[MONTH] < smallest[MONTH]):
            smallest = compare
        elif (compare[YEAR] == smallest[YEAR] and compare[MONTH] == 
        smallest[MONTH] and compare[DAY] < smallest[DAY]):
            smallest = compare
        else:
            smallest = smallest
            
    return smallest

def get_actors_in_most_shows(shows: list[NetflixShow]) -> list[str]:
    """ Returns a sorted list of actors that are in the casts of the most shows

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]

    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]
    
    >>> empty_actors = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], [], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], [], (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], [], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], [], (2019, 12, 31))]

    >>> get_actors_in_most_shows([])
    []

    >>> get_actors_in_most_shows(l_unique_casts) # doctest: +NORMALIZE_WHITESPACE
    ['Emma Stone', 'Hugh Bonneville', 'Lily Travers', 'Michael Cera', \
    'Om Puri', 'Paresh Rawal']

    >>> get_actors_in_most_shows(one_actor_in_multiple_casts)
    ['Jonah Hill']

    >>> get_actors_in_most_shows(actors_in_multiple_casts)
    ['Jonah Hill', 'Om Puri']
    
    >>> get_actors_in_most_shows(empty_actors)
    []
    """
    # TODO: complete this function according to the documentation
    if shows == []:
        return []
    
    lo_actors = []
    for tup in shows:
        actors = tup[CAST]
        for name in actors:
            if name not in lo_actors:
                lo_actors.append(name)
    
    if lo_actors == []:
        return []
    
    lo_appearences = []
    for actor in lo_actors:
        appearences = 0
        for tup in shows:
            if actor in tup[CAST]:
                appearences += 1
        appearences_tup = (actor, appearences)
        lo_appearences.append(appearences_tup)
    
    lo_occurances = []
    for tup in lo_appearences:
        lo_occurances.append(tup[APPEARENCES])
    
    max_occurance = max(lo_occurances)
    
    most_appearences = []
    for tup in lo_appearences:
        if tup[APPEARENCES] == max_occurance:
            most_appearences.append(tup[ACTOR])
    most_appearences.sort()
    return most_appearences

def get_shows_with_search_terms(show_data: list[NetflixShow], terms: list[str]
                                 ) -> list[NetflixShow]:
    """ returns a list of only those NetflixShow elements in show_data
    that contain any of the given terms in the title.
    If terms is empty, all elements in show_data will be included in the returned list.
    Matching of terms ignores case ('roAD' is found in 'Road to Sangam') and
    matches on substrings ('Sang' is found in 'Road to Sangam')

    Precondition: the strings in terms are not empty strings

    >>> movies = [\
    ('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
     ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor',  \
      'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', \
      'Anupam Kher', 'Madhavan'],  \
     (2018, 8, 2)),\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],  \
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',  \
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',  \
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'],  \
     (2017, 12, 12)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]

    >>> terms1 = ['House']
    >>> terms1_wrong_case = ['hoUSe']

    >>> terms_subword = ['Sang']

    >>> terms2 = ['House', 'Road', 'Basanti']
    >>> terms2_wrong_case = ['house', 'ROAD', 'bAsanti']

    >>> get_shows_with_search_terms([], [])
    []

    >>> get_shows_with_search_terms(movies, []) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor',  \
       'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', \
       'Anupam Kher', 'Madhavan'],  \
      (2018, 8, 2)),\
     ('Movie', "Viceroy's House", ['Gurinder Chadha'],  \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',  \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',  \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'],  \
      (2017, 12, 12)),\
     ('Movie', 'Road to Sangam', ['Amit Rai'], \
       ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
        'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
       (2019, 12, 31))]
    >>> get_shows_with_search_terms([], terms1)
    []

    >>> get_shows_with_search_terms(movies, terms1) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], 
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms1_wrong_case) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms_subword) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', \
       'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', \
       'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], 
      (2018, 8, 2)), \
     ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
        'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
        'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
       (2017, 12, 12)), \
      ('Movie', 'Road to Sangam', ['Amit Rai'], \
       ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
        'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
       (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2_wrong_case) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', \
       'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', \
       'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], \
      (2018, 8, 2)), \
     ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12)), \
     ('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]
    """
    # TODO: complete this function according to the documentation
    if show_data == []:
        return []
    elif terms == []:
        return show_data
    
    lo_titles = []
    for tup in show_data:
        title = tup[TITLE]
        lo_titles.append(title)
    
    lowered_terms = []
    for term in terms:
        lowered_terms.append(term.lower())
    
    title_to_found = {}
    for title in lo_titles:
        title_to_found[title] = 0
    
    for title in title_to_found:
        for term in lowered_terms:
            if term in title.lower():
                title_to_found[title] += 1
    
    found = []
    for title in title_to_found:
        if title_to_found[title] > 0:
            found.append(title)
    
    found_tup = []
    for tup in show_data:
        for title in found:
            if tup[TITLE] == title:
                found_tup.append(tup)
    
    return found_tup

def query(show_data: list[NetflixShow]) -> list[str]:
    """
    Returns a sorted list of only the show titles from show_data
    that are acted in by the 'most popular' actors
    where the 'most popular' is defined as the actors in the most shows.

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]
    
    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]
    
    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]
    
    >>> empty_actors = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], [], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], [], (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], [], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], [], (2019, 12, 31))]
    
    >>> query([])
    []
    
    >>> query(l_unique_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    
    >>> query(one_actor_in_multiple_casts)
    ['Maniac', 'Superbad']

    >>> query(actors_in_multiple_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    
    >>> query(empty_actors)
    []
    """
    # TODO: complete this function according to the documentation
    popular_actors = get_actors_in_most_shows(show_data)
    lo_titles = []
    for actor in popular_actors:
        for tup in show_data:
            if actor in tup[CAST] and tup[TITLE] not in lo_titles:
                lo_titles.append(tup[TITLE])
    lo_titles.sort()
    return lo_titles