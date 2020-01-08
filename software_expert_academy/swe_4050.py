# Software Expert Academy pb.4050 재관이의 대량할인


for t in range(1, int(input()) + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    prices.sort()

    answer = 0
    idx = 1
    for i in range(N-1, -1, -1):
        if idx % 3 == 0:
            idx += 1
            continue
        answer += prices[i]
        idx += 1
    print("#{} {}".format(t, answer))
