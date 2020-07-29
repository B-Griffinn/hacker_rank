'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is [2 3 6 6 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # print(n)

# UNDERSTAND
# - input n = an integer of how many scores we receive in the lsit
# - second input = a list containging integers with the length of n
# we need to serch the list for the second highest number

# PLAN
# loop trhough our list
# create a new list to hold all items
new_lst = []
for i in arr:
    new_lst.append(i)

new_lst.sort()
# print(new_lst)
# create a list to hold dupe free
dupe_free = list()
for x in new_lst:
    # dupe_free.add(x)

    if x not in dupe_free:
        dupe_free.append(x)

# print(dupe_free)
print(dupe_free[-2])
