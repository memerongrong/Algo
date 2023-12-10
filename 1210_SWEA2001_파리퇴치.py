'''
<문제>
1. N*N 배열 안에서
2. M*M 크기의 파리채를 내려쳐 잡을 수 있는
3. 최대 파리의 수를 구하라.

<자료 구조>
1. 이차원 리스트
'''

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_dead = 0

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            dead = sum(flies[i][j] for i in range(r, r + M) for j in range(c, c + M))
            max_dead = max(max_dead, dead)

    print(f'#{tc} {max_dead}')