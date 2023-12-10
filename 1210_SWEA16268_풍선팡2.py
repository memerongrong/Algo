'''
<자료 구조>
1. 이차원 리스트

<문제>
1. 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력
2. 타겟 + 상하좌우의 합이 가장 큰 것을 찾는다.
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]

    max_point = 0

    for r in range(N):
        for c in range(M):
            points = balloons[r][c]

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    points += balloons[nr][nc]

            max_point = max(max_point, points)

    print(f'#{tc} {max_point}')