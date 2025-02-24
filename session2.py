def transpose(matrix):
    """
    IN = [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]

    OUT = [1, 4, 7],
          [2, 5, 8],
          [3, 6, 9]
    """
    if not matrix or not matrix[0]:
        return matrix

    row, col = len(matrix), len(matrix[0])
    result = []

    for _ in range(col):
        result.append([0] * row)

    for i in range(row):
        for j in range(col):
            result[j][i] = matrix[i][j]

    return(result)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))


def reverse_list(lst):
    l, r = 0, len(lst) - 1

    while (l <= r):
        leftElement = lst[l]
        lst[l] = lst[r]
        lst[r] = leftElement
        l+=1
        r-=1
    return lst


lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))



def remove_dupes(lst):
    """
    items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
    result = 4

    items = ["extract of malt", "haycorns", "honey", "thistle"]
    result = 4

    items["a", "a", "a"]
    result = 0

    items[]
    result = 0

    go through the list and use the index function and see if that index is earlier than the one we are at now so then i will delete from the list.
    """
    for i in range(len(lst)):
        if lst.index(lst[i]) < i:
            lst.remove(lst[i])
            i -= 1
    return len(lst)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))

items = ["a", "a"]
print(remove_dupes(items))