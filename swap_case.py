'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
'''


def swap_case(s):
    result = ""

    for i in s:
        # print(i)
        if i == i.upper():
            result += i.lower()
        else:
            result += i.upper()

    return result


# Understand
# we are given a string of words seperated by a space
# we are asked to change every case of upper case to lower and vice versa

# PLAN
# we need to split each word in order to check the case of each letter
# swap cases
# put str back together and return with new cases

# create a str to return when complete
# loop through our input
# if index of our input is upper, then udpate our result str with that index to be lower
# run the opposite conditional for lower to upper
# return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
