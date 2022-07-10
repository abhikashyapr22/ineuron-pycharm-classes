def check_mono(arr):
    if arr[0] < arr[-1]:
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                continue
            else:
                return "NO"
    else:
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                continue
            else:
                return "NO"

    return "YES"


print(check_mono([2, 3, 4, 6, 7, 8, 9]))

"""def sec_largest(l):
    largest = -99999999999
    s_largest = -999999999999
    for i in l:
        if s_largest < largest < i:
            largest = i
            s_largest = largest
        elif largest > i > s_largest:
            s_largest = i

    return s_largest


print(sec_largest([8, 2, 3, 4, 4, 5]))"""
