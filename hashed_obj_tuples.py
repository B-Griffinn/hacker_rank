'''
Task
Given an integer, n , and n space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of .

Sample Input 0

2
1 2
Sample Output 0

3713081631934410656
'''

### Fastest Method / Second Approach and Revision ###
'''
x = tuple(integer_list)
print(hash(x))
'''
#####################

if __name__ == '__main__':
    n = int(input('Enter a n for spaces to be'))
    integer_list = map(int, input("Please enter integers").split())
    # print(n)
    # print(integer_list)

# we are given a number = n
# we are also given an integer list

# TODO
# create a tuple 't' with the integers given
# compute the hash of 't' and print result

# looping through int list
tuple_ready = []
for i in integer_list:
    # print(i)
    tuple_ready.append(i)

tupled_list_to_hash = tuple(tuple_ready)
print(hash(tupled_list_to_hash))
