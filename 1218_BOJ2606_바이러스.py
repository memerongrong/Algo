dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

M = int(input()) # 컴퓨터 대수
N = int(input()) # 연결된 쌍의 수

computers = [[0] * (M + 1) for _ in range(M + 1)]

for i in range(N):
    x, y = map(int, input().split())
    computers[x][y] = 1
    computers[y][x] = 1

visited = set()

def DFS(now):
    if now not in visited:
        visited.add(now)

    for next in range(M + 1):
        if computers[now][next] and next not in visited:
            DFS(next)

DFS(1)

print(len(visited) - 1)