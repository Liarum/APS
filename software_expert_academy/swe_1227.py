# Software Expert Academy pb.1227 미로2
'''
1: 벽
0: 길
2: 출발
3: 도착
'''
import sys
sys.stdin = open("input_1227.txt", "r")

def dfs(s, e):
    stack = [(s, e)]
    check[s][e] = 1

    while stack:
        x, y = stack.pop(-1)
        if board[x][y] == '3':
            return 1

        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 100 and 0 <= ny < 100 and check[nx][ny] == 0 and (board[nx][ny] == '0' or board[nx][ny] == '3'):
                stack.append((nx, ny))
                check[nx][ny] = 1
    return 0
    

diff = [(0, 1), (1, 0), (-1, 0), (0, -1)]
board = [0] * 100
check = [[0] * 100 for _ in range(100)]
for _ in range(10):
    t = int(input())
    for i in range(100):
        board[i] = input()
        check[i] = [0] * 100

    for i in range(100):
        for j in range(100):
            if board[i][j] == '2':
                answer = dfs(i, j)
                continue
            if board[i][j] == '1':
                check[i][j] = 1
    print("#{} {}".format(t, answer))