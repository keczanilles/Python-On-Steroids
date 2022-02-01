def parse_user_data(line):
    """
    >>> parse_user_data('John Doe john.doe@example.com')
    ('John', 'Doe', 'john.doe', 'example.com')
    """
    return (line.split()[0], line.split()[1], (line.split()[2]).split('@')[0],(line.split()[2]).split('@')[1])

def compare_lists(dir_a, dir_b):
    """
    >>> dir_a = ['hello.py', 'readme.txt']
    >>> dir_b = ['readme.txt', 'install.txt', 'hello2.py']
    >>> compare_lists(dir_a, dir_b)
    {'removed': ['hello.py'], 'added': ['hello2.py', 'install.txt']}
    """

    return {'removed': sorted([x for x in dir_a if x not in dir_b]), 'added': sorted([x for x in dir_b if x not in dir_a])}

from datetime import datetime 
def print_log(message, process_id, timestamp, level=2):
    """
    >>> from datetime import datetime
    >>> print_log('System started!', 1532, datetime(2019, 1, 2, 10, 30, 55).isoformat(' '))
    2019-01-02 10:30:55 [1532] [INFO] System started!
    """
    levels = {0: 'TRACE', 1: 'DEBUG', 2: 'INFO', 3: 'WARN', 4: 'ERROR'}
    print(f'{timestamp} [{process_id}] [{levels[level]}] {message}')

def biggest_rectangle(rectangles):
    """
    Find the biggest rectangle in a sequence.
    Rectangles are represented as tuples of (width, height).

    >>> biggest_rectangle([(2, 4), (3, 3), (4, 2)])
    (3, 3)
    """

    return sorted(rectangles, key = lambda x: (x[0]*x[1]), reverse = True)[0]



def find_in_file(pattern, filename):
    """
    Find a pattern in file. Print out all lines that match the pattern
    (case-insensitive) with line numbers.

    >>> find_in_file('nevermore', 'raven.txt')
     62 Quoth the Raven, "Nevermore."
     69 With such name as "Nevermore."
     77 Then the bird said, "Nevermore."
     84 Of 'Never- nevermore'."
     92 Meant in croaking "Nevermore."
     99 She shall press, ah, nevermore!
    107 Quoth the Raven, "Nevermore."
    115 Quoth the Raven, "Nevermore."
    123 Quoth the Raven, "Nevermore."
    132 Quoth the Raven, "Nevermore."
    140 Shall be lifted- nevermore!
    """

    with open('raven.txt', 'r') as f:
        l = [(key, value.strip()) for key, value in enumerate(f.readlines()) if pattern.lower() in value.lower()]
    for i in l:
        print(f'{i[0] if len(str(i[0])) > 2 else " " + str(i[0])} {i[1]}')


def read_long_words(filename, min_length=0):
    """
    >>> words = read_long_words('raven.txt', 5)
    >>> words[:6]
    ['midnight', 'dreary', 'pondered', 'quaint', 'curious', 'volume']
    """
    with open(filename, 'r') as f:
        x = "".join([x for x in f.read() if x not in r'[.,"!-]' ])
    return [i.lower() for i in x.split() if len(i) > min_length]


def top_words(words, n=10):
    """
    Find top N words in a file. Return a list of tuples (word, count).

    >>> words = read_long_words('raven.txt', 5)
    >>> top_words(words, 5)
    [('chamber', 11), ('nevermore', 10), ('lenore', 8), ('nothing', 7), ('tapping', 5)]
    """

    return sorted([(x, words.count(x)) for x in set(words)], key = lambda x : x[1], reverse = True)[:n]
