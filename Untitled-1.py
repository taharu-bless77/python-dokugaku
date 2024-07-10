def permutation(n, k):
    result = 1
    for x in range(n - k + 1, n + 1):
        result *= x
    return result

print(permutation(7,7))