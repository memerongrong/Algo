'''
<문제 분석>
1. N*N 크기의 글자판에서, 길이가 M인 회문을 찾아 출력하시오.
1-1. 회문은 1개가 존재한다.
1-2. 가로뿐만 아니라 세로로 찾아질 수도 있다.

<자료 구조>
1. 2차원 리스트
'''


def find_palindrome(board):
    for line in board:
        for i in range(N - M + 1):
            word = line[i:M + i]
            if word == word[::-1]:
                return ''.join(word)
    return ''


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    char_list = []  # 입력받은 문자열을 저장할 리스트
    for i in range(N):
        char_list.append(list(input()))

    horizon_result = find_palindrome(char_list)
    if horizon_result:
        print(f'#{tc} {horizon_result}')

    else:
        rotated_list = list(map(list, zip(*char_list)))
        vertical_result = find_palindrome(rotated_list)
        print(f'#{tc} {vertical_result}')
