# * Iterable unpacking and ** Dictionary unpacking operators

import os
f = open(os.devnull, 'w')
# f = None # uncomment to print

# prefix operators
# not to be confused with infix * multiplication and ** exponentiation
# Also called
# "packing" and "unpacking" operator
# "splat" (from Roby)
#  "star", "double start", "star star"

# different from the multiplication and exponentiatio
# in that they are used as prefix operators

# "unpacking":

# unpack iterable into tuple
*range(4), 4
# (0, 1, 2, 3, 4)

# unpack iterable into list or any sequence
[*range(4), 4]
# [0, 1, 2, 3, 4]

# unpack iterable into set
{*range(4), 4}
# {0, 1, 2, 3, 4}

# unpack dict into dict
{'x': 1, **{'y': 2}}
# {'x': 1, 'y': 2}

# unpack dict into dic and override key
{'y': 1, **{'y': 2}}
# { 'y': 2 }

# unpack iterable into function call arguments
# sending arbitrary length arguments to functions
# its not possible without the * operator without a list
# so not just syntactic sugar
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(*fruits, file=f)
# lemon pear watermelon tomato

# unpack dictionary into keyword arguments
date_info = {'year': "2020", 'month': "01", 'day': "01"}
"{year}-{month}-{day}.txt".format(**date_info)
# '2020-01-01.txt'

# "packing" or "catching":

# pack unassigned items with b as an array
a, *b, c = range(5)
# => 0 [1, 2, 3] 4

# Only one unpack operation allowed in list
  # a, *b, c, *d = [1, 2, 4, 3, 4, 5]
# Error

# packing any arguments given to a function into a tuple
def fu(*any_args):
  print(any_args, type(any_args), file=f)
fu('foo', 'bar')
# ('foo', 'bar') <class 'tuple'>

# packing any keyword arguments given to a function into a dict
def fa(**any_kwargs):
  print(any_kwargs, type(any_kwargs), file=f)
fa(foo=1, boo=2)
# {'foo': 1, 'boo': 2} <class 'dict'>

# pack arguments leaving keyword-only arguments
# when we pack all arguments into n_numbers
# the rest of the arguments are keyword-only arguments
def operation(*n_numbers, operation, silence_err = False):
  print(n_numbers, operation, silence_err, file=f)
operation(2, 4, 6, 3, 9, operation = '+')
# (2, 4, 6, 3, 9) + False

# if we try to use positional arguments afer kwargs we get an error
# operation(2, 4, 6, 3, 9, operation = '+', 4)
# Error

# we can make only kwargs functions by using *-on-its-own
# if you try to send positional args it will throw an Error
def only_kwargs(*, foo):
  print(foo, file=f)
only_kwargs(foo='bar')

# unpack dict to kwargs n times
date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
"{year}-{month}-{day}-{artist}-{title}.txt".format(**date_info, **track_info)

# multiple assignment unpacking with nested unpacking
(*starting_chars, last_char), *other = ['leon', 'volkov', 'range', 'velocity']
print(*starting_chars, last_char, *other, file=f)

# ** can be used to copy, extend or merge dicts

# Both * and ** can be used multiple times in function calls, as of Python 3.5.

# https://www.python.org/dev/peps/pep-0448/
# https://www.python.org/dev/peps/pep-3132/
# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/#Asterisks_in_tuple_unpacking
# https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
