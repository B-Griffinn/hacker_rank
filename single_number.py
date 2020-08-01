'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


def singleNumber(nums):
    # dict = {0: times its counted, 1: times its counted...}
    storage = dict()

    result = 0

    # loop through our list of nums
    for i in nums:
        # if i not in dict, add it at its Key
        if i not in storage:
            storage[i] = 1
        elif i in storage:
            storage[i] += 1

    # print(storage)

    for j in storage:
        if storage[j] == 1:
            result = j

    # print(storage)
    return result


if __name__ == '__main__':
    nums_list = [4, 1, 2, 1, 2]
    print(singleNumber(nums_list))
