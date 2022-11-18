import calendar
import locale
from functools import wraps


def day_abbr(func):
    """Print each day of the week with it's abbreviation

    Args:
        func (callback): function return the days of the week

    Returns:
        callback: function that wraps the input function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = zip(result, list(calendar.day_abbr))
        for day, abbr in result:
            print(f"{day} abbreviation is {abbr}")
    return wrapper


def set_locale(cult=''):
    """Change calendar current locale

    Args:
        locale (str, optional): calendar new locale. Defaults to ''.
    """
    def inner_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            locale.setlocale(locale.LC_ALL, cult)
            return func(*args, **kwargs)
        return wrapper
    return inner_function
