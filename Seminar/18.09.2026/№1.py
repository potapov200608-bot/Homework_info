def fib(N):
    if N > 0:
        N = N - 1
        if N == 0:
            return 0
        if N == 1:
            return 1
        else:
            return fib(N-1)+fib(N-2)
    else: return ValueError

n = int(input())
print(fib(n))