'''
CTRL + F will be enough to find a challenge
'''

import math, re, statistics


def hello(name=''):
    return f"Hello, {name.title() or 'World'}"


# ---------------------------

def hello(name=''):
    user_input = str(name).capitalize()
    if user_input:
        return f'Hello, {user_input}!'
    else:
        return 'Hello, World!'


# print(hello())

# ------------------------------------

def two_highest(arg1):
    if type(arg1) is list:
        new_list = sorted(list(set(arg1)))
        new_list.reverse()
        return new_list[:2]
    else:
        return False


# print(two_highest([15, 20, 20, 17]), [20, 17])

# ---------------------------
# Short Long Short

def solution(a, b):
    return a + b + a if len(a) < len(b) else b + a + b


# print(solution('1', '99'))

# ---------------------------
# USD => CNY

def usdcny(usd: int) -> str:
    # :.2f convert to 2 decimal places
    return f'{6.75 * usd:.2f} Chinese Yuan'


# i found it so simple:
# https://stackoverflow.com/a/47775345/15164646
# https://stackoverflow.com/a/28142318/15164646

# print(usdcny(6870))

# ------------------------------
# MakeUpperCase

def make_upper_case(string):
    return string.upper()


# or
def make_upper_case(string):
    return string.upper()


# print(make_upper_case('swagger'))

# ------------------------------
# What is between?


def between(a, b):
    return list(range(a, b + 1))


# print(between(-1, 6))

# -----------------------------
# All Star Code Challenge #18


def str_count(string, letter):
    # return len(string.split(letter))-1
    return string.count(letter)


# print(str_count('Hello', 'e'))

# -----------------------------
# Beginner Series #4 Cockroach


def cockroach_speed(s) -> int:
    return math.floor(s * 27.778)


# print(cockroach_speed(1.08))

# -----------------------------
# You only need one - Beginner


def check(seq, elem):
    return True if elem in seq else False


# print(check([66, 101], 66))

# ----------------------------
# Twice as old


def twise_as_old(dad_years_old, son_years_old):
    # abs() gives a positive value of any number in return
    return abs(2 * son_years_old - dad_years_old)


# print(twise_as_old(36, 7))

# -----------------------------
# Find Multiples of a Number


def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))


# print(find_multiples(5,25))

# -----------------------------
# Ensure question


def ensure_question(string):
    return string if string.endswith('?') else string + '?'
    # or

    if string.endswith('?'):
        return string
    else:
        string += '?'
        return string

    # or
    if not string.endswith("?"):
        return string + "?"
    return string


# print(ensure_question('Yes'))

# -----------------------------
# Jenny's secret message


def greet(name):
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"


# print(greet('Brabus'))

# -----------------------------
# Grasshopper - Function syntax debugging


def main(verb, noun):
    return verb + noun


# -----------------------------
# Grasshopper - Messi Goals


def messi_goals(league1, league2, league3):
    total_goals = sum([league1, league2, league3])
    return f"total goals should equal to {total_goals}"


# print(messi_goals(43, 10, 5))

# or
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = sum([la_liga_goals, champions_league_goals, copa_del_rey_goals])


# -----------------------------
# The Feast of Many Beasts
# the dish must START and END  with the same letters as the animal's name and returns TRUE or FALSE


def feast(beast_name, beast_dish):
    return True if beast_dish.startswith(
        beast_name[0]) and beast_dish.endswith(beast_name[-1]) else False
    # or
    return beast_name[0] == beast_dish[0] and beast_dish[-1] == beast_name[-1]


# print(feast("chickadee", "chocolate cake"))

# -----------------------------
# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# each lowercase letter becomes uppercase and each uppercase letter becomes lowercase


def to_alternating_case(string):
    return ''.join(
        [char.upper() if char.islower() else char.lower() for char in string])


# print(to_alternating_case('HeLLo WoRLD'))

# -----------------------------
# Reversed Words


def reverse_words(s):
    return ' '.join(reversed(s.split()))


# print(reverse_words("The greatest victory is that which requires no battle"))
# print becomes battle no requires which that is victory greatest The

# -----------------------------
# Find the smallest integer in the array


def find_smallest_int(arr):
    return min(arr)

    # or

    # sort array
    arr.sort()
    return arr[0]


# print(find_smallest_int([-123, -12121, -21122, 21,1,5,2]))

# -----------------------------
# Exclamation marks series #2: Remove all exclamation marks from the end of sentence


def remove(s):
    return s.rstrip('!')


# print(remove('!Heeeelllo! Yo! Oh, hay man!'))

# -----------------------------
# Filtering even numbers (Bug Fixes)


def kata_13_december(lst):
    new = list()
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            new.append(lst[i])
    return new


# or
# def kata_13_december(lst):
#     return [item for item in lst if item & 1]

# print(kata_13_december([1, 2, 2, 2, 4, 3, 4]))

# ----------------------------
# Compare within margin


def close_compare(a, b, margin=0):
    if a == b or abs(a - b) <= margin:
        return 0
    if a < b:
        return -1
    if a > b:
        return 1


# print(close_compare(6,5))

# -----------------------------
# is it a number?


def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False


# print(isDigit('-3sa'))

# -----------------------------
# Count of positives / sum of negatives
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.


def count_positives_sum_negatives(arr):
    count = []
    sum_numbers = []

    if not arr: return []

    for num in arr:
        if num > 0:
            count.append(num)
        elif num < 0:
            sum_numbers.append(num)

    return [len(count), sum(sum_numbers)]


# print(count_positives_sum_negatives([12,12,4,6,1,-21,-21,3,-3]))

# -----------------------------
# Alan Partridge II - Apple Turnover


def apple(x: str or int):
    return "It's hotter than the sun!!" if int(
        x
    )**2 > 1000 else 'Help yourself to a honeycomb Yorkie for the glovebox.'


# print(apple(60))

# -----------------------------
# Convert Boolean to String


def boolean_to_string(b):
    return str(b)


# -----------------------------
# Convert Hex To Decimal


def hex_to_dec(s):
    return int(s, 16)


# print(hex_to_dec('21'))

# -----------------------------
# Return Negative


def make_negative(number):
    return -number if int(number) > 0 else number
    # or
    return -abs(number)


# print(make_negative('-42'))

# -----------------------------
# Generate range of integers


def generate_range(min, max, step):
    return list(range(min, max + 1, step))


# print(generate_range(0, 20, 2))

# -----------------------------
# Count the number of cubes with paint on
''' 
PROOF:
number of cuts = x
The total number of cubes = (x+1)^3
the number of all blue cubes = (x-1)^3

Number of cubes with one or more red squares:
= (x+1)^3 - (x-1)^3
= (x+1)(x+1)(x+1) - (x-1)(x-1)(x-1)
= x^3 + 3x^2 + 3x + 1 - (x^3 - 3x^2 + 3x -1 )
= 6x^2 + 2
'''


def count_squares(x):
    return 6 * x**2 + 2


# print(count_squares(2))

# ------------------------------
# Swap names


def name_shuffler(str_):
    return ' '.join(reversed(str_.split()))
    # return ' '.join(str_.split()[::-1])

    # elems = str_.split(' ')
    # swap1 = elems[0]
    # swap2 = elems[1]
    # swap = swap2, swap1

    # return ' '.join(swap)


# print(name_shuffler('john McClane'))

# --------------------------------
# Delete all spaces


def no_space(x):
    return re.sub(r'\s+', '', x)
    # or
    return x.replace(' ', '')


# print(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'))

# --------------------------------
# Counting sheeps

array1 = [
    True, True, True, False, True, True, True, True, True, False, True, False,
    True, False, False, True, True, True, True, True, False, False, True, True
]


def count_sheeps(sheep):
    return sheep.count(True)


# print(count_sheeps(array1))

# --------------------------------
# Well of Ideas - Easy Version


def well(x):
    if x.count("good") == 0:
        return "Fail!"
    elif x.count("good") <= 2:
        return "Publish!"
    else:
        return "I smell a series!"


# print(well(['good', 'good', 'good', 'bad', 'bad']))

# --------------------------------
# Sum Mixed Array


def sum_mix(arr):
    return sum(list(map(int, arr)))
    # or
    return sum(map(int, arr))


# print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))

# --------------------------------
# Fake Binary


def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result


# or
# def fake_bin(x):
#     return ''.join('0' if c < '5' else '1' for c in x)

# print(fake_bin('45385593222131107843568'))

# --------------------------------
# Fake Light

# def update_light(current):
# return {"green": "yellow", "yellow": "red", "red": "green"}[current]


# or more readable
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."


# print(update_light('green'))

# ----------------------------
# Multiplication table for number


def multi_table(number):
    numbers = []
    for num in range(1, 11):
        numbers.append(f'{num} * {number} = {num * number}')
    return '\n'.join(numbers)


# or
# def multi_table(number):
#     return '\n'.join(f'{num} * {number} = {num * number}' for num in range(1, 11))

# print(multi_table(15))

# ----------------------------
# Convert number to reversed array of digits


def digitize(n):
    # list_ = []
    # for i in str(n):
    #     list_.append(int(i))
    # return list_[::-1]
    # or
    return [int(x) for x in reversed(str(n))]


# print(digitize(235141247889823898))

# --------------------------
# Count by X

def count_by(x, n):
    return [num * x for num in range(1, n + 1)]

    # or
    # return range(x, x * n + 1, x)

    # or
    # list_ = []
    # for num in range(1, n+1):
    #   out_num = num * x
    #   list_.append(out_num)
    # return list_


# print(count_by(3,5))


# -------------------------
# Square(n) Sum

def square_sum(numbers):
    return sum([num**2 for num in numbers])


# print(square_sum([1, 2, 2]))

# -------------------------
# Get the mean of an array

def get_average(marks):
    return sum(marks) // len(marks)
    # or
    # return math.floor(statistics.mean(marks))


# print(get_average([1, 5, 87, 45, 8, 8]))


# ---------------------------
# Sum of Strings

def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))


# print(sum_str(2, 5))

# ---------------------------
# Remove First and Last Character

def remove_char(s):
    return ''.join(s[1:-1])


# print(remove_char('eloquent'))


# ---------------------------
# String repeat

def repeat_str(repeat, string):
    return repeat * string


# or
# return ''.join(string for i in range(repeat))
# or
# _string = []
# for _ in range(repeat):
#     i = string
#     _string.append(i)
# return ''.join(_string)


# print(repeat_str(5, 'Запорожье'))

# ---------------------------
# Remove exclamation marks

def remove_exclamation_marks(s):
    return s.replace('!', '')


# --------------------------
# BMI Calc

def bmi(weight, height):
    bmi = weight / height**2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"


# ---------------------------

# Enumerable Magic #25 - Take the First N Elements

def take(arr, n):
    return arr[:n]


# --------------------------

# Extract URL domain name
from urllib.parse import urlparse


def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]


# print(domain_name('http://google.co.jp'))

# --------------------------

# Simple multiplication
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9


# --------------------------

# Define a card suit
def define_suit(card):
    # DECK = ['2S','3S','4S','5S','6S','7S','8S','9S',          '10S','JS','QS','KS','AS',
    #       '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
    #       '2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
    #       '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC']

    # for suit in DECK:
    #   if card[-1] in suit[-1] == 'C':
    #     return 'clubs'
    #   elif card[-1] in suit[-1] == 'D':
    #     return 'diamonds'
    #   elif card[-1] in suit[-1] == 'H':
    #     return 'hearts'
    #   elif card[-1] in suit[-1] == 'S':
    #     return 'spades'

    # or
    return {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}[card[-1]]


# print(define_suit("3H"))

# --------------------------

# Remove duplicates from list
def distinct(seq):
    return list(dict.fromkeys(seq))


# print(distinct([1,2,1,1,3,4,5,6,78,8]))

# --------------------------

# Enumerable Magic #1 - True for All?
greater_than_9 = lambda x: x > 9
less_than_9 = lambda x: x < 9


def all(seq, fun):
    return next((False for x in seq if not fun(x)), True)


# print(all(1, 2, 3, 4, 5))

# --------------------------

# Sort and Star
def two_sort(array):
    # return '***'.join(sorted(array)[0])
    # or
    return '***'.join(min(array))


# print(two_sort(["turns", "out", "buy", "eaur", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))

# --------------------------

# Find the first non-consecutive number
def first_non_consecutive(arr):
    pass


# print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))

# --------------------------

# Expressions Matter
def expression_matter(a, b, c):
    return max(a * b * c, a + b + c, (a + b) * c, a * (b + c))


# print(expression_matter(1,2,3))

# -------------------------

# Reversed sequence
def reverse_seq(n):
    return [_ for _ in range(1, n + 1)][::-1]

    # or
    # list(range(n, 0, -1))

    # or
    # return range(n, 0, -1)

    # or
    # return [x for x in range(n, 0, -1)]


# print(reverse_seq(5))

# ---------------------

# Century From Year
def century(year):
    return (year + 99) // 100


# print(century(1705))

# ----------------------

# Find Maximum and Minimum Values of a List
def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)


# -----------------------

# Correct the mistakes of the character recognition software
def correct(s):
    return s.replace("0", "O").replace("5", "S").replace("1", "I")


# print(correct("L51ND0N"))

# ----------------------

# Double Char
def double_char(s):
    return ''.join([char * 2 for char in s])

# print(double_char("Hello World"))
