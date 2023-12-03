#입력받은 테스트케이스만큼 반복
for testCase in range(int(input())):
    numOfWords = int(input())
    words = [] #word를 저장할 빈 리스트 생성
    for num in range(numOfWords): #입력받은 단어의 수만큼 입력 반복 실행
        words.append(input()) #입력받은 word를 리스트에 저장
    for i in range(numOfWords): #words 리스트의 인자 수만큼 아래 로직 반복
        for j in range(numOfWords):
            if i != j: #i와 j가 일치하지 않으면(=자신을 제외하고)
                wordSum = words[i] + words[j] #리스트 내 다른 모든 인자와의 문자열 합 연산 후
                if wordSum == wordSum[::-1]: #회문인지 검사 후, 회문이라면
                    print(wordSum) #회문을 출력하고
                    exit(0) #루프 종료

    print(0) #회문이 없다면 0 출력