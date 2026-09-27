from copy import copy
import numpy as np
# from more_itertools import locate
import itertools as it

def is_consecutive(list_of_numbers):
    list_of_numbers = np.sort(list_of_numbers)
    for i in range(len(list_of_numbers)-1):
        if list_of_numbers[i+1] - list_of_numbers[i] > 1 or \
        list_of_numbers[i+1] - list_of_numbers[i] == 0:
            return False
    # print(list_of_numbers)
    return True

def find_consecutive(list_of_lists):
    for element in it.product(*list_of_lists):
        if is_consecutive(list(element)):
            return True
    return False

"""
problems from leetcode:

Q. Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
or false otherwise.
Constraints:
1. s1 and s2 contains lowercase letters only
"""
def checkInclusion(s1: str, s2: str) -> bool:
    set_s1 = [s1[i] for i in range(len(s1))]
    set_s2 = [s2[i] for i in range(len(s2))]
    """
    trivial solution: for each letter in s1 find the initial occurance. 
    Once the first of the characters are found
    check for the following letters being permutations
    (account for multiple occurances)
    """
    """
    Non trivial solution:
    (works only for non-repeating characters)
    Time complexity: O(2nlogn + n)
    Space complexity O(len(s1) + 2*len(s2))
    """
    """
    editable_s2 = copy(set_s2)
    location_arr = np.ones(len(set_s1))
    for character_id in range(len(set_s1)):
        character = set_s1[character_id]
        if character in editable_s2:
            location_arr[character_id] = set_s2.index(character)
            editable_s2.pop(editable_s2.index(character))
        else:
            return False
    location_arr = np.sort(location_arr)
    for i in range(len(location_arr)-1):
        if location_arr[i] - location_arr[i+1] > 1:
            return False
        else:
            return True
    """
    """
    May be a better solution
    unique requires O(n^2) time computation
    but handles repeats
    """
    """
    # create a dictionary from the s2
    dict_of_s2 = {}
    unique_chars_of_s2 = np.unique(set_s2)
    for i in range(len(unique_chars_of_s2)):
        current_char = unique_chars_of_s2[i]
        indices = [i for i,val in enumerate(set_s2) if val==current_char]
        # indices = list(locate(set_s2, lambda x: x==str(current_char)))
        dict_of_s2[current_char] = indices


    dict_matches = []
    for chars in set_s1:
        if chars in set_s2:
            dict_matches.append(dict_of_s2[chars])
        else:
            return False
    # now that we have all matches see if we can create a sequence such that
    #  i, i+12 differs by 1 only
    
    return find_consecutive(dict_matches)
    """
    return False

def main():
    s1 = "trinitrophenylmethylnitramine"
    s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"
    print(checkInclusion(s1, s2))
    return None

if __name__ == "__main__":
    main()