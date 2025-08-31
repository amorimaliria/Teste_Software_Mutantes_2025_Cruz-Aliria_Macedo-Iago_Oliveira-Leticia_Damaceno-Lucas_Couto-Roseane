# -*- coding: utf-8 -*-

"""
Python version of unix utility Cal 
"""


number_of_days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
    
def x_number_of_days__mutmut_orig(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) and month == 2):
        return 29

    if ( year == 1752 and month == 9 ):
        return 19
   
    return number_of_days_month[month]
    
def x_number_of_days__mutmut_1(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) or month == 2):
        return 29

    if ( year == 1752 and month == 9 ):
        return 19
   
    return number_of_days_month[month]
    
def x_number_of_days__mutmut_2(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(None) and month == 2):
        return 29

    if ( year == 1752 and month == 9 ):
        return 19
   
    return number_of_days_month[month]
    
def x_number_of_days__mutmut_3(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) and month != 2):
        return 29

    if ( year == 1752 and month == 9 ):
        return 19
   
    return number_of_days_month[month]
    
def x_number_of_days__mutmut_4(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) and month == 3):
        return 29

    if ( year == 1752 and month == 9 ):
        return 19
   
    return number_of_days_month[month]
    
def x_number_of_days__mutmut_5(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) and month == 2):
        return 30

    if ( year == 1752 and month == 9 ):
        return 19
   
    return number_of_days_month[month]
    
def x_number_of_days__mutmut_6(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) and month == 2):
        return 29

    if ( year == 1752 or month == 9 ):
        return 19
   
    return number_of_days_month[month]
    
def x_number_of_days__mutmut_7(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) and month == 2):
        return 29

    if ( year != 1752 and month == 9 ):
        return 19
   
    return number_of_days_month[month]
    
def x_number_of_days__mutmut_8(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) and month == 2):
        return 29

    if ( year == 1753 and month == 9 ):
        return 19
   
    return number_of_days_month[month]
    
def x_number_of_days__mutmut_9(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) and month == 2):
        return 29

    if ( year == 1752 and month != 9 ):
        return 19
   
    return number_of_days_month[month]
    
def x_number_of_days__mutmut_10(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) and month == 2):
        return 29

    if ( year == 1752 and month == 10 ):
        return 19
   
    return number_of_days_month[month]
    
def x_number_of_days__mutmut_11(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) and month == 2):
        return 29

    if ( year == 1752 and month == 9 ):
        return 20
   
    return number_of_days_month[month]

x_number_of_days__mutmut_mutants : ClassVar[MutantDict] = {
'x_number_of_days__mutmut_1': x_number_of_days__mutmut_1, 
    'x_number_of_days__mutmut_2': x_number_of_days__mutmut_2, 
    'x_number_of_days__mutmut_3': x_number_of_days__mutmut_3, 
    'x_number_of_days__mutmut_4': x_number_of_days__mutmut_4, 
    'x_number_of_days__mutmut_5': x_number_of_days__mutmut_5, 
    'x_number_of_days__mutmut_6': x_number_of_days__mutmut_6, 
    'x_number_of_days__mutmut_7': x_number_of_days__mutmut_7, 
    'x_number_of_days__mutmut_8': x_number_of_days__mutmut_8, 
    'x_number_of_days__mutmut_9': x_number_of_days__mutmut_9, 
    'x_number_of_days__mutmut_10': x_number_of_days__mutmut_10, 
    'x_number_of_days__mutmut_11': x_number_of_days__mutmut_11
}

def number_of_days(*args, **kwargs):
    result = _mutmut_trampoline(x_number_of_days__mutmut_orig, x_number_of_days__mutmut_mutants, args, kwargs)
    return result 

number_of_days.__signature__ = _mutmut_signature(x_number_of_days__mutmut_orig)
x_number_of_days__mutmut_orig.__name__ = 'x_number_of_days'




def x_first_of_month__mutmut_orig(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_1(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = None

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_2(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 1

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_3(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) or month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_4(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(None) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_5(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month >= 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_6(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 3):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_7(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k = 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_8(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k -= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_9(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 2
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_10(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(None, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_11(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, None):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_12(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_13(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, ):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_14(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(1, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_15(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k = number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_16(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k -= number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_17(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 or month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_18(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year != 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_19(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1753 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_20(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month >= 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_21(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 10 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_22(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k = 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_23(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k += 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_24(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 12

    k %= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_25(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k = 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_26(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k /= 7
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_27(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 8
    k = int(k + jan1(year)) % 7

    return k




def x_first_of_month__mutmut_28(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = None

    return k




def x_first_of_month__mutmut_29(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) / 7

    return k




def x_first_of_month__mutmut_30(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(None) % 7

    return k




def x_first_of_month__mutmut_31(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k - jan1(year)) % 7

    return k




def x_first_of_month__mutmut_32(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(None)) % 7

    return k




def x_first_of_month__mutmut_33(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 8

    return k

x_first_of_month__mutmut_mutants : ClassVar[MutantDict] = {
'x_first_of_month__mutmut_1': x_first_of_month__mutmut_1, 
    'x_first_of_month__mutmut_2': x_first_of_month__mutmut_2, 
    'x_first_of_month__mutmut_3': x_first_of_month__mutmut_3, 
    'x_first_of_month__mutmut_4': x_first_of_month__mutmut_4, 
    'x_first_of_month__mutmut_5': x_first_of_month__mutmut_5, 
    'x_first_of_month__mutmut_6': x_first_of_month__mutmut_6, 
    'x_first_of_month__mutmut_7': x_first_of_month__mutmut_7, 
    'x_first_of_month__mutmut_8': x_first_of_month__mutmut_8, 
    'x_first_of_month__mutmut_9': x_first_of_month__mutmut_9, 
    'x_first_of_month__mutmut_10': x_first_of_month__mutmut_10, 
    'x_first_of_month__mutmut_11': x_first_of_month__mutmut_11, 
    'x_first_of_month__mutmut_12': x_first_of_month__mutmut_12, 
    'x_first_of_month__mutmut_13': x_first_of_month__mutmut_13, 
    'x_first_of_month__mutmut_14': x_first_of_month__mutmut_14, 
    'x_first_of_month__mutmut_15': x_first_of_month__mutmut_15, 
    'x_first_of_month__mutmut_16': x_first_of_month__mutmut_16, 
    'x_first_of_month__mutmut_17': x_first_of_month__mutmut_17, 
    'x_first_of_month__mutmut_18': x_first_of_month__mutmut_18, 
    'x_first_of_month__mutmut_19': x_first_of_month__mutmut_19, 
    'x_first_of_month__mutmut_20': x_first_of_month__mutmut_20, 
    'x_first_of_month__mutmut_21': x_first_of_month__mutmut_21, 
    'x_first_of_month__mutmut_22': x_first_of_month__mutmut_22, 
    'x_first_of_month__mutmut_23': x_first_of_month__mutmut_23, 
    'x_first_of_month__mutmut_24': x_first_of_month__mutmut_24, 
    'x_first_of_month__mutmut_25': x_first_of_month__mutmut_25, 
    'x_first_of_month__mutmut_26': x_first_of_month__mutmut_26, 
    'x_first_of_month__mutmut_27': x_first_of_month__mutmut_27, 
    'x_first_of_month__mutmut_28': x_first_of_month__mutmut_28, 
    'x_first_of_month__mutmut_29': x_first_of_month__mutmut_29, 
    'x_first_of_month__mutmut_30': x_first_of_month__mutmut_30, 
    'x_first_of_month__mutmut_31': x_first_of_month__mutmut_31, 
    'x_first_of_month__mutmut_32': x_first_of_month__mutmut_32, 
    'x_first_of_month__mutmut_33': x_first_of_month__mutmut_33
}

def first_of_month(*args, **kwargs):
    result = _mutmut_trampoline(x_first_of_month__mutmut_orig, x_first_of_month__mutmut_mutants, args, kwargs)
    return result 

first_of_month.__signature__ = _mutmut_signature(x_first_of_month__mutmut_orig)
x_first_of_month__mutmut_orig.__name__ = 'x_first_of_month'



def x_is_leap__mutmut_orig(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_1(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year < 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_2(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1753 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_3(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year / 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_4(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 5 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_5(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 != 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_6(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 1 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_7(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return False
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_8(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return True

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_9(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year / 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_10(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 401 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_11(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 != 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_12(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 1 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_13(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return False
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_14(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year / 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_15(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 101 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_16(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 != 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_17(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 1 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_18(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return True
        if ( year % 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_19(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year / 4 == 0 ):
            return True

    return False



def x_is_leap__mutmut_20(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 5 == 0 ):
            return True

    return False



def x_is_leap__mutmut_21(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 != 0 ):
            return True

    return False



def x_is_leap__mutmut_22(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 1 ):
            return True

    return False



def x_is_leap__mutmut_23(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return False

    return False



def x_is_leap__mutmut_24(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return True

x_is_leap__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_leap__mutmut_1': x_is_leap__mutmut_1, 
    'x_is_leap__mutmut_2': x_is_leap__mutmut_2, 
    'x_is_leap__mutmut_3': x_is_leap__mutmut_3, 
    'x_is_leap__mutmut_4': x_is_leap__mutmut_4, 
    'x_is_leap__mutmut_5': x_is_leap__mutmut_5, 
    'x_is_leap__mutmut_6': x_is_leap__mutmut_6, 
    'x_is_leap__mutmut_7': x_is_leap__mutmut_7, 
    'x_is_leap__mutmut_8': x_is_leap__mutmut_8, 
    'x_is_leap__mutmut_9': x_is_leap__mutmut_9, 
    'x_is_leap__mutmut_10': x_is_leap__mutmut_10, 
    'x_is_leap__mutmut_11': x_is_leap__mutmut_11, 
    'x_is_leap__mutmut_12': x_is_leap__mutmut_12, 
    'x_is_leap__mutmut_13': x_is_leap__mutmut_13, 
    'x_is_leap__mutmut_14': x_is_leap__mutmut_14, 
    'x_is_leap__mutmut_15': x_is_leap__mutmut_15, 
    'x_is_leap__mutmut_16': x_is_leap__mutmut_16, 
    'x_is_leap__mutmut_17': x_is_leap__mutmut_17, 
    'x_is_leap__mutmut_18': x_is_leap__mutmut_18, 
    'x_is_leap__mutmut_19': x_is_leap__mutmut_19, 
    'x_is_leap__mutmut_20': x_is_leap__mutmut_20, 
    'x_is_leap__mutmut_21': x_is_leap__mutmut_21, 
    'x_is_leap__mutmut_22': x_is_leap__mutmut_22, 
    'x_is_leap__mutmut_23': x_is_leap__mutmut_23, 
    'x_is_leap__mutmut_24': x_is_leap__mutmut_24
}

def is_leap(*args, **kwargs):
    result = _mutmut_trampoline(x_is_leap__mutmut_orig, x_is_leap__mutmut_mutants, args, kwargs)
    return result 

is_leap.__signature__ = _mutmut_signature(x_is_leap__mutmut_orig)
x_is_leap__mutmut_orig.__name__ = 'x_is_leap'




def x_jan1__mutmut_orig(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_1(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = None

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_2(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 1, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_3(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 1

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_4(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = None
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_5(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = None

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_6(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y - (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_7(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 - y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_8(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 5 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_9(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) * 4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_10(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y - 3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_11(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+4) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_12(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /5

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_13(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y >= 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_14(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1801):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_15(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d = (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_16(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d += (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_17(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701) * 100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_18(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y + 1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_19(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1702)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_20(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/101
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_21(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d = (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_22(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d -= (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_23(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601) * 400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_24(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y + 1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_25(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1602)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_26(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/401

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_27(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y >= 1752):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_28(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1753):
        d += 3

    return int(d % 7)




def x_jan1__mutmut_29(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d = 3

    return int(d % 7)




def x_jan1__mutmut_30(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d -= 3

    return int(d % 7)




def x_jan1__mutmut_31(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 4

    return int(d % 7)




def x_jan1__mutmut_32(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(None)




def x_jan1__mutmut_33(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d / 7)




def x_jan1__mutmut_34(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 8)

x_jan1__mutmut_mutants : ClassVar[MutantDict] = {
'x_jan1__mutmut_1': x_jan1__mutmut_1, 
    'x_jan1__mutmut_2': x_jan1__mutmut_2, 
    'x_jan1__mutmut_3': x_jan1__mutmut_3, 
    'x_jan1__mutmut_4': x_jan1__mutmut_4, 
    'x_jan1__mutmut_5': x_jan1__mutmut_5, 
    'x_jan1__mutmut_6': x_jan1__mutmut_6, 
    'x_jan1__mutmut_7': x_jan1__mutmut_7, 
    'x_jan1__mutmut_8': x_jan1__mutmut_8, 
    'x_jan1__mutmut_9': x_jan1__mutmut_9, 
    'x_jan1__mutmut_10': x_jan1__mutmut_10, 
    'x_jan1__mutmut_11': x_jan1__mutmut_11, 
    'x_jan1__mutmut_12': x_jan1__mutmut_12, 
    'x_jan1__mutmut_13': x_jan1__mutmut_13, 
    'x_jan1__mutmut_14': x_jan1__mutmut_14, 
    'x_jan1__mutmut_15': x_jan1__mutmut_15, 
    'x_jan1__mutmut_16': x_jan1__mutmut_16, 
    'x_jan1__mutmut_17': x_jan1__mutmut_17, 
    'x_jan1__mutmut_18': x_jan1__mutmut_18, 
    'x_jan1__mutmut_19': x_jan1__mutmut_19, 
    'x_jan1__mutmut_20': x_jan1__mutmut_20, 
    'x_jan1__mutmut_21': x_jan1__mutmut_21, 
    'x_jan1__mutmut_22': x_jan1__mutmut_22, 
    'x_jan1__mutmut_23': x_jan1__mutmut_23, 
    'x_jan1__mutmut_24': x_jan1__mutmut_24, 
    'x_jan1__mutmut_25': x_jan1__mutmut_25, 
    'x_jan1__mutmut_26': x_jan1__mutmut_26, 
    'x_jan1__mutmut_27': x_jan1__mutmut_27, 
    'x_jan1__mutmut_28': x_jan1__mutmut_28, 
    'x_jan1__mutmut_29': x_jan1__mutmut_29, 
    'x_jan1__mutmut_30': x_jan1__mutmut_30, 
    'x_jan1__mutmut_31': x_jan1__mutmut_31, 
    'x_jan1__mutmut_32': x_jan1__mutmut_32, 
    'x_jan1__mutmut_33': x_jan1__mutmut_33, 
    'x_jan1__mutmut_34': x_jan1__mutmut_34
}

def jan1(*args, **kwargs):
    result = _mutmut_trampoline(x_jan1__mutmut_orig, x_jan1__mutmut_mutants, args, kwargs)
    return result 

jan1.__signature__ = _mutmut_signature(x_jan1__mutmut_orig)
x_jan1__mutmut_orig.__name__ = 'x_jan1'



def x_cal__mutmut_orig(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_1(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n != 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_2(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 20 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_3(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "XX       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30XX"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_4(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = None

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_5(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = "XXXX"

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_6(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(None, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_7(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, None):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_8(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_9(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, ):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_10(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(1, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_11(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s = "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_12(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s -= "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_13(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "XX   XX"

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_14(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = None
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_15(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds - 1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_16(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+2
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_17(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(None, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_18(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, None):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_19(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_20(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, ):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_21(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(2, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_22(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n - 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_23(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 2):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_24(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k <= 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_25(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 11 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_26(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s = " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_27(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s -= " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_28(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += "XX XX"
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_29(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s = str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_30(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s -= str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_31(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(None)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_32(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont / 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_33(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 8 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_34(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 != 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_35(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 1):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_36(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s = "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_37(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s -= "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_38(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "XX\nXX"
        
        else:
            s += " "
        
        cont+= 1

    return s



def x_cal__mutmut_39(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s = " "
        
        cont+= 1

    return s



def x_cal__mutmut_40(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s -= " "
        
        cont+= 1

    return s



def x_cal__mutmut_41(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += "XX XX"
        
        cont+= 1

    return s



def x_cal__mutmut_42(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont = 1

    return s



def x_cal__mutmut_43(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont -= 1

    return s



def x_cal__mutmut_44(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 2

    return s

x_cal__mutmut_mutants : ClassVar[MutantDict] = {
'x_cal__mutmut_1': x_cal__mutmut_1, 
    'x_cal__mutmut_2': x_cal__mutmut_2, 
    'x_cal__mutmut_3': x_cal__mutmut_3, 
    'x_cal__mutmut_4': x_cal__mutmut_4, 
    'x_cal__mutmut_5': x_cal__mutmut_5, 
    'x_cal__mutmut_6': x_cal__mutmut_6, 
    'x_cal__mutmut_7': x_cal__mutmut_7, 
    'x_cal__mutmut_8': x_cal__mutmut_8, 
    'x_cal__mutmut_9': x_cal__mutmut_9, 
    'x_cal__mutmut_10': x_cal__mutmut_10, 
    'x_cal__mutmut_11': x_cal__mutmut_11, 
    'x_cal__mutmut_12': x_cal__mutmut_12, 
    'x_cal__mutmut_13': x_cal__mutmut_13, 
    'x_cal__mutmut_14': x_cal__mutmut_14, 
    'x_cal__mutmut_15': x_cal__mutmut_15, 
    'x_cal__mutmut_16': x_cal__mutmut_16, 
    'x_cal__mutmut_17': x_cal__mutmut_17, 
    'x_cal__mutmut_18': x_cal__mutmut_18, 
    'x_cal__mutmut_19': x_cal__mutmut_19, 
    'x_cal__mutmut_20': x_cal__mutmut_20, 
    'x_cal__mutmut_21': x_cal__mutmut_21, 
    'x_cal__mutmut_22': x_cal__mutmut_22, 
    'x_cal__mutmut_23': x_cal__mutmut_23, 
    'x_cal__mutmut_24': x_cal__mutmut_24, 
    'x_cal__mutmut_25': x_cal__mutmut_25, 
    'x_cal__mutmut_26': x_cal__mutmut_26, 
    'x_cal__mutmut_27': x_cal__mutmut_27, 
    'x_cal__mutmut_28': x_cal__mutmut_28, 
    'x_cal__mutmut_29': x_cal__mutmut_29, 
    'x_cal__mutmut_30': x_cal__mutmut_30, 
    'x_cal__mutmut_31': x_cal__mutmut_31, 
    'x_cal__mutmut_32': x_cal__mutmut_32, 
    'x_cal__mutmut_33': x_cal__mutmut_33, 
    'x_cal__mutmut_34': x_cal__mutmut_34, 
    'x_cal__mutmut_35': x_cal__mutmut_35, 
    'x_cal__mutmut_36': x_cal__mutmut_36, 
    'x_cal__mutmut_37': x_cal__mutmut_37, 
    'x_cal__mutmut_38': x_cal__mutmut_38, 
    'x_cal__mutmut_39': x_cal__mutmut_39, 
    'x_cal__mutmut_40': x_cal__mutmut_40, 
    'x_cal__mutmut_41': x_cal__mutmut_41, 
    'x_cal__mutmut_42': x_cal__mutmut_42, 
    'x_cal__mutmut_43': x_cal__mutmut_43, 
    'x_cal__mutmut_44': x_cal__mutmut_44
}

def cal(*args, **kwargs):
    result = _mutmut_trampoline(x_cal__mutmut_orig, x_cal__mutmut_mutants, args, kwargs)
    return result 

cal.__signature__ = _mutmut_signature(x_cal__mutmut_orig)
x_cal__mutmut_orig.__name__ = 'x_cal'




if __name__ == "__main__":
    
    dayw = "Do Se Te Qa Qi Se Sa"

    smon = ["Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"]

    import sys

    number_of_parameters = len(sys.argv) 

    if(number_of_parameters >= 3 or number_of_parameters == 1):

        #print out just month
        if(number_of_parameters == 1):

            #current month
            import datetime
            today = datetime.datetime.today()

            m = today.month
            y = today.year
        
        else:

            m = 0

            #parse the month parameter
            try:
                m = int(sys.argv[1]) #argv[0] is  always the name of the python script. [1] is the first parameter
            except Exception as e:
                print("type error: " + str(e))

            if(m < 1 or m > 12):
                print("Cal: {}: invalid month.\n".format(sys.argv[1]))
                sys.exit(-1)

            y = 0

            #parse the year parameter
            try:
                y = int(sys.argv[2])

            except Exception as e:
                print("type error: " + str(e))

            if(y < 1 or y > 9999):
                print("Cal: {}: invalid year.\n".format(sys.argv[2]))
                sys.exit(-1)

        #print the result
        print("   {} {}\n".format(smon[m-1], y) )
        print("{}\n".format(dayw))

        dds = first_of_month(m, y)
        n   = number_of_days(m, y)
        result = cal(dds, n)

        print(result)
        print()
    

    #print the complet year
    else:
        
        y = 0

        #parse the year parameter
        try:
            y = int(sys.argv[1])

        except Exception as e:
            print("type error: " + str(e))

        if(y < 1 or y > 9999):
            print("Cal: {}: invalid year.\n".format(sys.argv[1]))
            sys.exit(-1)

        for z in range(1, 13):

            print("   {} {}\n".format(smon[z-1], y) )
            print("{}\n".format(dayw))

            dds = first_of_month(z, y)
            n   = number_of_days(z, y)
            
            result = cal(dds, n)

            print(result)
            print()