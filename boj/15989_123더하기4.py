# https://www.acmicpc.net/problem/15989

# 탐색이 아니라 점화식 + DP 로 접근해야함

repeat = int(input())

# limit = 101 # 100개정도 찍어보면서 점화식 진행 확인
limit = 10001
dp = [1] * limit  # 1. 1만 쓰는 경우로 초기화 (모든 수는 1로만 표현 가능하므로 기본 1가지)
# print('step 1:', dp)

# 2. 2를 쓰는 경우 추가
for i in range(2, limit):
    dp[i] += dp[i - 2]
    # print('step 2:', i, dp)

# 3. 3을 쓰는 경우 추가
for i in range(3, limit):
    dp[i] += dp[i - 3]
    # print('step 3:', i, dp)

def solution(dp, number):
    print(dp[number])
    pass

for _ in range(repeat):
    solution(dp, int(input()))