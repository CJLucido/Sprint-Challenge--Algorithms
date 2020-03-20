'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th_counter=0
    i=0
    if len(word) <= 1:
        return 0
    elif word[i] == "t" and word[i+1] == "h":
        add_next= 0
        if len(word[i+2:int(len(word))]) > 1:
            add_next += count_th(word[i+2:int(len(word))])

        return 1 + add_next
    else:
        th_counter += count_th(word[i+1:int(len(word))])
    return th_counter        





#  start from the end, head to string[0], exit at string  less than zero (because we need to check string 0 too)
#     maybe do this the other way actually
#  if the h has a t before it return 1


#had an issue with getting past the first "th" used recursion a second time, this first pass solution needs some work! but it passes the tests!