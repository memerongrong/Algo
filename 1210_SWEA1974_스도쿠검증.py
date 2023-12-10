'''
<문제 분석>
1. 가로 9칸에 겹치는 수 X
2. 세로 9칸에 겹치는 수 X
3. 3*3 격자에 겹치는 수 X
4. 모든 조건을 만족할 경우 1, 아니면 0 출력

'''
def check_board(board):
    for line in board:
        if len(set(line)) < 9:
            return 0
    return 1


for tc in range(1, 1+int(input())):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku2 = list(zip(*sudoku))
    sudoku3 = []

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            sudoku3.append(sudoku[i][j] for i in range(x, x+3) for j in range(y, y+3))

    ans = check_board(sudoku) and check_board(sudoku2) and check_board(sudoku3)

    print(f'#{tc} {ans}')