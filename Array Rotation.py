n = int(input())
arr = list(map(int, input().split()))
q = int(input())
qarr = list(map(int, input().split()))
m = 1000000007
sarr = sum(arr) % m
for _ in range(q):
    sarr = (sarr + sarr) % m
    print(sarr)
