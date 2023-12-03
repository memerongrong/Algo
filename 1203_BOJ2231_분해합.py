# N = input()
# NtoNum = int(N)
# nums = list(N)
# M = NtoNum
# for i in range(len(nums)):
#     nums[i] = int(nums[i])
#     M += nums[i]
# print(f'생성자는 {NtoNum}, 분해합은 {M}입니다.')

##N은 생성자, M은 분해합
# N = input("자연수를 입력하세요: ")
# NtoNum = int(N)
# M = NtoNum + sum(map(int, N))
#
# print(f'생성자는 {NtoNum}, 분해합은 {M}입니다.')

#N은 분해합, M은 생성자의 최솟값
N = int(input())
for M in range(1, N+1):
    decompositionSum = M + sum(map(int, str(M)))
    if decompositionSum == N:
        print(M)
        break
else:
    print(0)