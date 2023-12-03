#테스트케이스 수 입력
testCase = int(input())

#입력받은 테스트케이스 수만큼 반복
for tc in range(1, testCase+1):
    #정수의 수 N, 구간의 수 M 입력
    N, M = map(int, input().split())
    #정수들 입력
    nums = list(map(int, input().split()))
    #구간합을 저장할 배열
    result = []
    #구간합 저장
    for i in range(N - M+1):
        result.append(sum(nums[i:i+M]))
    #테스트케이스, 구간합 최댓값-최솟값 출력
    print(f"#{tc} {max(result)-min(result)}")