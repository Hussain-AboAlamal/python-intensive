"""
For the function get_data(), which returns a list of days in a week
Create two decorators

Decorator #1 short_form -> returns the abbreviations of the days of the week
Example :
When get_data() is ['Monday', ..., 'Sunday'], then decorator
short_form have to return ['Mon', ..., 'Sun'].
Tip : discover the module `calendar`. Find a function there, that suitable for you

Decorator #2 translate(language) -> a decorator, which takes an argument `language`
Should translate the names of the days of the week into the language specified in the parameter.
Tip : discover how module `locale` works and find the function `setlocale`

As a result, the program should simply display a list of German abbreviations for the days of the week on the screen. ->
['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']

Decorators and execution code that testing it must be in different modules!

Nothing more ;)
"""
import calendar
from my_decorator import day_abbr, set_locale


@set_locale('de_DE')
@day_abbr
def get_data():
    return list(calendar.day_name)


if __name__ == '__main__':
    get_data()
