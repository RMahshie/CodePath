"""Practice for first codepath"""


def linear_search(lst, target):
    """find in thing"""
    for i, item in enumerate(lst):
        if target == item:
            return print(i)
    return print(-1)

def final_value_after_operations(operation):
    """stuff"""
    result = 1
    for item in operation:
        if item == "bouncy" or item == "flouncy":
            result+=1
        else:
            result -=1
    print(result)


def tiggerfy(word):
    """stuff"""
    for substr in ['t', 'i', 'gg', 'e', 'r']:
        word = word.replace(substr, '')
    print(word)

def non_decreasing(nums):
    numWrong = 0
    for i, num in enumerate(nums):
        if i == 0:
            continue
        if num < nums[i - 1]:
            numWrong += 1
    
    if numWrong > 1:
        print(False)
    else:
        print(True)


def find_missing_clues(clues, lower, upper):
    """stuff"""
    

    missing_range = []

    lowRange = 0
    highRange = 0
    returnList = []
    for i in range(lower, upper):
        highRange = i
        if i in clues:
            returnList.append([lowRange, highRange - 1])
            lowRange = i
    print(returnList)


clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
find_missing_clues(clues, lower, upper)

clues = [-1]
lower = -1
upper = -1
find_missing_clues(clues, lower, upper)
            
        