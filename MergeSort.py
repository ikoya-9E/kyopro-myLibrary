def MergeSort(lst):
    lst_length = len(lst)
    if lst_length <= 1:
        return lst
    mid = lst_length // 2
    lst_left = MergeSort(lst[:mid])
    lst_right = MergeSort(lst[mid:])
    return Merge(lst_left, lst_right)

def Merge(X, Y):
    X_length = len(X)
    Y_length = len(Y)
    X.append(9*10**18)
    Y.append(9*10**18)
    x, y = 0, 0
    res = []
    while x < X_length or y < Y_length:
        if X[x] < Y[y]:
            res.append(X[x])
            x += 1
        else:
            res.append(Y[y])
            y += 1
    return res