'''
8. Remove Duplicate Letters
Problem: Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.
'''

def remove_duplicate_letter(string):

    n=len(string)
    result=set()
    for letter in range(n):
        if letter not in result:
            result.add(string[letter])

    return ''.join(result)

string_input="prashant"

print(remove_duplicate_letter(string_input))