'''
<문제 분석>
1. 이진 탐색 게임에서 이기는 사람 찾기
2. A와 B의 목표 숫자가 다름

<출력>
#tc 이긴 사람
비긴 경우에는 0 출력
'''
from typing import List


def find(page, target_page):
    times = 0
    l, r = 1, page
    mid = (l + r) // 2

    while mid != target_page:
        if mid > target_page:
            r = mid
        elif mid < target_page:
            l = mid
        mid = (l + r) // 2
        times += 1

    return times


for tc in range(1, 1 + int(input())):
    P, Pa, Pb = map(int, input().split())

    A = find(P, Pa)
    B = find(P, Pb)

    winner = 'A'
    if B < A:
        winner = 'B'
    elif A == B:
        winner = 0

    print(f'#{tc} {winner}')