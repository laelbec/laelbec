import doctest

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR, 
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2

YEAR_LST = 2
DAY_LST = 0

# column numbers of data within input csv file
INPUT_SID        = 0
INPUT_TITLE      = 2
INPUT_CAST       = 4
INPUT_DATE       = 6
INPUT_CATEGORIES = 10



SHOWID_TO_DATE = 0
SHOWID_TO_UNIQUE = 1
CATEGORY_TO_SHOWID = 2
SHOWID_TO_TITLE = 3

def read_file(filename: str) -> (dict[str, Date],
                                 dict[str, list[str]],
                                 dict[str, list[str]],
                                 dict[str, str]):
    """
    Populates and returns a tuple with the following 4 dictionaries
    with data from valid filename.
    
    4 dictionaries returned as a tuple:
    - dict[show id: date added to Netflix]
    - dict[show id: list of unique actor names]
    - dict[category: list of unique show ids]
    - dict[show id: show title]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show id: list of unique actor names]

    The list of actors for each key in
      dict[show id: list of unique actor names]
      should be in the order they appear on the line in the input file.
      If the line has duplicated actor names, the unique actor name 
      is added once for the first time it occurs in the line.
    
    Precondition: file is csv with data in expected columns 
        and contains a header row with column titles
        Show ids within the file are unique.
        
    >>> read_file('0lines_data.csv')
    ({}, {}, {}, {})
    
    >>> read_file('11lines_data.csv')  # doctest: +NORMALIZE_WHITESPACE
    ({'81217749': (2019, 11, 15),
      '70303496': (2018, 9, 6),
      '70142798': (2018, 9, 5),
      '80999063': (2018, 10, 5),
      '80190843': (2018, 9, 7),
      '80119349': (2017, 9, 29),
      '70062814': (2018, 9, 5),
      '80182115': (2017, 9, 29),
      '80187722': (2018, 10, 12),
      '70213237': (2018, 10, 2),
      '70121522': (2019, 8, 1)},
     {'81217749': ['Naseeruddin Shah'],
      '70303496': ['Aamir Khan',
                   'Anuskha Sharma',
                   'Sanjay Dutt',
                   'Saurabh Shukla',
                   'Parikshat Sahni',
                   'Sushant Singh Rajput',
                   'Boman Irani',
                   'Rukhsar'],
      '70142798': ['Jirayu La-ongmanee',
                   'Charlie Trairat',
                   'Worrawech Danuwong',
                   'Marsha Wattanapanich',
                   'Nicole Theriault',
                   'Chumphorn Thepphithak',
                   'Gacha Plienwithi',
                   'Suteerush Channukool',
                   'Peeratchai Roompol',
                   'Nattapong Chartpong'],
      '80999063': ['Elyse Maloway',
                   'Vincent Tong',
                   'Erin Matthews',
                   'Andrea Libman',
                   'Alessandro Juliani',
                   'Nicole Anthony',
                   'Diana Kaarina',
                   'Ian James Corlett',
                   'Britt McKillip',
                   'Kathleen Barr'],
      '70062814': ['Ananda Everingham',
                   'Natthaweeranuch Thongmee',
                   'Achita Sikamana',
                   'Unnop Chanpaibool',
                   'Titikarn Tongprasearth',
                   'Sivagorn Muttamara',
                   'Chachchaya Chalemphol',
                   'Kachormsak Naruepatr'],
      '80187722': ['Frank Grillo'],
      '70213237': ['Graham Chapman',
                   'Eric Idle',
                   'John Cleese',
                   'Michael Palin',
                   'Terry Gilliam',
                   'Terry Jones'],
      '70121522': ['Aamir Khan',
                   'Kareena Kapoor',
                   'Madhavan',
                   'Sharman Joshi',
                   'Omi Vaidya',
                   'Boman Irani',
                   'Mona Singh',
                   'Javed Jaffrey']},
     {'Documentaries': ['81217749', '80119349', '80182115'],
      'International Movies': ['81217749',
                               '70303496',
                               '70142798',
                               '80119349',
                               '70062814',
                               '70121522'],
      'Comedies': ['70303496', '70121522'],
      'Dramas': ['70303496', '70121522'],
      'Horror Movies': ['70142798', '70062814'],
      'Children & Family Movies': ['80999063'],
      'Docuseries': ['80190843', '80187722', '70213237'],
      'British TV Shows': ['70213237']},
     {'81217749': 'SunGanges',
      '70303496': 'PK',
      '70142798': 'Phobia 2',
      '80999063': 'Super Monsters Save Halloween',
      '80190843': 'First and Last',
      '80119349': 'Out of Thin Air',
      '70062814': 'Shutter',
      '80182115': 'Long Shot',
      '80187722': 'FIGHTWORLD',
      '70213237': "Monty Python's Almost the Truth",
      '70121522': '3 Idiots'})
    """
    # TODO: complete this function according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    
    file_handle = open(filename, 'r')
    header = file_handle.readline()
    showid_to_date = {}
    showid_to_unique = {}
    category_to_showid = {}
    showid_to_title = {}
    
    for line in file_handle:
        line = line.split(',')
        date = create_date(line[INPUT_DATE])
        cast = get_unique_cast(line[INPUT_CAST])
        category = line[INPUT_CATEGORIES]
        category_lst = category.split(':')
        showid = line[INPUT_SID]
        showid_to_date[line[INPUT_SID]] = date
        if cast != ['']:
            showid_to_unique[line[INPUT_SID]] = cast
        for category in category_lst:
            if category not in category_to_showid:
                category_to_showid[category]=[showid]
            else:
                category_to_showid[category].append(showid)     
        showid_to_title[line[INPUT_SID]] = line[INPUT_TITLE]
            
    file_handle.close()
    dict_tuple = (showid_to_date, showid_to_unique, category_to_showid,\
                  showid_to_title)
    return dict_tuple

def get_unique_cast(cast: str) -> list[str]:
    """returns a list of unique actors from given string in where actors are 
    seperated by a colon
    >>> get_unique_cast('')
    ['']
    >>> get_unique_cast('Aamir Khan')
    ['Aamir Khan']
    >>> get_unique_cast('Aamir Khan:Anuskha Sharma:Sanjay Dutt:Saurabh Shukla:\
Parikshat Sahni:Sushant Singh Rajput:Boman Irani:Rukhsar')
    ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', \
'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar']
    >>> get_unique_cast('Aamir Khan:Anuskha Sharma:Sanjay Dutt:Saurabh Shukla:\
Parikshat Sahni:Sushant Singh Rajput:Boman Irani:Rukhsar:Rukhsar')
    ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', \
'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar']
    """
    cast_list = cast.split(':')
    unique_cast = []
    for name in cast_list:
        if name not in unique_cast:
            unique_cast.append(name)
    return unique_cast

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

def query(filename: str, category: str, date: Date, actors: list[str]
          ) -> list[tuple[str, str]]:
    """
    returns a list of sorted tuples containing (show title, show id) pairs 
    of only those shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
    - were added to Netflix before the given date
    
    Precondition: category and actor names must match case exactly. 
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'
    
    You MUST call read_file and use look ups in the returned dictionaries 
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.
    
    >>> query('0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    [('3 Idiots', '70121522'), ('PK', '70303496')]

    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    [('3 Idiots', '70121522'), ('PK', '70303496')]
        
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Sanjay Dutt'])
    [('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('3 Idiots', '70121522'), ('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 8, 1), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'not found', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'Aamir Khan', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either', 'Aamir Khan']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('large_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('PK', '70303496')]
    
    >>> query('large_data.csv', 'Comedies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'),
     ('PK', '70303496'), ('Zed Plus', '81213884')]
    
    >>> query('large_data.csv', 'International Movies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'), 
     ('Dangal', '80166185'), ('Dhobi Ghat (Mumbai Diaries)', '70144331'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'), 
     ('Lagaan', '60020906'), ('Madness in the Desert', '80229953'),
     ('PK', '70303496'), ('Raja Hindustani', '17457962'), 
     ('Rang De Basanti', '70047320'), ('Secret Superstar', '80245408'), 
     ('Shutter', '70062814'), ('Taare Zameen Par', '70087087'),
     ('Talaash', '70262614'), ('Zed Plus', '81213884')]
    """
    # TODO: complete this function according to the documentation
    tuple_dict = read_file(filename)
    showid_to_date = tuple_dict[SHOWID_TO_DATE]
    showid_to_unique = tuple_dict[SHOWID_TO_UNIQUE]
    category_to_showid = tuple_dict[CATEGORY_TO_SHOWID]
    showid_to_title = tuple_dict[SHOWID_TO_TITLE]

    lo_tup = []
    for key in showid_to_title:
        older = is_older(showid_to_date[key], date)
        if key in showid_to_unique:
            cast = showid_to_unique[key]
        else:
            cast = []
        include_actor = actor_in(cast, actors)
        
        if category not in category_to_showid:
            return lo_tup
        
        if (older and include_actor and key in category_to_showid[
            category]):
            title = showid_to_title[key]
            tup = (title, key)
            lo_tup.append(tup)
        
    lo_tup.sort()
    return lo_tup
    
    
def is_older(date: Date, threshold: Date) -> bool:
    """determines if date is older than given threshold
    >>> is_older((2004, 10, 20), (2015, 5, 6))
    True
    >>> is_older((2015, 10, 20), (2015, 11, 1))
    True
    >>> is_older((2015, 10, 2), (2015, 10, 10))
    True
    >>> is_older((2015, 10, 10), (2015, 10, 10))
    False
    >>> is_older((2015, 5, 6), (2004, 10, 20))
    False
    >>> is_older((2015, 11, 1), (2015, 10, 20))
    False
    >>> is_older((2015, 10, 20), (2015, 10, 10))
    False
    """
    for values in date:
        if date[YEAR] < threshold[YEAR]:
            return True
        elif (date[YEAR] == threshold[YEAR] and 
              date[MONTH] < threshold[MONTH]):
            return True
        elif (date[YEAR] == threshold[YEAR] and date[MONTH] == 
            threshold[MONTH] and date[DAY] < threshold[DAY]):
            return True
        else:
            return False
        
def actor_in(cast: list[str], actors: list[str]) -> bool:
    """determines if any actors from list actors is in cast list
    >>> actor_in([], [])
    True
    >>> cast = ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', \
    'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', \
    'Boman Irani', 'Rukhsar'] 
    >>> actor_in(cast, [])
    True
    >>> actor_in([], ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    False
    >>> actor_in(cast, ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    True
    >>> actor_in(cast, ['Mona Singh', 'Aamir Khan', 'Achita Sikamana'])
    True
    >>> actor_in(cast, ['Mona Singh', 'Achita Sikamana', 'Aamir Khan'])
    True
    >>> actor_in(cast, ['Mona Singh', 'Achita Sikamana'])
    False
    """
    is_found = False
    
    if actors == []:
        is_found = True
        
    for actor in actors:
        if actor in cast:
            is_found = True

    return is_found