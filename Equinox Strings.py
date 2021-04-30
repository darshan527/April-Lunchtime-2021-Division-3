chk = {"E", "Q", "U", "I", "N", "O", "X"}
for _ in range(int(input())):
    s, a, b = list(map(int, input().split()))
    sar = 0
    anu = 0
    for i in range(s):
        tst = False
        rs = input()
        if rs[0] in chk:
            sar += a
            tst = True
        if tst:
            continue
        anu += b
    print(sar, anu)
    if sar > anu:
        print("SARTHAK")
    elif anu > sar:
        print("ANURADHA")
    else:
        print("DRAW")
