#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    """
    Create a dictionary from the given keys and values.
    :param keys: List of keys for the dictionary.
    :param values: List of values for the dictionary.
    :return: Dictionary created from keys and values.
    """
    result = {}
    index = 0
    while index < len(keys) and index < len(values):
        result[keys[index]] = values[index]
        index += 1
    return result

def shared_values(dict1, dict2):
    """
    Find the common values between two dictionaries.
    :param dict1: The first dictionary.
    :param dict2: The second dictionary.
    :return: A set of shared values between the two dictionaries.
    """
    values1 = set(dict1.values())
    values2 = set(dict2.values())
    return values1.intersection(values2)

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York:', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values:', common)

