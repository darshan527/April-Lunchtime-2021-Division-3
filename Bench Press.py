for _ in range(int(input())):
    n, w, wr = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    flag = False
    if w <= wr:
        print("YES")
        continue
    wd = dict()
    for i in weights:
        if i in wd:
            wd[i] += 1
        else:
            wd[i] = 1
    finalWeight = wr
    tmpWeight = 0
    for k, v in wd.items:
        if finalWeight == w:
            flag = True
            break
        if (v % 2) == 0:
            if finalWeight == w:
                flag = True
                break
