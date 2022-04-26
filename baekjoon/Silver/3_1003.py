# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }


# def fibo(n):
#     global a
#     global b
#     if n == 0:
#         a += 1
#         return 0
    
#     elif n == 1:
#         b += 1
#         return 1
    
#     else:
#         return fibo(n - 1) + fibo(n - 2)
    
# m = int(input())
# for i in range(m):
#     s = int(input())
#     a = 0
#     b = 0
    
#     fibo(s)
#     print(a, b)


dp = [[-1, -1] for _ in range(50)]

dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, 50):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1]
    

T = int(input())
for tc in range(T):
    n = int(input())
    
    print(*dp[n])