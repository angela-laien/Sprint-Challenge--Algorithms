'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
# check if the length if the word is bigger or equal to "th"
    if len(word) < len('th'):
        return 0 
# If the first two letters are "th", count += 1
    elif word[:2] == "th":
        count += 1
# If not "th", move on to the next letter
    return count + count_th(word[1:])