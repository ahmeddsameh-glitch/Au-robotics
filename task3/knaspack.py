N, c = map(int, input().split())
wt = []
val = []
for _ in range(N):
    wi, vi = map(int, input().split())
    wt.append(wi)
    val.append(vi)
dp = [[0 for i in range(c + 1)] for j in range(N)]
for w in range(c + 1):
    wi = wt[0]
    if wi <= w:
        dp[0][w] = val[0]
    else:
        dp[0][0] = 0
for i in range(1, N):
    wi = wt[i]
    vi = val[i]
    for w in range(1, c + 1):
        if wi <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wi] + vi)
        else:
            dp[i][w] = dp[i - 1][w]
print(dp[N - 1][c])
