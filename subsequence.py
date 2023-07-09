def nondecsub(l, threshold=None):
    nums = []
    for i, e in enumerate(l):
        print(i)
        print(e)
        if threshold is None or e >= threshold:
            a = nondecsub(l[i + 1:], e)
            print(a)
            for x in a:
                print(x)
                nums.append([e] + x)
        else:
            continue
    nums.append([])
    print(nums)
    return nums