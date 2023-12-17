'''
<자료 구조>
1. 마당은 직사각형 모양(R * C)
2. . = 필드, o = 늑대, # = 울타리, v = 양
3. 수평, 수직 이동 가능

<로직>
1. 영역 안의 양, 늑대 수 비교
1-1. 양이 많으면 양 수 카운트
1-2. 늑대가 많거나 같으면 늑대 수 카운트
'''

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

alive_sheep = 0
alive_wolf = 0

stack = []
def DFS(r, c):
    global alive_sheep
    global alive_wolf
    stack.append((r, c))

    curr_sheep = 0
    curr_wolf = 0

    if yard[r][c] == 'o':
        curr_sheep += 1
    elif yard[r][c] == 'v':
        curr_wolf += 1

    yard[r][c] = '#'

    while stack:
        r, c = stack.pop()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < R and 0 <= nc < C and yard[nr][nc] != '#':
                if yard[nr][nc] == 'v':
                    curr_wolf += 1
                elif yard[nr][nc] == 'o':
                    curr_sheep += 1

                yard[nr][nc] = '#'
                stack.append((nr, nc))

    if curr_sheep > curr_wolf:
        alive_sheep += curr_sheep
    elif curr_wolf >= curr_sheep:
        alive_wolf += curr_wolf

R, C = map(int, input().split())
yard = []

for _ in range(R):
    yard.append(list(input()))

for r in range(R):
    for c in range(C):
        if yard[r][c] != '#':
            DFS(r, c)

print(alive_sheep, alive_wolf)