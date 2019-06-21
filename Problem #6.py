'''
Write a function for doing an in-place ↴ shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have the same probability
of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.
'''

import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def naive_shuffle(the_list):
    # For each index in the list
    for first_index in xrange(0, len(the_list) - 1):
        # Grab a random other index
        second_index = get_random(0, len(the_list) - 1)
        # And swap the values
        if second_index != first_index:
            the_list[first_index], the_list[second_index] = \
                the_list[second_index], the_list[first_index]