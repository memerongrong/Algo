'''
<문제 분석>
1. 전체 종이의 크기는 N*N
2. 종이를 자르는 규칙
2-1. 전체 구역이 모두 같은 색이 아니라면 가로 세로 중간을 잘라 4구역으로 분할
2-2. 한 구역이 모두 같은 색이 될 때까지 2-1을 반복
3. 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하시오.

<출력 형태>
하얀색 색종이
파란색 색종이
'''

def devide(r, c, n):
    global white, blue

    color = paper[r][c]

    for i in range(r, r + n):
        for j in range(c, c + n):
            if color != paper[i][j]:
                devide(r, c, n//2)
                devide(r, c + n//2, n//2)
                devide(r + n//2, c, n//2)
                devide(r + n//2, c + n//2, n//2)

                return

    if color == 0:
        white += 1
    elif color == 1:
        blue += 1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

devide(0, 0, N)
print(white)
print(blue)