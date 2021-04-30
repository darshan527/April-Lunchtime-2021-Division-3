for _ in range(int(input())):
    n = int(input())
    s = input()
    flag = False
    ones = 0
    for i in range(n):
        if s[i] == "1":
            ones += 1
            if ones >= ((i + 1) / 2):
                flag = True
                break
        # print(i, s[i], flag, ones)
    if flag:
        print("YES")
    else:
        print("NO")