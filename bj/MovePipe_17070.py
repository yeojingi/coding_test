N = int(input())
rows = [ list(map(int, input().split(' '))) for _ in range(N) ]
hdp = [ [0] * N for _ in range(N) ]
ddp = [ [0] * N for _ in range(N) ]
vdp = [ [0] * N for _ in range(N) ]
dp = [ [0] * N for _ in range(N) ]

hdp[0][1] = 1

for j in range(1, N):
  for i in range(N):
    # if hdp[i][j] == 0 and ddp[i][j] == 0 and vdp[i][j] == 0:
    #   break

    if j+1 < N:
      if not (rows[i][j+1] == 1):
        hdp[i][j+1] = hdp[i][j] + ddp[i][j]
    if i+1 < N and j+1 < N:
      if not (rows[i+1][j] == 1 or rows[i][j+1] == 1 or rows[i+1][j+1] == 1) :
        ddp[i+1][j+1] = hdp[i][j] + ddp[i][j] + vdp[i][j]
    if i+1 < N:
      if not (rows[i+1][j] == 1):
        vdp[i+1][j] = ddp[i][j] + vdp[i][j]

#     dp[i][j] = hdp[i][j] + ddp[i][j] + vdp[i][j]

# print(*hdp, sep="\n")
# print('---')
# print(*ddp, sep="\n")
# print('---')
# print(*vdp, sep="\n")
# print('---')
# print(*dp, sep="\n")

print(hdp[N-1][N-1] + ddp[N-1][N-1] + vdp[N-1][N-1])