'''
<자료 구조>
1. N 장의 카드
2. 1 -> N 순서대로 정렬

<로직>
1. for i in range(N)
2. i 버리고 i + 1은 맨 아래로
3. 1장 남을 때까지 반복
4. 마지막 남은 카드 출력
'''

from collections import deque

N = int(input())
Q = deque()

for card in range(1, N + 1):
    Q.append(card)

while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())

print(Q.popleft())