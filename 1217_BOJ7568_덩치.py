'''
<자료 구조>
1. 전체 사람의 수 N
1-1. 2 <= N <= 50
2. 행별로 키 x, 몸무게 y = (x, y)
2-2. 10 <= x, y <= 200

<로직>
1. 가로 세로 20 <= i <= 200인 인접행렬 만들고
2. 입력받은 x, y를 배정하고
3. (200, 200)부터 너비우선 탐색을 통해 순위 정하기
3-1. (x, y)가 모두 작아야만 더 낮은 등수
3-2. (x, y) 중 하나만 작거나 크다면 같은 등수
3-3. 너비우선 탐색을 통해 (x, y) 모두 작은 아이를 만나면 낮은 등수 부여 시작
3-4. 다시 (x, y) 모두 작은 아이를 만나면 다음 등수 부여 시작
4. 입력받은 순서대로 등수를 출력해야 한다.

이렇게 풀려고 했는데.. 안 됐다.

정렬된 리스트 만들고, 맨 뒤에서부터 앞 차례 아이와 비교하고,
원래 리스트에서 값에 해당하는 인덱스를 찾아 ans 리스트에 등수 입력함.
'''

# xy_list = []
# N = int(input())
# ans = [0] * N
# rank = 1
# cnt = 0 # 동순위 카운트
# for _ in range(N):
#     xy_list.append(list(map(int, input().split())))
# sorted_list = sorted(xy_list)
#
# for i in range(N - 1, -1, -1): # 몸무게순으로 정렬된 순서에서 거꾸로 시작
#     order = xy_list.index(sorted_list[i])
#
#     # 정렬된 리스트에서 내가 앞 아이보다 둘 다 크다면, 나까지만 동점 입력하고, 다음 아이에게는 다음 등수 부여 후 동점자 수 리셋
#     if sorted_list[i][0] > sorted_list[i - 1][0] and sorted_list[i][1] > sorted_list[i - 1][1]:
#         ans[order] = rank
#         rank += cnt + 1
#         cnt = 0
#
#     # 하나라도 작거나 같으면 동순위 입력하고, cnt(동점자) +1
#     else:
#         ans[order] = rank
#         cnt += 1
#
# print(*ans)

N = int(input())
info = []
rank = [1] * N

for _ in range(N):
    x, y = map(int, input().split())
    info.append((x, y))

for now in range(N):
    now_w, now_h = info[now]

    for other in range(now + 1, N):
        other_w, other_h = info[other]

        if now_w > other_w and now_h > other_h:
            rank[other] += 1

        elif now_w < other_w and now_h < other_h:
            rank[now] += 1

print(*rank)