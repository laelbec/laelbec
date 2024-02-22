import doctest
from race_time import RaceTime
from race_result import RaceResult

# represents a racer as (name, country)
# where name and country != ''
RacerNameCountry = tuple[str, str]

# represents race time as (milliseconds, seconds, minutes)
# where all elements >= 0
Time = tuple[int, int, int]

# columns of values in input file row and positions in RacerNameCountry
NAME = 0
COUNTRY = 1
TIME_MS = 2

MS = 0
SEC = 1
MIN = 2

MS_SEC = 1000
MS_MIN = 60000

def read_file(filename: str) -> list[RaceResult]:
    """ returns a list of RaceResults populated with data from filename
    Precondition: the file exists, is not empty, has the following
      information on each row separated by commas:
      racer's name, racer's country, race time in milliseconds>=0
      and contains a header row with the column titles.
      The header row is ignored.

    >>> read_file('0lines_data.csv')
    []
    >>> read_file('9lines_data.csv') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Evan Jager', 'United States', RaceTime(450, 0, 8)), \
     RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7)), \
     RaceResult('Saif Saaeed Shaheen', 'Qatar', RaceTime(630, 53, 7)), \
     RaceResult('Wander Moura', 'Brazil', RaceTime(410, 14, 8)), \
     RaceResult('Mahiedine Mekhissi-Benabbad', 'France', RaceTime(90, 0, 8)), \
     RaceResult('Peter Renner', 'New Zealand', RaceTime(50, 14, 8))]
    """
    # TODO: complete this function
    file_handle = open(filename, 'r')
    header = file_handle.readline()
    
    lo_raceresult = []
    for line in file_handle:
        line = line.strip()
        line_list = line.split(',')
        name = line_list[NAME]
        country = line_list[COUNTRY]
        Time = convert_millisecond(int(line_list[TIME_MS]))
        racetime = RaceTime(Time[MS], Time[SEC], Time[MIN])
        race_result = RaceResult(name, country, racetime)
        lo_raceresult.append(race_result)
        
    file_handle.close()
    return lo_raceresult

def convert_millisecond(ms: int) -> Time:
    """converts given ms to a time tuple
    >>> convert_millisecond(0)
    (0, 0, 0)
    >>> convert_millisecond(1)
    (1, 0, 0)
    >>> convert_millisecond(1000)
    (0, 1, 0)
    >>> convert_millisecond(60000)
    (0, 0, 1)
    >>> convert_millisecond(480450)
    (450, 0, 8)
    >>> convert_millisecond(494050)
    (50, 14, 8)
    """
    if ms >= MS_MIN:
        minute = ms // MS_MIN
    else:
        minute = 0
        
    min_remainder = ms % MS_MIN
    if min_remainder >= MS_SEC:
        sec = min_remainder // MS_SEC
    else:
        sec = 0
        
    ms_remainder = min_remainder % MS_SEC
    
    Time = (ms_remainder, sec, minute)
    return Time

def find_athlete(loresults: list[RaceResult], name: str) -> int:
    """ returns the position of RaceResult with given athlete name in loresults
    Returns -1 if name not found
    Returns the position of the first if there >1 RaceResult with given name
    Precondition: case sensitive (ie. 'Brad' != 'brad')

    >>> find_athlete([], 'Brimin Kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))],\
        'brimin kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Brimin Kipruto')
    1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Peter Renner')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Usain Bolt', 'Canada', RaceTime(1, 2, 2019))], \
        'Usain Bolt')
    0
    """
    # TODO: complete this function
    num_elements = len(loresults)
    index = 0
    
    if num_elements == 0:
        return -1
    
    while index < num_elements and loresults[index].get_name() != name:
        index += 1
        
    if index == num_elements:
        index = -1
        
    return index

def get_all_from_country(loresults: list[RaceResult], country: str
                         ) -> list[RaceResult]:
    """ returns a list of all results of the given country
    Precondition: case sensitive (ie. 'Canada' != 'canada')

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 12)), \
     RaceResult('Perrier', 'France', RaceTime(1, 23, 18)), \
     RaceResult('Perrieruels', 'Canada', RaceTime(3, 29, 0)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country([], 'Jamaica')
    []

    >>> get_all_from_country(results, 'jamaica')
    []

    >>> get_all_from_country(results, 'Jamaica') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country(results, 'Japan')
    []
    """
    # TODO: complete this function
    lo_found = []
    
    for result in loresults:
        if result.get_country()  == country:
            lo_found.append(result)
            
    return lo_found

def get_fastest_time(loresults: list[RaceResult]) -> RaceTime:
    """ returns the fastest RaceTime of all finish_times of 
    RaceResult instances in loresults
    Precondition: loresults is not empty

    >>> one_result = [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 9))]
    >>> results = \
    [RaceResult('Allen', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 16, 17)), \
     RaceResult('Barnes', 'Canada', RaceTime(3, 43, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 29, 9)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 48, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 17))]

    >>> get_fastest_time(one_result)
    RaceTime(12, 31, 9)
    >>> get_fastest_time(results)
    RaceTime(3, 29, 9)
    """
    # TODO: complete this function
    num_elements = len(loresults)
    
    if num_elements == 1:
        return loresults[0].get_finish_time()
    
    fastest = loresults[0].get_finish_time()
    
    for index in range(1, num_elements):
        racetime = loresults[index].get_finish_time()
        if not fastest.is_faster(racetime):
            fastest = racetime
            
    return fastest


def get_with_fastest_time(loresults: list[RaceResult]
                          ) -> list[RacerNameCountry]:
    """ returns a list tuples of fastest RaceResults in loresults

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 6)), \
     RaceResult('Barnes', 'Canada', RaceTime(1, 23, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 10, 7)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 15, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 6))]
     
    >>> get_with_fastest_time([])
    []
    >>> get_with_fastest_time(results)
    [('Zhou', 'China'), ('Davis', 'Jamaica')]
    """
    # TODO: complete this function
    lo_fastest = []  
    
    if loresults == []:
        return lo_fastest
        
    fastest = get_fastest_time(loresults)
    for result in loresults:
        if result.get_finish_time() == fastest:
            RacerNameCountry = (result.get_name(), result.get_country())
            lo_fastest.append(RacerNameCountry)
    return lo_fastest
