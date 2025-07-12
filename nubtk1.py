MOD = 1000000007

def partition(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        j = 1
        while True:
            pent1 = (j * (3 * j - 1)) // 2
            pent2 = (j * (3 * j + 1)) // 2
            if pent1 > i and pent2 > i:
                break
            if pent1 <= i:
                dp[i] = (dp[i] + ((-1)**(j+1)) * dp[i - pent1]) % MOD
            if pent2 <= i:
                dp[i] = (dp[i] + ((-1)**(j+1)) * dp[i - pent2]) % MOD
            j += 1
        if dp[i] < 0:
            dp[i] += MOD
    return dp[n]

# Read input from file
import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for _ in range(t):
    n = int(input())
    print(partition(n))

#End code