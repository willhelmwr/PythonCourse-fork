# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""

# Your Code Below:

def grow_string(word):
    new_word = ''
    for i in range(len(word)):
        new_word += word[:i+1]
    print(new_word)


grow_string('Code') #→ 'CCoCodCode'
grow_string('abc') #→ 'aababc'
grow_string('ab') #→ 'aab'


































# Solution:

# def grow_string(str):
#   result = ""
#   # On each iteration, add the substring of the chars 0..i
#   for i in range(len(str)):
#     result = result + str[:i+1]
#   return result

