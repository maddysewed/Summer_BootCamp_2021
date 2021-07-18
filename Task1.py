N = int(input())
M = int(input())
H = int(input())
if 1 <= N <= H <= 100 and 1 <= M <= 100:
    tree_cnt = 0
    count = 0
    h = 0
    r = H % N
    while tree_cnt < M:
        h += H - r
        tree_cnt = h//N
        count += 1
    print(count)
else:
    print('Incorrect input')