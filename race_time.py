import doctest
class RaceTime:
    """ RaceTime: represents a race time result in 
    milliseconds (ms), seconds (sec), minutes (mins)
    Precondition, ms, sec, mins>=0, ms<1000, sec<60
    """

    def __init__(self, ms: int, sec: int, mins: int) -> None:
        """ initializes attributes of RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        """
        self.__ms = ms
        self.__sec = sec
        self.__mins = mins

    def get_ms(self) -> int:
        """ returns ms of self RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        >>> rt.get_ms()
        88
        """
        return self.__ms

    def get_sec(self) -> int:
        """ returns sec of self RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        >>> rt.get_sec()
        20
        """
        return self.__sec

    def get_mins(self) -> int:
        """ returns mins of self RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        >>> rt.get_mins()
        4
        """
        return self.__mins

    def __str__(self) -> str:
        """ returns a readable string with ms, sec, mins of RaceTime
        >>> rt = RaceTime(88, 20, 4)
        >>> str(rt)
        '4:20:88'
        """
        return f'{self.__mins}:{self.__sec}:{self.__ms}'

    def __repr__(self) -> str:
        """ returns a string representation of self RaceTime
        >>> rt = RaceTime(88, 20, 4)
        >>> repr(rt)
        'RaceTime(88, 20, 4)'
        """
        return f'RaceTime({self.__ms}, {self.__sec}, {self.__mins})'

    def __eq__(self, other: 'RaceTime') -> bool:
        """ returns True if self RaceTime has same ms, sec, mins as
        other RaceTime, otherwise False
        >>> rt121920a = RaceTime(12, 19, 20)
        >>> rt121920b = RaceTime(12, 19, 20)
        >>> rt121921  = RaceTime(12, 19, 21)
        >>> rt121820  = RaceTime(12, 18, 20)
        >>> rt111920  = RaceTime(11, 19, 20)

        >>> rt121920a == rt121920a
        True
        >>> rt121920a == rt121920b
        True
        >>> rt121920a == rt121921
        False
        >>> rt121920a == rt121820
        False
        >>> rt121920a == rt111920
        False
        """
        return (self.__ms == other.get_ms()
                and self.__sec == other.get_sec()
                and self.__mins == other.get_mins())
    
    def is_faster(self, other: 'RaceTime') -> bool:
        """determines if Racetime self is faster than Racetime other
        >>> rt1 = RaceTime(88, 20, 4)
        >>> rt2 = RaceTime(88, 20, 4)
        >>> rt3 = RaceTime(89, 20, 4)
        >>> rt4 = RaceTime(89, 21, 4)
        >>> rt5 = RaceTime(89, 21, 5)
        >>> rt6 = RaceTime(87, 20, 4)
        >>> rt7 = RaceTime(89, 19, 4)
        >>> rt8 = RaceTime(89, 20, 3)
        >>> rt1.is_faster(rt2)
        False
        >>> rt1.is_faster(rt3)
        True
        >>> rt1.is_faster(rt4)
        True
        >>> rt1.is_faster(rt5)
        True
        >>> rt1.is_faster(rt6)
        False
        >>> rt1.is_faster(rt7)
        False
        >>> rt1.is_faster(rt8)
        False
        """
        if self.__mins < other.get_mins():
            return True
        elif self.__mins == other.get_mins() and self.__sec < other.get_sec():
            return True
        elif (self.__mins == other.get_mins() and 
              self.__sec == other.get_sec() and self.__ms < other.get_ms()):
            return True
        else:
            return False
        
        