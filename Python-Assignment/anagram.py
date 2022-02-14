"""
    This program for find the anagrams of words from the given word list.
"""


def anagram(word_list):
    """
    This function takes the word list as an argumetent then finds the anagram from the list and returns it in the same group of anaragram.

    Args:
        word_list (list): list of the words.

    Returns:
        list: It's returning the group of anagram list.
    """
    anagram_dict = {}
    for i in word_list:
        sorted_string = ''.join(sorted(i))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(i)
        else:
            anagram_dict[sorted_string] = [i]
    return anagram_dict


word_list = input().split(',')
print(list(anagram(word_list).values()))
