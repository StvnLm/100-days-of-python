import random
import itertools

# First task: flip the first and last name.
# Second task: make a generator and randomly return a pair of names

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def reverse_first_last_names(name):
    first, last = name.split()
    # ' '.join([last, first]) -- wait we have f-strings now (>= 3.6)
    return f'{last} {first}'

def gen_pairs(names=NAMES):
    first_names = [name.split()[0].title() for name in names]
    while True:
        firstname, secondname = None, None
        while firstname == secondname:
            firstname, secondname = random.sample(first_names, 2)
        yield f'{firstname} teams up with {secondname}'


pairs = gen_pairs()
first_ten = itertools.islice(pairs, 10)
print(list(first_ten))
